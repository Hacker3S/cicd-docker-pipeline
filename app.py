from flask import Flask, jsonify
from datetime import datetime, timezone

app = Flask(__name__)


@app.route('/')
def home():
    """Root endpoint - basic landing response."""
    return jsonify({
        "message": "CI/CD Docker Pipeline Demo App",
        "status": "running"
    }), 200


@app.route('/health')
def health():
    """Health check endpoint - used by the deploy job to verify the container is alive."""
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.now(timezone.utc).isoformat()
    }), 200


@app.route('/api/info')
def info():
    """App metadata endpoint."""
    return jsonify({
        "app": "cicd-docker-pipeline",
        "version": "1.0.0",
        "author": "Shawn Sreeju Sampath"
    }), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
