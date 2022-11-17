import asyncio
import aiohttp
import json
from os import path

closed_trackers = []

choice = input("1. TrackerChecker\n2. Add new tracker\nSelect mode: ")

if choice == "1":
    f = open('trackers.json')
    data = json.load(f)
    URLS = data
    conn = aiohttp.TCPConnector(limit_per_host=100, limit=100, ttl_dns_cache=300)
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
                        status_code = response.status
                        if status_code > 500:
                            print(f"{name} is down!")
                            print(f"error code: {status_code}")
                        elif search_term in str(obj):
                            closed_trackers.append(name)
                        else:
                            print(f"{name} is open! {response.url}")
                except asyncio.exceptions.TimeoutError:
                    print(f"{name} timed out!")
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
    input("Done! Press any button to exit ")

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
