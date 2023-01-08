import asyncio
import aiohttp
import json
from os import path
import requests
error_msg = ["needs to review the security of your connection before proceeding", "Retrying, please wait", "404 Not Found", "down for maintenance", "The backend is currently offline","Something was wrong with your request"]
down = []
closed_trackers = []

choice = input("1. TrackerChecker\n2. Add new tracker\nSelect mode: ")


if choice == "1":
    r = requests.get("https://raw.githubusercontent.com/NDDDDDDDDD/TrackerChecker/main/trackers.json")
    trackers = r.text
    URLS = json.loads(trackers)
    conn = aiohttp.TCPConnector(limit_per_host=100, limit=100)
    PARALLEL_REQUESTS = len(URLS)
    async def gather_with_concurrency(n):
        timeout = aiohttp.ClientTimeout(total=30)
        semaphore = asyncio.Semaphore(n)
        session = aiohttp.ClientSession(connector=conn, timeout=timeout)
        print("Starting...")

        async def get(url, name, search_term):
            async with semaphore:
                try:
                    async with session.get(url, ssl=False) as response:
                        obj = await response.read()
                        for error in error_msg:
                            if error in str(obj):
                                down.append(name)
                            else:
                                continue
                        if response.status > 500:
                            down.append(name)
                        elif search_term in str(obj):
                            closed_trackers.append(name)
                        elif "https://redbits.xyz/login" in str(response.url):
                            closed_trackers.append(name)
                        elif "https://pretome.info/index.php?page=home&msg=not_qualified" in str(response.url):
                            closed_trackers.append(name)
                        else:
                            print(f"{name} is open! {response.url}")
                except asyncio.exceptions.TimeoutError:
                    down.append(name)
                    pass

        await asyncio.gather(
            *(
                get(
                    url.get("url"),
                    url.get("name"),
                    url.get("search_term"),
                )
                for url in URLS
            )
        )
        await session.close()


    if __name__ == "__main__":
        loop = asyncio.get_event_loop()
        loop.run_until_complete(gather_with_concurrency(PARALLEL_REQUESTS))
        conn.close()
    def sortt(status_):
        tempp = status_
        status_.sort()
        status_ = str(status_).replace("[", "")
        status_ = status_.replace("'", "")
        status_.replace("'", "")
        status_ = status_.replace("]", "")
        if down == tempp:
            print(f"\nCurrently down: {status_}")
        else:
            print(f"\nCurrently closed: {status_}")
    sortt(down)
    sortt(closed_trackers)

    input("Done! Press enter to exit ")

elif choice == "2":
    users = [
        {
            "name": "",
            "url": "",
            "search_term": ""
        },
    ]

    trackername = input("Trackers name: ")
    signup = input("Sign up URL: ")
    term = input("Search term: ")
    for user in users:
        user['name'] = trackername
        user['url'] = signup
        user['search_term'] = term

    my_path = 'C:/ ADD PATH HERE IN CODE'
    if path.exists(my_path):
        with open(my_path, 'r') as file:
            previous_json = json.load(file)
            users = previous_json + users

    with open(my_path, 'w') as file:
        json.dump(users, file, indent=4)
        input("Done! Press enter to exit ")
