import asyncio
import aiohttp
import json
from os import path
import requests
down = []
closed_trackers = []

choice = input("1. TrackerChecker\n2. Add new tracker\nSelect mode: ")

if choice == "1":
    r = requests.get("https://raw.githubusercontent.com/NDDDDDDDDD/TrackerChecker/main/trackers.json")
    lol = r.text
    URLS = json.loads(lol)
    conn = aiohttp.TCPConnector(limit_per_host=100, limit=100)
    PARALLEL_REQUESTS = len(URLS)
    async def gather_with_concurrency(n):
        timeout = aiohttp.ClientTimeout(total=10)
        semaphore = asyncio.Semaphore(n)
        session = aiohttp.ClientSession(connector=conn, timeout=timeout)
        print("Starting...")

        async def get(url, name, search_term):
            async with semaphore:
                try:
                    async with session.get(url, ssl=False) as response:
                        obj = await response.read()
                        status_code = response.status
                        if status_code > 500 or "needs to review the security of your connection before proceeding" in str(obj):
                            down.append(name)
                        elif "The backend is currently offline" in str(obj):
                            down.append(name)
                        elif "down for maintenance" in str(obj):
                            down.append(name)
                        elif search_term in str(obj):
                            closed_trackers.append(name)
                        elif "404 Not Found" in str(obj):
                            down.append(name)
                        elif "The server load is very high at the moment" in str(obj):
                            down.append(name)
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

    closed_trackers.sort()
    closed_trackers = str(closed_trackers).replace("[", "")
    closed_trackers = closed_trackers.replace("'", "")
    closed_trackers = closed_trackers.replace("]", "")
    print(f"\nClosed trackers: {closed_trackers}")
    down.sort()
    down = str(down).replace("[", "")
    down = down.replace("'", "")
    down = down.replace("]", "")
    print(f"Currently down: {down}")
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

    my_path = 'trackers.json'
    if path.exists(my_path):
        with open(my_path, 'r') as file:
            previous_json = json.load(file)
            users = previous_json + users

    with open(my_path, 'w') as file:
        json.dump(users, file, indent=4)
        input("Done! Press enter to exit ")
