import requests
import time

def check_urls(urls, interval=10):
    while True:
        results = []
        for url in urls:
            try:
                response = requests.get(url)
                status = response.status_code
                results.append(f"{url} - {status} {response.reason}")
                if 400 <= status < 600:
                    results.append(f" {url} is down")
            except requests.RequestException as e:
                results.append(f"Error checking {url}: {e}")
        print("\n".join(results))
        time.sleep(interval)

urls = [
    "http://www.example.com/nonexistentpage",
    "http://httpstat.us/404",
    "http://httpstat.us/500",
    "https://www.google.com/"
]

check_urls(urls)
