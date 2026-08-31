import os


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "change-me-in-production")
    DEBUG = os.environ.get("FLASK_DEBUG", "0") == "1"

    # Опциональные ключи для внешних сервисов (заполняются через .env)
    IPINFO_TOKEN = os.environ.get("IPINFO_TOKEN", "")
    SHODAN_API_KEY = os.environ.get("SHODAN_API_KEY", "")

    # Ограничение частоты запросов (запросов в минуту на IP)
    RATE_LIMIT = os.environ.get("RATE_LIMIT", "30/minute")
