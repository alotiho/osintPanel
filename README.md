# OSINT Panel

Open-source panel for aggregating **publicly available** OSINT data: domain WHOIS, IP geolocation, basic email checks, and SSL certificate info.

⚠️ **Scope of use.** This tool only works with publicly accessible technical data (domains, IPs, DNS, certificates). It is not intended and must not be used for searching leaked databases, deanonymizing individuals, collecting personal data without consent, or any activity that violates privacy or data protection laws.

## Features

- **WHOIS** — registrar, creation/expiration dates, name servers, status
- **IP Geolocation** — country, city, ISP via a public API (ipinfo.io)
- **Email check** — format validation and domain MX record lookup
- **SSL info** — issuer, validity period, and SAN of a site's certificate

## Project Structure

```
osint-panel/
├── app/
│   ├── __init__.py        # app factory
│   ├── config.py          # configuration
│   ├── routes.py          # routes / API
│   ├── modules/           # OSINT module logic
│   │   ├── whois_lookup.py
│   │   ├── ip_geolocation.py
│   │   ├── email_check.py
│   │   └── ssl_info.py
│   ├── templates/
│   │   └── index.html
│   └── static/
│       ├── style.css
│       └── app.js
├── dist/
│   └── osint-panel-ui.exe # desktop UI build (Windows)
├── tests/
│   └── test_email_check.py
├── run.py
├── requirements.txt
├── .env.example
└── README.md
```

## Desktop UI (.exe)

In addition to running it in a browser, a ready-to-use desktop build is available for Windows:

📥 [`dist/osint-panel-ui.exe`](./dist/osint-panel-ui.exe)

Download and run it — the app will spin up a local server and open the panel's interface in its own window, no need to manually run `python run.py` and open a browser.

> The file currently in `dist/` is a placeholder — it will be replaced with the actual build.

## Installation

```bash
git clone <repo-url>
cd osint-panel
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
```

Fill in `.env` if needed (an ipinfo.io token raises your request rate limit).

## Running

```bash
python run.py
```

The panel will be available at `http://localhost:5000`.

## API

All endpoints accept `POST` requests with a JSON body and return JSON.

| Endpoint      | Parameter  | Description                        |
|---------------|------------|-------------------------------------|
| `/api/whois`  | `domain`   | WHOIS data for a domain             |
| `/api/ip`     | `ip`       | Geolocation for an IP address       |
| `/api/email`  | `email`    | Format and MX record check          |
| `/api/ssl`    | `hostname` | SSL certificate information         |

Example request:

```bash
curl -X POST http://localhost:5000/api/whois \
  -H "Content-Type: application/json" \
  -d '{"domain": "example.com"}'
```

## Tests

```bash
pip install pytest
pytest tests/
```

## Extending

To add a new module:

1. Create a file in `app/modules/` implementing a function that returns a `dict`
2. Add a route in `app/routes.py`
3. Add a card to `app/templates/index.html` and a call in `app/static/app.js`

Planned extensions: Shodan integration (service banners by IP), breach checks via public aggregate services with a transparent consent flow, PDF/CSV report export.

## License

MIT — use and modify at your own risk, in compliance with the data protection and computer security laws of your jurisdiction.
