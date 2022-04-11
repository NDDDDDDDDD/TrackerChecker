from bs4 import BeautifulSoup
import requests

BeyondHD = "https://beyond-hd.me/register/"
r = requests.get(BeyondHD)
urll = r.text
if "n Page!','Whoops!');" in urll:
    print("BeyondHD is not open")
else:
    print(f"BeyondHD is open! {r.url}")
red_bits = "https://red-bits.com/register/null"
r = requests.get(red_bits)
urll = r.text
if "ar. Has sido devuelto a la página inicial.'" in urll:
    print("RED-BITS is not open")
else:
    print(f"RED-BITS is open! {r.url}")
asiancinema = "https://asiancinema.me/register/null"
r = requests.get(asiancinema)
urll = r.text
if "Open Registration is Closed!" in urll:
    print("AsianCinema is not open")
else:
    print(f"AsianCinema is open! {r.url}")
CinemaZ = "https://cinemaz.to/auth/register"
r = requests.get(CinemaZ)
urll = r.text
if "We sometimes open registration or application. " in urll:
    print("CinemaZ is not open")
else:
    print(f"CinemaZ is open! {r.url}")
HD_Space = "https://hd-space.org/index.php?page=signup"
r = requests.get(HD_Space)
urll = r.text
if "Sorry, but registrations are closed." in urll:
    print("HD-Space is not open")
else:
    print(f"HD-Space is open! {r.url}")
PrivateHD = "https://privatehd.to/auth/register"
r = requests.get(PrivateHD)
urll = r.text
if "PrivateHD is Invite Only" in urll:
    print("PrivateHD is not open")
else:
    print(f"PrivateHD is open! {r.url}")
Torrentland = "https://torrentland.li/register/null"
r = requests.get(Torrentland)
urll = r.text
if "Registro libre cerrado." in urll:
    print("Torrentland is not open")
else:
    print(f"Torrentland is open! {r.url}")
eShareNet = "https://esharenet.eu/register/null"
r = requests.get(eShareNet)
urll = r.text
if "pen Registration is Clos" in urll:
    print("eShareNet is not open")
else:
    print(f"eShareNet is open! {r.url}")
Abnormal = "https://abn.lol/Home/Register"
r = requests.get(Abnormal)
urll = r.text
if "Les inscriptions sont fermées pour le moment." in urll:
    print("Abnormal is not open")
else:
    print(f"Abnormal is open! {r.url}")
Aither = "https://aither.cc/register/null"
r = requests.get(Aither)
urll = r.text
if "Open Registration is Closed!" in urll:
    print("Aither is not open")
else:
    print(f"Aither is open! {r.url}")
The_Horror_Charnel = "https://horrorcharnel.org/signup.php"
r = requests.get(The_Horror_Charnel)
urll = r.text
if "The site has been set to invite only by the staff<" in urll:
    print("The Horror Charnel is not open")
else:
    print(f"The Horror Charnel is open! {r.url}")
TorrentDB = "https://torrentdb.net/register/null"
r = requests.get(TorrentDB)
urll = r.text
if "Registrations are closed" in urll:
    print("TorrentDB is not open")
else:
    print(f"TorrentDB is open! {r.url}")
AvistaZ = "https://avistaz.to/auth/register"
r = requests.get(AvistaZ)
urll = r.text
if "AvistaZ is Invite Only" in urll:
    print("AvistaZ is not open")
else:
    print(f"AvistaZ is open! {r.url}")

JPTV_CLUB = "https://jptv.club/register/null"
r = requests.get(JPTV_CLUB)
urll = r.text
if "Open registration is closed" in urll:
    print("JPTV.CLUB is not open")
else:
    print(f"JPTV.CLUB is open! {r.url}")

Blutopia = "https://blutopia.xyz/application"
r = requests.get(Blutopia)
urll = r.text
if "Applications Are Closed" in urll:
    print("Blutopia is not open")
else:
    print(f"Blutopia is open! {r.url}")
RetroFlix = "https://retroflix.club/signup.php"
r = requests.get(RetroFlix)
urll = r.text
if "Open registration is currently disabled" in urll:
    print("RetroFlix is not open")
else:
    print(f"RetroFlix is open! {r.url}")
BwTorrents = "https://bwtorrents.tv/signup.php"
r = requests.get(BwTorrents)
urll = r.text
if "The current users account limit has been reached." in urll:
    print("BwTorrents is not open")
else:
    print(f"BwTorrents is open! {r.url}")
hawke_uno = "https://www.hawke.uno/register/null"
r = requests.get(hawke_uno)
urll = r.text
if "en Registration is Closed" in urll:
    print("hawke-uno is not open")
else:
    print(f"hawke-uno is open! {r.url}")
HD_Olimpo = "https://hd-olimpo.club/register/null"
r = requests.get(HD_Olimpo)
urll = r.text
if "Registro libre cerrado. Se necesit" in urll:
    print("HD-Olimpo is not open")
else:
    print(f"HD-Olimpo is open! {r.url}")
Torrentland = "https://torrentland.li/register/null"
r = requests.get(Torrentland)
urll = r.text
if "Registro libre cerrado" in urll:
    print("Torrentland is not open")
else:
    print(f"Torrentland is open! {r.url}")
R3V_WTF = "https://r3vuk.wtf/signup.php"
r = requests.get(R3V_WTF)
urll = r.text
if "Signups are closed presently" in urll:
    print("R3V WTF! is not open")
else:
    print(f"R3V WTF! is open! {r.url}")
DanishBytes = "https://danishbytes.club/register/null"
r = requests.get(DanishBytes)
urll = r.text
if "Du skal have et invitationslink" in urll:
    print("DanishBytes is not open")
else:
    print(f"DanishBytes is open! {r.url}")
TellyTorrent = "https://telly.wtf/register/null"
r = requests.get(TellyTorrent)
urll = r.text
if "pen Registration is Closed" in urll:
    print("TellyTorrent is not open")
else:
    print(f"TellyTorrent is open! {r.url}")
ReelFLiX = "https://reelflix.xyz/register/null"
r = requests.get(ReelFLiX)
urll = r.text
if "Open Registration is Closed" in urll:
    print("ReelFLiX is not open")
else:
    print(f"ReelFLiX is open! {r.url}")
SkipTheTrailers = "https://skipthetrailers.xyz/register/null"
r = requests.get(SkipTheTrailers)
urll = r.text
if "Open Registration is Closed" in urll:
    print("SkipTheTrailers is not open")
else:
    print(f"SkipTheTrailers is open! {r.url}")
Red_Star_Torrent = "http://rstorrent.org.pl/signup.php"
r = requests.get(Red_Star_Torrent)
urll = r.text
if "Nieaktywne konta s" in urll:
    print("Red Star Torrent is not open")
else:
    print(f"Red Star Torrent is open! {r.url}")
Generation_Free = "https://generation-free.org/register/null"
r = requests.get(Generation_Free)
urll = r.text
if "Open Registration is Closed" in urll:
    print("Generation-Free is not open")
else:
    print(f"Generation-Free is open! {r.url}")
HellasTZ = "https://hellastz.com/index.php?page=signup"
r = requests.get(HellasTZ)
urll = r.text
if "Sorry, but registrations are closed." in urll:
    print("HellasTZ is not open")
else:
    print(f"HellasTZ is open! {r.url}")