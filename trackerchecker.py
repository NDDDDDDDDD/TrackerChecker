import asyncio
import aiohttp
import json

error_msg = [
    "needs to review the security of your connection before proceeding",
    "Open registration is currently disabled",
    "bing.com",
    "We do not allow members to register multiple accounts with the same IP Address",
    "Nebulance is temporarily offline for planned maintenance. Leave your torrents seeding in your client and we will be back shortly.",
    "Retrying, please wait",
    "404 Not Found",
    "down for maintenance",
    "The backend is currently offline",
    "and the server is refusing to fulfill it",
    "</h3></td></tr></table></body></html>",
]
closed_url_msg = [
    "https://redbits.xyz/login",
    "https://torrentseeds.org/buyinvite",
    "https://pretome.info/index.php?page=home&msg=not_qualified",
]

async def fetch_trackers():
    async with aiohttp.ClientSession() as session:
        async with session.get("https://raw.githubusercontent.com/NDDDDDDDDD/TrackerChecker/main/trackers.json") as response:
            trackers = await response.text()
        ### IF YOU WANT LOCALHOST
        # with open('trackers.json', 'r') as f:
        #     trackers = f.read()
            # print(trackers)
    return json.loads(trackers)

async def gather_with_concurrency(n, urls):
    conn = aiohttp.TCPConnector(limit_per_host=20, limit=100)
    timeout = aiohttp.ClientTimeout(total=30)
    semaphore = asyncio.Semaphore(n)
    async with aiohttp.ClientSession(connector=conn, timeout=timeout) as session:
        print("Starting...")
        tasks = [get(url.get("url"), url.get("name"), url.get("search_term"), semaphore, session) for url in urls]
        results = await asyncio.gather(*tasks, return_exceptions=True)
        return results

async def get(url, name, search_term, semaphore, session):
    temp_down = []
    down = []
    closed_trackers = []
    # print(url, search_term)
    async with semaphore:
        try:
            async with session.get(url, ssl=False) as response:
                
                try:
                    obj = await response.read()
                    obj = obj.decode("utf8")
                except:
                    obj = await response.read()
                # if name == "hebits":
                #     print(obj)
                for error in error_msg:
                    if error in str(obj):
                        temp_down.append(name)
                if response.status >= 500 or name in temp_down:
                    down.append(name)
                elif search_term in str(obj):
                    closed_trackers.append(name)
                elif str(response.url) in closed_url_msg:
                    closed_trackers.append(name)
                else:
                    print(f"{name} is open! {response.url}")
        except Exception as error:
            down.append(name)
            print(f"Error for {name}: {str(error)}")
    return down, closed_trackers

def print_results(results):
    down = []
    closed = []
    for result in results:
        if isinstance(result, Exception):
            print(f"Error: {str(result)}")
        else:
            down.extend(result[0])
            closed.extend(result[1])
    print("\nCurrently down: ", ", ".join(sorted(down)))
    print("\nCurrently closed: ", ", ".join(sorted(closed)))

if __name__ == "__main__":
    trackers = asyncio.run(fetch_trackers())
    results = asyncio.run(gather_with_concurrency(len(trackers), trackers))
    print_results(results)
    input("Done! Press enter to exit ")
