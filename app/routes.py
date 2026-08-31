from flask import Blueprint, render_template, request, jsonify, current_app

from app.modules.whois_lookup import lookup_domain
from app.modules.ip_geolocation import lookup_ip
from app.modules.email_check import check_email
from app.modules.ssl_info import get_ssl_info

bp = Blueprint("main", __name__)


@bp.route("/")
def index():
    return render_template("index.html")


@bp.route("/api/whois", methods=["POST"])
def api_whois():
    domain = request.json.get("domain", "").strip()
    if not domain:
        return jsonify({"error": "domain is required"}), 400
    return jsonify(lookup_domain(domain))


@bp.route("/api/ip", methods=["POST"])
def api_ip():
    ip = request.json.get("ip", "").strip()
    if not ip:
        return jsonify({"error": "ip is required"}), 400
    token = current_app.config.get("IPINFO_TOKEN", "")
    return jsonify(lookup_ip(ip, token))


@bp.route("/api/email", methods=["POST"])
def api_email():
    email = request.json.get("email", "").strip()
    if not email:
        return jsonify({"error": "email is required"}), 400
    return jsonify(check_email(email))


@bp.route("/api/ssl", methods=["POST"])
def api_ssl():
    hostname = request.json.get("hostname", "").strip()
    if not hostname:
        return jsonify({"error": "hostname is required"}), 400
    return jsonify(get_ssl_info(hostname))
