tg_token = "743010073:AAECohlhDgxV2MNNku2Uy5Ve9ZgA8RetBgA"

proxy = True
proxy_type = (True)*"socks5" + (False)*("http")
proxy_url = "790926.fckrknbot.club"
proxy_port = "443"

proxy_login = "user_727838040"
proxy_pswd = "f5UtVtp5otLU"

from aiosocksy import Socks5Auth
from aiohttp import BasicAuth

proxy = f"{proxy_type}://{proxy_url}:{proxy_port}" if proxy else None
proxy_auth = Socks5Auth(proxy_login, proxy_pswd) if proxy_type == "socks5" else None
