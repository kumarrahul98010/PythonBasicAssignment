import requests
import time

def check_urls(urls, interval=10, max_backoff=60):
    backoff = {url: interval for url in urls}

    while True:
        results = []
        for url in urls:
            try:
                response = requests.get(url)
                status = response.status_code
                results.append(f"{url} - {status} {response.reason}")

                if 400 <= status < 600:
                    results.append(f"{url} is down")
                    backoff[url] = min(backoff[url] * 2, max_backoff)  # Increase backoff
                else:
                    backoff[url] = interval  # Reset backoff on success
            except requests.RequestException as e:
                results.append(f"Error checking {url}: {e}")
                backoff[url] = min(backoff[url] * 2, max_backoff)  # Increase backoff

        print("\n".join(results))
        time.sleep(min(backoff.values()))  # Wait based on the smallest backoff

urls = [
    "http://www.example.com/nonexistentpage",
    "http://httpstat.us/404",
    "http://httpstat.us/500",
    "https://www.google.com/"
]

check_urls(urls)
