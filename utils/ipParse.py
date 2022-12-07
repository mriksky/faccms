import os
import ipaddress
import ipdb

# 定义基础信息
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IPDB_NAME = "ipv4.ipdb"
IPV4_DBFILE = os.path.join(BASE_DIR, IPDB_NAME)

# 解析IP为地域信息
def ip2addr(ip):
    if not ip:
        return "无"
    if ipaddress.ip_address(ip).is_private:
        return "局域网"
    elif not os.path.isfile(IPV4_DBFILE):
        return ip

    db = ipdb.City(IPV4_DBFILE)
    result = db.find_info(ip, "CN")
    address = '%s-%s-%s' % (result.country_name, result.region_name, result.city_name)
    return address