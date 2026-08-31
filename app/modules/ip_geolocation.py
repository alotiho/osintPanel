"""
Модуль геолокации IP-адреса на основе публичного API ipinfo.io.
Возвращает только общедоступную информацию (страна/город/провайдер),
без персональных данных о конкретном человеке.
"""
import requests

IPINFO_URL = "https://ipinfo.io/{ip}/json"


def lookup_ip(ip: str, token: str = "") -> dict:
    params = {"token": token} if token else {}
    try:
        resp = requests.get(IPINFO_URL.format(ip=ip), params=params, timeout=5)
        resp.raise_for_status()
        data = resp.json()
        return {
            "ip": data.get("ip"),
            "city": data.get("city"),
            "region": data.get("region"),
            "country": data.get("country"),
            "org": data.get("org"),
            "loc": data.get("loc"),
            "timezone": data.get("timezone"),
        }
    except requests.RequestException as e:
        return {"ip": ip, "error": str(e)}
