#  Scientific Calculator — DevOps CI/CD Pipeline

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?logo=docker)
![Jenkins](https://img.shields.io/badge/Jenkins-CI%2FCD-D24939?logo=jenkins)
![Ansible](https://img.shields.io/badge/Ansible-Deployment-EE0000?logo=ansible)

A command-line Scientific Calculator application built with Python, deployed through a fully automated DevOps CI/CD pipeline using **GitHub → Jenkins → Docker → Docker Hub → Ansible**.

---

##  Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Pipeline Architecture](#pipeline-architecture)
- [Getting Started](#getting-started)
- [Running Tests](#running-tests)
- [Docker Usage](#docker-usage)
- [CI/CD Pipeline](#cicd-pipeline)
- [Links](#links)

---

## Overview

This project demonstrates a complete DevOps workflow for a Python-based Scientific Calculator. Every code push to GitHub automatically triggers a Jenkins pipeline that runs unit tests, builds a Docker image, pushes it to Docker Hub, and deploys the container using Ansible — all without any manual intervention.

---

## Features

The calculator supports the following mathematical operations:

| Operation | Symbol | Input Constraint |
|---|---|---|
| Square Root | √x | x ≥ 0 |
| Factorial | x! | x must be a non-negative integer |
| Natural Logarithm | ln(x) | x > 0 |
| Power | x^b | No restriction |

- Menu-driven command-line interface
- Input validation with descriptive error messages
- Operation logging to `calculator.log` (timestamp, operation, inputs, result)

---

## Tech Stack

| Tool | Role |
|---|---|
| **Python 3.12** | Application development |
| **PyUnit (unittest)** | Automated unit testing (19 test cases) |
| **GitHub** | Source control & webhook triggers |
| **Jenkins** | CI/CD pipeline orchestration |
| **Docker** | Containerization |
| **Docker Hub** | Container image registry |
| **Ansible** | Automated deployment |
| **ngrok** | Exposes local Jenkins to GitHub webhooks |
| **Gmail SMTP** | Pipeline email notifications |

---

## Project Structure

```
scientific-calculator/
├── calculator.py           # Main application
├── test_calculator.py      # Unit tests (19 test cases)
├── Dockerfile              # Container build instructions
├── Jenkinsfile             # CI/CD pipeline definition
└── ansible/
    ├── inventory.ini       # Target machine configuration
    └── playbook.yml        # Deployment instructions
```

---

## Pipeline Architecture

```
Developer (git push)
        │
        ▼
  GitHub Repository
        │  webhook
        ▼
   ngrok Tunnel
        │
        ▼
  Jenkins (localhost:8080)
        │
        ├── 1. Checkout Code
        ├── 2. Run PyUnit Tests (19 tests)
        ├── 3. Build Docker Image
        ├── 4. Push to Docker Hub
        ├── 5. Deploy via Ansible
        │       └── Pull image → Stop old container → Run new container
        └── 6. Send Email Notification (Success / Failure)
```

---

## Getting Started

### Prerequisites

- Python 3.12
- Docker Desktop
- Java (for Jenkins)
- Ansible (via WSL/Ubuntu)
- ngrok

### Clone the Repository

```bash
git clone https://github.com/VINNIESINGHSISODIA/scientific-calculator.git
cd scientific-calculator
```

### Run the Calculator Locally

```bash
python3 calculator.py
```

---

## Running Tests

19 unit tests are written using Python's built-in `unittest` framework, covering normal inputs, edge cases, and invalid inputs.

```bash
python3 -m unittest test_calculator.py -v
```

**Test Coverage:**

| Function | Normal Tests | Edge Cases | Invalid Input |
|---|---|---|---|
| `square_root` | sqrt(9)=3.0 | sqrt(0)=0.0 | sqrt(-1) → ValueError |
| `factorial` | factorial(5)=120 | factorial(0)=1 | factorial(-3) → ValueError |
| `natural_log` | ln(10)≈2.302 | ln(1)=0.0 | ln(0) → ValueError |
| `power` | 2^3=8.0 | 5^0=1.0 | 2^(-1)=0.5 (valid) |

---

## Docker Usage

### Build the Image

```bash
docker build -t scientific-calculator .
```

> Unit tests run automatically during the build. If any test fails, the image is not created.

### Run the Container

```bash
docker run -it scientific-calculator
```

### Pull from Docker Hub

```bash
docker pull vinnie9999/scientific-calculator:latest
```

---

## CI/CD Pipeline

The pipeline is defined in `Jenkinsfile` and contains the following stages:

| Stage | Description |
|---|---|
| **Checkout** | Pulls latest code from GitHub |
| **Test** | Runs all 19 PyUnit tests |
| **Build Docker Image** | Builds the container image |
| **Push to Docker Hub** | Pushes image to registry |
| **Deploy with Ansible** | Pulls image and runs container |
| **Email Notification** | Sends success/failure email |

### Jenkins Setup (Local)

```bash
java -jar jenkins.war
# Access at http://localhost:8080
```

### Expose Jenkins via ngrok

```bash
ngrok http 8080
# Use the generated public URL as the GitHub webhook payload URL
```

### Run Ansible Deployment Manually

```bash
ansible-playbook -i ansible/inventory.ini ansible/playbook.yml
```

---

## Links

- **GitHub Repository:** https://github.com/VINNIESINGHSISODIA/scientific-calculator
- **Docker Hub Image:** https://hub.docker.com/r/vinnie9999/scientific-calculator

---

## Author

**Vini Singh Rajput** — MT2025131   
International Institute of Information Technology, Bangalore  
