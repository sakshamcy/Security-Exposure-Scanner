from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Import your modules
from modules.subdomain_scanner import find_subdomains
from modules.port_scanner import scan_ports
from modules.ssl_checker import check_ssl
from modules.risk_engine import calculate_risk
from modules.email_scanner import scan_emails


app = Flask(__name__)

# -----------------------------
# DATABASE CONFIGURATION
# -----------------------------
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


# -----------------------------
# DATABASE MODELS
# -----------------------------
class Target(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    domain = db.Column(db.String(200), nullable=False)
    scan_date = db.Column(db.DateTime, default=datetime.utcnow)


class ScanResult(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    target_id = db.Column(db.Integer, db.ForeignKey("target.id"))
    subdomains = db.Column(db.Text)
    open_ports = db.Column(db.Text)
    ssl_status = db.Column(db.String(200))


# Create tables
with app.app_context():
    db.create_all()


# -----------------------------
# MAIN ROUTE
# -----------------------------
@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "POST":

        domain = request.form.get("domain")
        email = request.form.get("email")

        # Run scanners
        subdomains = find_subdomains(domain)
        ports = scan_ports(domain)
        ssl_status = check_ssl(domain)
        email_result = scan_emails(domain)
        risk_level = calculate_risk(ports, ssl_status)

        # Save target to DB
        target = Target(domain=domain)
        db.session.add(target)
        db.session.commit()

        # Save scan results
        result = ScanResult(
            target_id=target.id,
            subdomains=str(subdomains),
            open_ports=str(ports),
            ssl_status=ssl_status
        )
        db.session.add(result)
        db.session.commit()

        return render_template(
            "dashboard.html",
            domain=domain,
            subdomains=subdomains,
            ports=ports,
            ssl=ssl_status,
            risk=risk_level,
            emails=email_result,
                      
        )

    return render_template("index.html")


# -----------------------------
# RUN SERVER
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)
