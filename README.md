# 🧮 Scientific Calculator with DevOps Pipeline

> A command-line Scientific Calculator built with Python, delivered through a complete DevOps pipeline including CI/CD, containerization, and automated deployment.

---

## 📋 Table of Contents
- [About the Application](#about-the-application)
- [Calculator Operations](#calculator-operations)
- [DevOps Pipeline](#devops-pipeline)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Running Tests](#running-tests)
- [Docker](#docker)
- [Jenkins Pipeline](#jenkins-pipeline)
- [Ansible Deployment](#ansible-deployment)
- [Links](#links)

---

## 📌 About the Application

A menu-driven command-line calculator built in Python supporting four mathematical operations. Every operation is logged to `calculator.log` for monitoring purposes.

**Built with:** Python 3.12  
**Course:** CS 816 - Software Production Engineering  

---

## 🔢 Calculator Operations

| Operation | Symbol | Example | Result |
|-----------|--------|---------|--------|
| Square Root | √x | √25 | 5.0 |
| Factorial | x! | 5! | 120 |
| Natural Logarithm | ln(x) | ln(10) | 2.302 |
| Power | x^b | 2^8 | 256.0 |

---

## ⚙️ DevOps Pipeline

Every push to GitHub automatically triggers the full pipeline:

```
Push to GitHub
      ↓
GitHub Webhook → ngrok → Jenkins
      ↓
✅ Pull latest code
✅ Run 19 unit tests (PyUnit)
✅ Build Docker image
✅ Push to Docker Hub
✅ Deploy with Ansible
✅ Send email notification
```

### Tools Used

| Stage | Tool | Alternative |
|-------|------|-------------|
| Source Control | GitHub | GitLab, BitBucket |
| Testing | PyUnit | pytest, JUnit |
| CI/CD | Jenkins | GitHub Actions, GitLab CI |
| Containerization | Docker | Podman |
| Image Registry | Docker Hub | Amazon ECR, GitHub Registry |
| Deployment | Ansible | Chef, Puppet, Rundeck |
| Tunnel | ngrok | Cloudflare Tunnel |
| Notifications | Gmail SMTP | Slack, SendGrid |

---

## 📁 Project Structure

```
scientific-calculator/
├── calculator.py          # Main application with 4 operations
├── test_calculator.py     # 19 unit tests covering all functions
├── Dockerfile             # Container build instructions
├── Jenkinsfile            # CI/CD pipeline definition
└── ansible/
    ├── inventory.ini      # Target machines (localhost)
    └── playbook.yml       # Deployment instructions
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.12+
- Docker Desktop
- Git

### Run the Calculator Locally

```bash
# Clone the repository
git clone https://github.com/VINNIESINGHSISODIA/scientific-calculator.git

# Navigate to project folder
cd scientific-calculator

# Run the calculator
python3 calculator.py
```

You will see:
```
=============================
    Scientific Calculator    
=============================
1. Square Root  √x
2. Factorial    x!
3. Natural Log  ln(x)
4. Power        x^b
5. Exit
=============================
Enter your choice (1-5):
```

---

## 🧪 Running Tests

```bash
# Run all 19 unit tests with verbose output
python3 -m unittest test_calculator.py -v
```

Expected output:
```
test_factorial_normal ... ok
test_factorial_zero ... ok
test_natural_log_of_e ... ok
test_square_root_positive ... ok
...
----------------------------------------------------------------------
Ran 19 tests in 0.004s
OK
```

### Test Coverage

| Function | Normal | Edge Case | Invalid Input |
|----------|--------|-----------|---------------|
| square_root | ✅ | ✅ | ✅ |
| factorial | ✅ | ✅ | ✅ |
| natural_log | ✅ | ✅ | ✅ |
| power | ✅ | ✅ | ✅ |

---

## 🐳 Docker

### Build Image Locally

```bash
# Build the Docker image
docker build -t scientific-calculator .

# Run the container interactively
docker run -it scientific-calculator

# Pull from Docker Hub
docker pull vinnie9999/scientific-calculator:latest

# Run from Docker Hub image
docker run -it vinnie9999/scientific-calculator:latest
```

### Docker Image Details

| Detail | Value |
|--------|-------|
| Base Image | python:3.12-slim |
| Image Size | ~180MB |
| Docker Hub | vinnie9999/scientific-calculator |
| Tag | latest |

---

## 🔧 Jenkins Pipeline

Jenkins automates the entire pipeline on every GitHub push.

### Pipeline Stages

```
Declarative: Checkout SCM  →  1s   ✅
Checkout                   →  1s   ✅
Test (19 PyUnit tests)     →  700ms ✅
Build Docker Image         →  6s   ✅
Push to Docker Hub         →  19s  ✅
Deploy with Ansible        →  15s  ✅
Post Actions (Email)       →  1s   ✅
─────────────────────────────────────
Total pipeline time:       ~35 seconds
```

### Jenkins Setup

```bash
# Run Jenkins using WAR file
java -jar jenkins.war

# Access Jenkins at
http://localhost:8080

# Expose Jenkins to internet for GitHub webhooks
ngrok http 8080
```

### Plugins Required
- GitHub Integration Plugin
- Email Extension Plugin

---

## 📦 Ansible Deployment

Ansible automatically pulls the latest Docker image and runs the container after every successful Jenkins build.

```bash
# Install Ansible (WSL/Ubuntu)
sudo apt-get install -y ansible

# Run playbook manually
ansible-playbook -i ansible/inventory.ini ansible/playbook.yml
```

### Playbook Tasks

```
TASK [Pull latest Docker image]     → changed
TASK [Stop existing container]      → changed/ignored
TASK [Remove existing container]    → changed/ignored
TASK [Run new container]            → changed
─────────────────────────────────────────────────
PLAY RECAP: ok=9, failed=0
```

---

## 📊 Logging

Every calculator operation is automatically logged to `calculator.log`:

```
2024-02-28 14:30:00 - INFO - Calculator application started
2024-02-28 14:30:05 - INFO - square_root(25) = 5.0
2024-02-28 14:30:10 - INFO - factorial(5) = 120
2024-02-28 14:30:15 - INFO - natural_log(10) = 2.302585
2024-02-28 14:30:20 - INFO - power(2, 8) = 256.0
```

---

## 🔗 Links

| Resource | URL |
|----------|-----|
| GitHub Repository | https://github.com/VINNIESINGHSISODIA/scientific-calculator |
| Docker Hub Image | https://hub.docker.com/r/vinnie9999/scientific-calculator |

---

## 👤 Author

**Vinnie Singh Sisodia**  
CS 816 - Software Production Engineering

---

## 📄 License

This project is for educational purposes as part of CS 816 Mini Project.