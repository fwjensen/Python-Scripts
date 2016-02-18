import re

ip = re.findall('[0-9]{1,3}','192.168.0.1 255.255.255.0')

print(ip);
