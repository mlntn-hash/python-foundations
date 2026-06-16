import re
import argparse
from collections import Counter

def parser_log(filename : str, top: int = 10):
    ip_counter = Counter()
    response_times = []

    with open(filename, "r") as f:
        for line in f:
            match = re.search(r'(\d+\.\d+\.\d+\.\d+).*(\d+\.\d+)$', line)
            if match:
                ip = match.group(1)
                response_time = float(match.group(2))
                ip_counter[ip] += 1
                response_times.append(response_time)

    return ip_counter, response_times

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Parse nginx access log")
    parser.add_argument("file", help="Path to log file")
    parser.add_argument("--top", type=int, default=10, help="Number of top IPs")
    args = parser.parse_args()

    ip_counter, response_times = parser_log(args.file, args.top)

    print(f"Топ-{args.top} IP:")
    for ip, count in ip_counter.most_common(args.top):
        print(f" {ip}: {count} запитів")

    if response_times:
        avg = sum(response_times) / len(response_times)
        print(f"Середній час відповіді: {avg:.3f}s")


