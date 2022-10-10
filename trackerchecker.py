import asyncio
import aiohttp

URLS = [
    {
        "name": "BeyondHD",
        "url": "https://beyond-hd.me/register/",
        "search_term": "You Must Be Invited To",
    },
    {
        "name": "RED-BITS",
        "url": "https://red-bits.com/register/null",
        "search_term": "Has sido devuelto",
    },
    {
        "name": "AsianCinema",
        "url": "https://asiancinema.me/register/null",
        "search_term": "ust have an invitation link to regist",
    },
    {
        "name": "CinemaZ",
        "url": "https://cinemaz.to/auth/register",
        "search_term": "We sometimes open registration or application. ",
    },
    {
        "name": "PrivateHD",
        "url": "https://privatehd.to/auth/register",
        "search_term": "PrivateHD is Invite Only",
    },
    {
        "name": "eShareNet",
        "url": "https://esharenet.eu/register/null",
        "search_term": "pen Registration is Clos",
    },
    {
        "name": "Aither",
        "url": "https://aither.cc/register/null",
        "search_term": "Open Registration is Closed!",
    },
    #{
    #    "name": "The Horror Charnel",
    #    "url": "https://horrorcharnel.org/signup.php",
    #    "search_term": "The site has been set to invite only by the staff<",
    #},
    {
        "name": "AvistaZ",
        "url": "https://avistaz.to/auth/register",
        "search_term": "AvistaZ is Invite Only",
    },
    {
        "name": "JPTV.CLUB",
        "url": "https://jptv.club/register/null",
        "search_term": "Open registration is closed",
    },
    {
        "name": "RetroFlix",
        "url": "https://retroflix.club/signup.php",
        "search_term": "Open registration is currently disabled",
    },
    {
        "name": "BwTorrents",
        "url": "https://bwtorrents.tv/signup.php",
        "search_term": "The current users account limit has been reached.",
    },
    {
        "name": "hawke-uno",
        "url": "https://www.hawke.uno/register/null",
        "search_term": "en Registration is Closed",
    },
    {
        "name": "HD-Olimpo",
        "url": "https://hd-olimpo.club/register/null",
        "search_term": "Registro libre cerrado. Se necesit",
    },
    {
        "name": "Torrentland",
        "url": "https://torrentland.li/register/null",
        "search_term": "Registro libre cerrado",
    },
    {
        "name": "R3V WTF!",
        "url": "https://r3vuk.wtf/signup.php",
        "search_term": "Signups are closed presently",
    },
    {
        "name": "DanishBytes",
        "url": "https://danishbytes.club/register/null",
        "search_term": "Du skal have et invitationslink",
    },
    {
        "name": "TellyTorrent",
        "url": "https://telly.wtf/register/null",
        "search_term": "pen Registration is Closed",
    },
    {
        "name": "ReelFLiX",
        "url": "https://reelflix.xyz/register/null",
        "search_term": "Open Registration is Closed",
    },
    {
        "name": "SkipTheTrailers",
        "url": "https://skipthetrailers.xyz/register/null",
        "search_term": "Open Registration is Closed",
    },
    {
        "name": "Red Star Torrent",
        "url": "http://rstorrent.org.pl/signup.php",
        "search_term": "Nieaktywne konta s",
    },
    {
        "name": "Generation-Free",
        "url": "https://generation-free.org/register/null",
        "search_term": "https://generation-free.org/login",
    },
    {
        "name": "Peeratiko",
        "url": "https://peeratiko.org/signup.php",
        "search_term": "ignups are closed pres",
    },
    {
        "name": "TheScenePlace",
        "url": "https://www.thesceneplace.com/index.php?page=account",
        "search_term": "ry, but registrations are closed",
    },
    {
        "name": "HDMonkey",
        "url": "https://hdmonkey.org/account-signup.php",
        "search_term": "orry this site has disabled user registration",
    },
    {
        "name": "TorrentSeeds",
        "url": "https://torrentseeds.org/buyinvite",
        "search_term": "https://torrentseeds.org/buyinvite",
    },
    {
        "name": "Tophos",
        "url": "https://tophos.org/signup.php",
        "search_term": "Signups are closed presently",
    },
    {
        "name": "HD-F",
        "url": "https://hdf.world/register.php",
        "search_term": "ctuellement sur invitation se",
    },
    {
        "name": "AlphaRatio",
        "url": "https://alpharatio.cc/register.php",
        "search_term": "e site is currently invite",
    },
    {
        "name": "ExoticaZ",
        "url": "https://exoticaz.to/register",
        "search_term": "metimes open registration or applic",
    },
    {
        "name": "Abnormal",
        "url": "https://abn.lol/Home/Register",
        "search_term": "pour le momen",
    },
    {
        "name": "dream-torrents",
        "url": "http://dream-torrents.com/signup.php",
        "search_term": "gistration is currently disabl",
    },
]

conn = aiohttp.TCPConnector(limit_per_host=10, limit=10, ttl_dns_cache=300)
PARALLEL_REQUESTS = len(URLS)


async def gather_with_concurrency(n):
    timeout = aiohttp.ClientTimeout(total=30)
    semaphore = asyncio.Semaphore(n)
    session = aiohttp.ClientSession(connector=conn, timeout=timeout)

    async def get(url, name, search_term):
        async with semaphore:
            try:
                async with session.get(url, ssl=False) as response:
                    obj = await response.read()
                    status_code = response.status
                    if status_code > 500:
                        print(f"{name} is down!")
                    if search_term in str(obj):
                        print(f"{name} is not open")
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
