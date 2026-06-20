# 🚀 End-to-End CI/CD Pipeline with Docker

[![CI/CD Pipeline](https://github.com/Hacker3S/cicd-docker-pipeline/actions/workflows/ci-cd.yml/badge.svg)](https://github.com/Hacker3S/cicd-docker-pipeline/actions/workflows/ci-cd.yml)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=flat&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green.svg)

A fully automated CI/CD pipeline that tests, builds, containerizes, and deploys a Python Flask application on every push to `main` — built entirely with free tools.

---

## 📐 Architecture

```
Developer pushes code
        │
        ▼
   GitHub Repository
        │
        ▼
   GitHub Actions triggered
        │
        ▼
   ┌─────────────┐
   │  Run Tests  │  (pytest)
   └─────────────┘
        │
        ▼
   ┌──────────────────┐
   │ Build Docker      │
   │ Image             │
   └──────────────────┘
        │
        ▼
   ┌──────────────────┐
   │ Push Image to     │
   │ Docker Hub        │
   └──────────────────┘
        │
        ▼
   ┌──────────────────┐
   │ Deploy            │
   │ (pull + smoke test)│
   └──────────────────┘
```

Every stage runs automatically inside GitHub Actions — no manual steps after `git push`.

---

## 🧰 Tech Stack

| Layer            | Tool                          |
|-------------------|--------------------------------|
| Application       | Python 3.11, Flask             |
| Testing           | Pytest                         |
| Containerization  | Docker                         |
| CI/CD             | GitHub Actions                 |
| Image Registry    | Docker Hub                     |
| Version Control   | Git & GitHub                   |

---

## 📁 Project Structure

```
cicd-docker-pipeline/
├── .github/
│   └── workflows/
│       └── ci-cd.yml      # GitHub Actions pipeline definition
├── app.py                  # Flask application
├── test_app.py             # Pytest test suite
├── requirements.txt        # Python dependencies
├── Dockerfile              # Container build instructions
├── .dockerignore
├── .gitignore
└── README.md
```

---

## ⚙️ How the Pipeline Works

The pipeline is defined in [`.github/workflows/ci-cd.yml`](.github/workflows/ci-cd.yml) and runs as three sequential jobs:

1. **`test`** — Installs dependencies and runs the Pytest suite. If a single test fails, the pipeline stops here and nothing gets built or deployed.
2. **`build-and-push`** — Only runs if tests pass and the push is to `main`. Builds the Docker image and pushes it to Docker Hub, tagged with both `latest` and the Git commit SHA (for traceability).
3. **`deploy`** — Pulls the image that was just pushed, runs it as a container, waits for it to boot, then hits the `/health` endpoint to confirm the deployment actually works (a "smoke test"). The container is torn down afterward to keep the runner clean.

This mirrors how real production pipelines work: **test → build → push → verify deployment**, with each stage gated on the previous one succeeding.

---

## 🖥️ Running Locally (without Docker)

```bash
# Clone the repo
git clone https://github.com/Hacker3S/cicd-docker-pipeline.git
cd cicd-docker-pipeline

# Create a virtual environment
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
```

Visit `http://localhost:5000` in your browser.

---

## 🧪 Running Tests

```bash
pytest -v
```

---

## 🐳 Running with Docker

```bash
# Build the image
docker build -t cicd-docker-pipeline .

# Run the container
docker run -d -p 5000:5000 --name cicd-app cicd-docker-pipeline

# Check it's alive
curl http://localhost:5000/health

# Stop and remove when done
docker stop cicd-app && docker rm cicd-app
```

---

## 🔑 Setting Up the Pipeline Yourself

1. Fork or clone this repo.
2. Create a [Docker Hub](https://hub.docker.com) account and generate an **Access Token** (Account Settings → Security → New Access Token).
3. In your GitHub repo, go to **Settings → Secrets and variables → Actions** and add:
   - `DOCKERHUB_USERNAME` — your Docker Hub username
   - `DOCKERHUB_TOKEN` — the access token you generated
4. Push to `main`. Go to the **Actions** tab and watch the pipeline run.
5. Check your Docker Hub repository — the new image will appear automatically.

---

## 📡 API Endpoints

| Endpoint        | Method | Description                          |
|------------------|--------|---------------------------------------|
| `/`              | GET    | Basic landing response                |
| `/health`        | GET    | Health check (used by the deploy job) |
| `/api/info`      | GET    | App metadata                          |

---

## 💡 What This Project Demonstrates

- Writing automated tests that gate deployment
- Multi-stage GitHub Actions workflows with job dependencies (`needs:`)
- Building and tagging Docker images for traceability
- Securely handling credentials using GitHub Secrets
- Post-deployment verification (smoke testing) — not just "it built," but "it actually works"

---

## 🚀 Possible Extensions

- Deploy to a real cloud target (Render, EC2, or a VPS) instead of the in-runner smoke test
- Add a staging vs. production environment split
- Push images to GitHub Container Registry (GHCR) instead of Docker Hub
- Add code coverage reporting and linting (`flake8`/`black`) as an extra pipeline stage

---

## 👤 Author

**Shawn Sreeju Sampath**
[GitHub](https://github.com/Hacker3S) · [LinkedIn](https://linkedin.com/in/shawn-sreeju-sampath-074923377)

---

## 📄 License

This project is licensed under the MIT License.
