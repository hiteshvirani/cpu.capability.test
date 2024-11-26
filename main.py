import asyncio
import httpx
import time
import random


async def make_request(client: httpx.AsyncClient, url: str) -> float:
    """Makes a single request to the given URL and returns the response time."""
    start_time = time.monotonic()
    try:
        response = await client.get(url)
        response.raise_for_status()  # Raise an error for bad HTTP status codes
    except httpx.RequestError as e:
        print(f"Request failed: {e}")
        return -1  # Indicates a failed request
    end_time = time.monotonic()
    return end_time - start_time


async def perform_requests(url: str, total_requests: int):
    """Perform the specified number of requests to the given URL."""
    async with httpx.AsyncClient() as client:
        tasks = [make_request(client, url) for _ in range(total_requests)]
        response_times = await asyncio.gather(*tasks)
    
    # Filter out failed requests
    successful_times = [t for t in response_times if t >= 0]
    
    if successful_times:
        avg_time = sum(successful_times) / len(successful_times)
        max_time = max(successful_times)
        min_time = min(successful_times)
    else:
        avg_time = max_time = min_time = None
    
    return {
        "total_requests": total_requests,
        "successful_requests": len(successful_times),
        "failed_requests": total_requests - len(successful_times),
        "avg_time": avg_time,
        "max_time": max_time,
        "min_time": min_time
    }


async def normal_mode(url: str, total_requests: int):
    """Send requests in normal mode."""
    print(f"Normal mode: Sending {total_requests} requests at once...")
    result = await perform_requests(url, total_requests)
    print_result(result)


async def continuous_mode(url: str, total_requests: int, interval: int, max_time: int):
    """Send requests continuously at fixed intervals for a limited time."""
    print(f"Continuous mode: Sending {total_requests} requests every {interval} seconds for up to {max_time} seconds...")
    start_time = time.monotonic()
    while time.monotonic() - start_time < max_time:
        result = await perform_requests(url, total_requests)
        print_result(result)
        await asyncio.sleep(interval)
    print("Continuous mode completed.")


async def random_continuous_mode(url: str, request_range: tuple, sleep_range: tuple, max_time: int):
    """Send requests with random numbers and random intervals for a limited time."""
    print(f"Random Continuous mode: Sending requests randomly in range {request_range} every {sleep_range} seconds for up to {max_time} seconds...")
    start_time = time.monotonic()
    while time.monotonic() - start_time < max_time:
        random_requests = random.randint(*request_range)
        random_sleep = random.uniform(*sleep_range)
        print(f"Sending {random_requests} requests, next batch in {random_sleep:.2f} seconds...")
        result = await perform_requests(url, random_requests)
        print_result(result)
        await asyncio.sleep(random_sleep)
    print("Random Continuous mode completed.")


def print_result(result):
    """Print the results of the request batch."""
    print("\nResults:")
    print(f"Total requests: {result['total_requests']}")
    print(f"Successful requests: {result['successful_requests']}")
    print(f"Failed requests: {result['failed_requests']}")
    print(f"Average response time: {result['avg_time']:.2f} seconds" if result['avg_time'] else "N/A")
    print(f"Maximum response time: {result['max_time']:.2f} seconds" if result['max_time'] else "N/A")
    print(f"Minimum response time: {result['min_time']:.2f} seconds" if result['min_time'] else "N/A")


async def main():
    url = input("Enter the endpoint URL: ").strip()
    mode = input("Select mode (normal/continuous/random): ").strip().lower()
    
    if mode == "normal":
        total_requests = int(input("Enter the number of requests to send: "))
        await normal_mode(url, total_requests)
    elif mode == "continuous":
        total_requests = int(input("Enter the number of requests to send per batch: "))
        interval = int(input("Enter the interval between batches (in seconds): "))
        max_time = int(input("Enter the maximum time for continuous mode (in seconds): "))
        await continuous_mode(url, total_requests, interval, max_time)
    elif mode == "random":
        min_requests = int(input("Enter the minimum number of requests per batch: "))
        max_requests = int(input("Enter the maximum number of requests per batch: "))
        min_interval = float(input("Enter the minimum interval between batches (in seconds): "))
        max_interval = float(input("Enter the maximum interval between batches (in seconds): "))
        max_time = int(input("Enter the maximum time for random continuous mode (in seconds): "))
        await random_continuous_mode(url, (min_requests, max_requests), (min_interval, max_interval), max_time)
    else:
        print("Invalid mode selected. Exiting.")


if __name__ == "__main__":
    asyncio.run(main())
