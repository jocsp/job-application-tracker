"""Initial Flask application for the Job Application Tracker."""

from flask import Flask, jsonify

from database import fetch_one


app = Flask(__name__)


@app.get("/")
def home():
    """Return a basic response while the application is being built."""
    return jsonify({
        "application": "Job Application Tracker",
        "status": "running",
    })


@app.get("/health/database")
def database_health():
    """Check that Flask can run a simple query against MySQL."""
    try:
        result = fetch_one("SELECT 1 AS connected")
        if result and result["connected"] == 1:
            return jsonify({"database": "connected"}), 200
    except Exception as error:
        # Avoid returning connection details or credentials to the client.
        app.logger.error("Database health check failed (%s).", type(error).__name__)

    return jsonify({"database": "unavailable"}), 503


if __name__ == "__main__":
    app.run(debug=True)
