import re
log_data = "User 192.168.1.1 logged in. Failed login from 10.0.0.55. Connection closed by 192.168.1.1."

ips = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", log_data)
print("All IPs found:", ips)

unique_ips = set(ips)
print("Unique IPs:", unique_ips)
print("Number of unique IP addresses:", len(unique_ips))