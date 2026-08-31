"""
Модуль получения публичной WHOIS-информации о домене.
Использует библиотеку python-whois поверх стандартного протокола WHOIS.
"""
import whois


def lookup_domain(domain: str) -> dict:
    """
    Возвращает публичные WHOIS-данные о домене:
    регистратор, даты создания/истечения, NS-серверы и т.д.
    """
    try:
        data = whois.whois(domain)
        return {
            "domain": domain,
            "registrar": data.get("registrar"),
            "creation_date": _stringify(data.get("creation_date")),
            "expiration_date": _stringify(data.get("expiration_date")),
            "name_servers": data.get("name_servers"),
            "status": data.get("status"),
            "org": data.get("org"),
            "country": data.get("country"),
        }
    except Exception as e:
        return {"domain": domain, "error": str(e)}


def _stringify(value):
    if isinstance(value, list):
        return [str(v) for v in value]
    if value is None:
        return None
    return str(value)
