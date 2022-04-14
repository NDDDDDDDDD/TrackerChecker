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
PrivateHD = "https://privatehd.to/auth/register"
r = requests.get(PrivateHD)
urll = r.text
if "PrivateHD is Invite Only" in urll:
    print("PrivateHD is not open")
else:
    print(f"PrivateHD is open! {r.url}")
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
HDTime = "https://hdtime.org/signup.php"
r = requests.get(HDTime)
urll = r.text
if "自由注册当前关闭，只允许邀请注册" in urll:
    print("HDTime is not open")
else:
    print(f"HDTime is open! {r.url}")
MicroBit = "http://microbit.eu/signup.php"
r = requests.get(MicroBit)
urll = r.text
if "Az oldalon jelenleg nincs sz" in urll:
    print("MicroBit is not open")
else:
    print(f"MicroBit is open! {r.url}")
Peeratiko = "https://peeratiko.org/signup.php"
r = requests.get(Peeratiko)
urll = r.text
if "ignups are closed pres" in urll:
    print("Peeratiko is not open")
else:
    print(f"Peeratiko is open! {r.url}")
PTerClub = "https://pterclub.com/signup.php"
r = requests.get(PTerClub)
urll = r.text
if "自由注册当前关闭，只允许邀请注册" in urll:
    print("PTerClub is not open")
else:
    print(f"PTerClub is open! {r.url}")
Tapochek = "https://tapochek.net/profile.php?mode=register&agreed=true"
r = requests.get(Tapochek)
urll = r.text
if "данный момент регистрация разрешена тольк" in urll:
    print("Tapochek is not open")
else:
    print(f"Tapochek is open! {r.url}")
TheScenePlace = "https://www.thesceneplace.com/index.php?page=account"
r = requests.get(TheScenePlace)
urll = r.text
if "ry, but registrations are closed" in urll:
    print("TheScenePlace is not open")
else:
    print(f"TheScenePlace is open! {r.url}")
TOrrent_tuRK = "https://torrent-turk.de/?p=signup&pid=16"
r = requests.get(TOrrent_tuRK)
urll = r.text
if "Şu an için üye alımımız kapalıd" in urll:
    print("TOrrent-tuRK is not open")
else:
    print(f"TOrrent-tuRK is open! {r.url}")
HDMonkey = "https://hdmonkey.org/account-signup.php"
r = requests.get(HDMonkey)
urll = r.text
if "orry this site has disabled user registration" in urll:
    print("HDMonkey is not open")
else:
    print(f"HDMonkey is open! {r.url}")
ChangTrai = "https://3changtrai.com/signup.php"
r = requests.get(ChangTrai)
urll = r.text
if "Hiện tại chúng tôi đã khóa đăng ký tự do" in urll:
    print("ChangTrai is not open")
else:
    print(f"ChangTrai is open! {r.url}")
Trackeros = "https://trackeros.tk/register/null"
r = requests.get(Trackeros)
urll = r.text
if "egistro libre cerrado." in urll:
    print("Trackeros is not open")
else:
    print(f"Trackeros is open! {r.url}")
TorrentSeeds = "https://torrentseeds.org/buyinvite"
r = requests.get(TorrentSeeds)
urll = r.text
if "https://torrentseeds.org/buyinvite" in urll:
    print("TorrentSeeds is not open")
else:
    print(f"TorrentSeeds is open! {r.url}")
LemondHD = "https://lemonhd.org/signup.php"
r = requests.get(LemondHD)
urll = r.text
if "注册当前关闭，只允许邀请注册。如果你" in urll:
    print("LemondHD is not open")
else:
    print(f"LemondHD is open! {r.url}")
Ourbits = "https://ourbits.club/signup.php"
r = requests.get(Ourbits)
urll = r.text
if "注册当前关闭，只允许邀请注册。如果你" in urll:
    print("Ourbits is not open")
else:
    print(f"Ourbits is open! {r.url}")
TorrentCCF = "https://et8.org/signup.php"
r = requests.get(TorrentCCF)
urll = r.text
if "注册当前关闭，只允许邀请注册。如果你" in urll:
    print("TorrentCCF is not open")
else:
    print(f"TorrentCCF is open! {r.url}")
SoulVoice = "https://pt.soulvoice.club/signup.php"
r = requests.get(SoulVoice)
urll = r.text
if "由注册当前关闭，只允许邀请" in urll:
    print("SoulVoice is not open")
else:
    print(f"SoulVoice is open! {r.url}")
HDAtmos = "https://hdatmos.club/signup.php"
r = requests.get(HDAtmos)
urll = r.text
if "注册当前关闭，只允许邀请注册。如果你" in urll:
    print("HDAtmos is not open")
else:
    print(f"HDAtmos is open! {r.url}")
HD4FANS = "https://pt.hd4fans.org/signup.php"
r = requests.get(HD4FANS)
urll = r.text
if "自由注册当前关闭，只允许邀" in urll:
    print("HD4FANS is not open")
else:
    print(f"HD4FANS is open! {r.url}")
Tophos = "https://tophos.org/signup.php"
r = requests.get(Tophos)
urll = r.text
if "Signups are closed presently" in urll:
    print("Tophos is not open")
else:
    print(f"Tophos is open! {r.url}")
Spare_Tire = "https://www.beitai.pt/signup.php"
r = requests.get(Spare_Tire)
urll = r.text
if "自由注册当前关闭，只允许邀请注册。如果你" in urll:
    print("Spare Tire is not open")
else:
    print(f"Spare Tire is open! {r.url}")
CHDBits = "https://chdbits.co/signup.php"
r = requests.get(CHDBits)
urll = r.text
if "自由注册当前关闭，只允许邀请注册" in urll:
    print("CHDBits is not open")
else:
    print(f"CHDBits is open! {r.url}")
HD_F = "https://hdf.world/register.php"
r = requests.get(HD_F)
urll = r.text
if "ctuellement sur invitation se" in urll:
    print("HD-F is not open")
else:
    print(f"HD-F is open! {r.url}")
AlphaRatio = "https://alpharatio.cc/register.php"
r = requests.get(AlphaRatio)
urll = r.text
if "e site is currently invite" in urll:
    print("AlphaRatio is not open")
else:
    print(f"AlphaRatio is open! {r.url}")
ExoticaZ = "https://exoticaz.to/register"
r = requests.get(ExoticaZ)
urll = r.text
if "ExoticaZ is Invite On" in urll:
    print("ExoticaZ is not open")
else:
    print(f"ExoticaZ is open! {r.url}")
dream_torrents = "http://dream-torrents.com/signup.php"
r = requests.get(dream_torrents)
urll = r.text
if "gistration is currently disabl" in urll:
    print("dream-torrents is not open")
else:
    print(f"dream-torrents is open! {r.url}")
input("Press any button to exit ")
