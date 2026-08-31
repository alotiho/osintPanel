"""
Модуль получения информации о SSL-сертификате домена.
Полезен для базового технического OSINT (проверка инфраструктуры сайта).
"""
import ssl
import socket
from datetime import datetime


def get_ssl_info(hostname: str, port: int = 443) -> dict:
    try:
        ctx = ssl.create_default_context()
        with socket.create_connection((hostname, port), timeout=5) as sock:
            with ctx.wrap_socket(sock, server_hostname=hostname) as ssock:
                cert = ssock.getpeercert()

        return {
            "hostname": hostname,
            "issuer": dict(x[0] for x in cert.get("issuer", [])),
            "subject": dict(x[0] for x in cert.get("subject", [])),
            "valid_from": cert.get("notBefore"),
            "valid_until": cert.get("notAfter"),
            "san": cert.get("subjectAltName"),
        }
    except Exception as e:
        return {"hostname": hostname, "error": str(e)}
