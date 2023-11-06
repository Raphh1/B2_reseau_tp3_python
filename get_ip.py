from psutil import net_if_addrs

print(net_if_addrs()['Wi-Fi'][1][1])
