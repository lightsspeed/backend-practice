# grafana_metrics_app.py

import random
import time
import threading
from prometheus_client import start_http_server, Gauge, Counter

# Gauges (for tracking values over time)
cpu_usage = Gauge("chaos_cpu_usage_percent", "Simulated CPU usage (%)")
memory_usage = Gauge("chaos_memory_mb", "Simulated memory usage in MB")
disk_read = Gauge("chaos_disk_read_mb", "Disk read throughput (MB/s)")
disk_write = Gauge("chaos_disk_write_mb", "Disk write throughput (MB/s)")

# Counter (for counting total requests, could be used with HTTP endpoints)
request_counter = Counter("chaos_http_requests_total", "Simulated HTTP requests", ['endpoint'])

def generate_metrics():
    while True:
        # Simulate values
        cpu = random.uniform(0, 100)
        mem = random.uniform(100, 16000)
        read = random.uniform(0, 300)
        write = random.uniform(0, 500)
        endpoint = random.choice(["/home", "/api/data", "/login"])

        # Update metrics
        cpu_usage.set(cpu)
        memory_usage.set(mem)
        disk_read.set(read)
        disk_write.set(write)
        request_counter.labels(endpoint=endpoint).inc()

        print(f"[METRICS] CPU: {cpu:.2f}%, MEM: {mem:.2f}MB, Read: {read:.2f}, Write: {write:.2f}")

        time.sleep(2)  # simulate every 2 seconds

if __name__ == "__main__":
    start_http_server(8000)  # Expose on /metrics
    print("🚀 Metrics server running at http://localhost:8000/metrics")
    thread = threading.Thread(target=generate_metrics)
    thread.start()
