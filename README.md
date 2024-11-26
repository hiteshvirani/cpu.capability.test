# Server Stress Testing Tool

## Description

This tool is designed to test the performance and capacity of your server by sending a high volume of HTTP requests under various modes. It provides statistics like average response time, maximum time, and minimum time to help analyze server performance.

---

## Features

- **Normal Mode**: Sends a defined number of requests all at once.
- **Continuous Mode**: Sends requests in batches at regular intervals for a set duration.
- **Random Continuous Mode**: Sends random-sized batches of requests at random intervals for a set duration.
- **Detailed Statistics**: Reports total, successful, and failed requests, along with response times.
- **Fault Tolerance**: Handles failed requests gracefully and excludes them from metrics.

---

## Requirements

- Python 3.8 or higher.
- Install the required dependency:
  ```bash
  pip install httpx
Usage
Run the script using:

bash
Copy code
python stress_test_tool.py
Enter the required parameters based on the selected mode:

Normal Mode:
Total requests: Number of requests to send.
Continuous Mode:
Total requests per batch.
Interval between batches (seconds).
Maximum time to run the test (seconds).
Random Continuous Mode:
Range for the number of requests per batch (e.g., 500–1000).
Range for intervals between batches (e.g., 5–10 seconds).
Maximum time to run the test (seconds).
Example Scenarios
Normal Mode
URL: https://example.com/api
Requests: 10000
Command:

bash
Copy code
python stress_test_tool.py
Input:

text
Copy code
Enter the endpoint URL: https://example.com/api
Select mode (normal/continuous/random): normal
Enter the number of requests to send: 10000
Continuous Mode
URL: https://example.com/api
Requests: 50 per batch
Interval: 2 seconds
Maximum Time: 30 seconds
Input:

text
Copy code
Enter the endpoint URL: https://example.com/api
Select mode (normal/continuous/random): continuous
Enter the number of requests to send per batch: 50
Enter the interval between batches (in seconds): 2
Enter the maximum time for continuous mode (in seconds): 30
Random Continuous Mode
URL: https://example.com/api
Request Range: 500–1000
Sleep Range: 5–10 seconds
Maximum Time: 60 seconds
Input:

text
Copy code
Enter the endpoint URL: https://example.com/api
Select mode (normal/continuous/random): random
Enter the minimum number of requests per batch: 500
Enter the maximum number of requests per batch: 1000
Enter the minimum interval between batches (in seconds): 5
Enter the maximum interval between batches (in seconds): 10
Enter the maximum time for random continuous mode (in seconds): 60
Output
The tool prints the following statistics after each batch of requests:

Total requests.
Successful and failed requests.
Average, maximum, and minimum response times.
Example:

text
Copy code
Results:
Total requests: 50
Successful requests: 48
Failed requests: 2
Average response time: 0.234 seconds
Maximum response time: 0.501 seconds
Minimum response time: 0.123 seconds
License
This project is licensed under the MIT License. Feel free to use and modify it as needed.

yaml
Copy code

---

### **Highlights**
- The script and README are designed to be clear and user-friendly.
- The **limit feature** ensures tests don't run indefinitely.
- Detailed **examples** and **instructions** make it easy to use.

Let me know if you need further enhancements!