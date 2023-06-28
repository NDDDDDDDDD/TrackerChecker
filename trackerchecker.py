import asyncio
import aiohttp
import json
import requests

error_msg = ["needs to review the security of your connection before proceeding", "Open registration is currently disabled", "bing.com", "We do not allow members to register multiple accounts with the same IP Address", "Nebulance is temporarily offline for planned maintenance. Leave your torrents seeding in your client and we will be back shortly.", "Retrying, please wait", "404 Not Found", "down for maintenance", "The backend is currently offline","and the server is refusing to fulfill it", "</h3></td></tr></table></body></html>"]
down = []
temp_down = []
closed_trackers = []

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
                            temp_down.append(name)
                    if response.status >= 500 or name in temp_down:
                        down.append(name)
                    elif search_term in str(obj):
                        closed_trackers.append(name)
                    elif "https://redbits.xyz/login" in str(response.url):
                        closed_trackers.append(name)
                    elif "https://torrentseeds.org/buyinvite" in str(response.url):
                        closed_trackers.append(name)
                    elif "https://pretome.info/index.php?page=home&msg=not_qualified" in str(response.url):
                        closed_trackers.append(name)
                    else:
                        print(f"{name} is open! {response.url}")
            except (asyncio.exceptions.TimeoutError, aiohttp.client_exceptions.ServerDisconnectedError,
                    aiohttp.client_exceptions.ClientConnectorError) as error:
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
    status_.sort()
    status_str = ", ".join(status_)
    if down == status_:
        print(f"\nCurrently down: {status_str}")
    else:
        print(f"\nCurrently closed: {status_str}")


sortt(down)
sortt(closed_trackers)

input("Done! Press enter to exit ")
