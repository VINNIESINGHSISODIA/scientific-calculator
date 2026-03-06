# Scientific Calculator with DevOps CI/CD Pipeline

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Docker](https://img.shields.io/badge/Docker-Containerized-blue)
![Jenkins](https://img.shields.io/badge/Jenkins-CI%2FCD-red)
![Ansible](https://img.shields.io/badge/Ansible-Deployment-black)
![License](https://img.shields.io/badge/Project-Educational-green)

A menu-driven scientific calculator built in Python, delivered using a fully automated DevOps pipeline including CI/CD, containerization, automated deployment, and notifications.

Every push to GitHub automatically triggers:

- Unit testing
- Docker image build
- Docker Hub push
- Ansible deployment
- Email notification

---

# Table of Contents

- About the Application
- Calculator Operations
- DevOps Pipeline Architecture
- DevOps Tools Used
- Project Structure
- Getting Started
- Running Tests
- Docker
- Jenkins CI/CD Pipeline
- Ansible Deployment
- Logging
- Project Metrics
- Links

---

# About the Application

This project implements a command-line scientific calculator capable of performing multiple mathematical operations.

The application includes:

- Input validation
- Error handling
- Logging of operations
- Automated unit testing
- Containerized execution
- Fully automated CI/CD pipeline

Language: Python 3.12  
Course: CS 816 – Software Production Engineering

---

# Calculator Operations

| Operation | Symbol | Example | Result |
|-----------|--------|---------|--------|
| Square Root | √x | √25 | 5.0 |
| Factorial | x! | 5! | 120 |
| Natural Logarithm | ln(x) | ln(10) | 2.302 |
| Power | x^b | 2^8 | 256.0 |

---

# DevOps Pipeline Architecture

The project implements a complete DevOps pipeline from code commit to deployment.
