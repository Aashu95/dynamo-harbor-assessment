There is an Apache-style access log file named `access.log` in your working directory. 

Write a script to parse this log file and summarize the traffic. You must evaluate the data and generate a final report that strictly adheres to the following success criteria:

1. **Output Format:** Save your findings as a valid JSON file named exactly `report.json` in the current working directory.
2. **Total Requests:** The JSON object must contain a key named `"total_requests"` with an integer value representing the exact total number of requests (lines) in the log.
3. **Unique IPs:** The JSON object must contain a key named `"unique_ips"` with an integer value representing the exact count of unique client IP addresses found in the log.
4. **Top Path:** The JSON object must contain a key named `"top_path"` with a string value representing the single most frequently requested URL path.

Ensure your solution executes successfully and generates the required file without requiring any human intervention.
