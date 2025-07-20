import requests

def check_pod_health():
    try:
        response = requests.get("https://httpbin.org/status/200", timeout=5)
        if response.status_code == 200:
            print("healthy pod")
            print(response.elapsed)
            return True
        else:
            print(f"unhealthy pod: status code {response.status_code}")
            print(response.elapsed)
            return False
    except requests.RequestException as e:
        print(f"unhealthy pod: connection error - {str(e)}")
        
        return False

# Execute the function
check_pod_health()