logs = [
    "2026-03-24 10:01:05;IP:192.168.1.10;STATUS:200;USER:admin",
    "2026-03-24 10:01:08;IP:10.0.0.5;STATUS:401;USER:root",
    "2026-03-24 10:01:10;IP:10.0.0.5;STATUS:401;USER:guest",
    "2026-03-24 10:01:12;IP:192.168.1.12;STATUS:200;USER:user1",
    "2026-03-24 10:01:15;IP:10.0.0.5;STATUS:401;USER:admin"
]

from functools import reduce

parsed_logs = map(lambda line: {
    "ip": line.split(";")[1].split(":")[1],
    "status": line.split(";")[2].split(":")[1]
}, logs)

failed_attempts = filter(lambda log: log["status"] == "401", parsed_logs)

failed_ips = map(lambda log: log["ip"], failed_attempts)

attack_report = reduce(
    lambda acc, ip: {**acc, ip: acc.get(ip, 0) + 1},
    failed_ips,
    {}
)

print(attack_report) 
