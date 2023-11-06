import os
from sys import argv
from _socket import gethostbyname
from psutil import net_if_addrs


def lookup(host: str) -> str:
    return gethostbyname(host)


def ping(ip: str) -> str:
    return "UP !" if os.system(f"ping {ip} > NUL") == 0 else "DOWN !"


def ip() -> str:
    return net_if_addrs()["Wi-Fi"][1][1]


v = ""
match argv[1]:
    case "lookup":
        v = lookup(argv[2])
    case "ping":
        v = ping(argv[2])
    case "ip":
        v = ip()
    case _:
        v = f"'{argv[1]}' is not an available command. Déso."

print(v)