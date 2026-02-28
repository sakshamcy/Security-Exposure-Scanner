from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Target(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    domain = db.Column(db.String(100), nullable=False)
    risk_score = db.Column(db.Integer, default=0)
    scan_date = db.Column(db.DateTime, default=datetime.utcnow)

class ScanResult(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    target_id = db.Column(db.Integer, nullable=False)
    subdomains = db.Column(db.Text)
    open_ports = db.Column(db.Text)
    ssl_status = db.Column(db.String(200))
