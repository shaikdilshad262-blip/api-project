import urllib.request
import urllib.error
import time


def check_api(url):
    print("\nChecking API:", url)

    start_time = time.time()

    try:
        request = urllib.request.Request(
            url,
            headers={"User-Agent": "Python API Monitor"}
        )

        with urllib.request.urlopen(
            request, timeout=10
        ) as response:

            status = response.status
            response.read(100)

        end_time = time.time()

        response_time = (end_time - start_time) * 1000

        print("Status Code:", status)
        print("Response Time:", round(response_time, 2), "ms")
        print("API Status: Working")

    except urllib.error.HTTPError as error:
        print("Status Code:", error.code)
        print("API returned an HTTP error.")

    except Exception as error:
        print("API Check Failed:", error)


def main():
    print("\n===== API PERFORMANCE MONITOR =====")

    url = input("Enter API URL: ")

    if not url.startswith(("http://", "https://")):
        print("Please enter a valid URL.")
        return

    try:
        count = int(input("Number of checks: "))

        if count < 1 or count > 20:
            print("Choose between 1 and 20 checks.")
            return

    except ValueError:
        print("Please enter a valid number.")
        return

    for i in range(count):
        print("\nCheck", i + 1)
        check_api(url)

        if i < count - 1:
            time.sleep(2)


main()
