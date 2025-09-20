import requests
import time

def calculate(load_balancer_ip, load_balancer_port):
    total_time = 0
    total_requests = 100
    dest = f"http://{load_balancer_ip}:{load_balancer_port}"
    print(f"Sending {total_requests} to load balancer...\n")
    
    start_time = time.time()
    for i in range(total_requests):
        try:
            start = time.time()
            response = requests.get(dest)
            end = time.time()
            response_time = (end - start)* 1000 # milliseconds
            total_time = total_time + response_time
            successful_req = successful_req + 1
        except Exception as e:
            print(f"Request {i + 1} : failed ({e})")
    end_time = time.time()
    avg_response_time = total_time/successful_req if successful_req > 0 else float('inf')
    total_duration = end_time - start_time
    throughput = successful_req / total_duration if total_duration > 0 else 0
    return avg_response_time, throughput

calculate(load_balancer_ip="10.0.1.1",load_balancer_port= 80)