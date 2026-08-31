"""
Модуль базовой проверки email-адреса:
- валидность формата
- наличие MX-записей у домена
Не выполняет поиск по слитым базам данных и не деанонимизирует владельца.
"""
import re
import dns.resolver

EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


def check_email(email: str) -> dict:
    result = {"email": email, "valid_format": bool(EMAIL_RE.match(email))}

    if not result["valid_format"]:
        return result

    domain = email.split("@")[1]
    try:
        answers = dns.resolver.resolve(domain, "MX")
        result["mx_records"] = [str(r.exchange) for r in answers]
        result["has_mx"] = True
    except Exception as e:
        result["has_mx"] = False
        result["mx_error"] = str(e)

    return result
