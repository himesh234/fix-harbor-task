Parse the Apache access log located at /app/access.log and generate a summary report.

Success criteria:
1. Create a valid JSON file at /app/report.json.
2. Include a key named "total_requests" containing the total number of requests.
3. Include a key named "unique_ips" containing the number of distinct client IPs.
4. Include a key named "top_path" containing the most frequently requested path.
