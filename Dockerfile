# ── Stage 1: Base Image ────────────────────────────────────────────────────────
# We start from an official lightweight Python image
# "3.11-slim" means Python 3.11 on a minimal Linux (much smaller than full Ubuntu)
FROM python:3.12-slim

# ── Stage 2: Set Working Directory ────────────────────────────────────────────
# All commands from here run inside /app inside the container
WORKDIR /app

# ── Stage 3: Copy Files ────────────────────────────────────────────────────────
# Copy your calculator files from your machine INTO the container
COPY calculator.py .
COPY test_calculator.py .

# ── Stage 4: Run Tests ────────────────────────────────────────────────────────
# Run unit tests during the build process
# If any test fails, the Docker build will STOP (great safety check!)
RUN python -m unittest test_calculator.py -v

# ── Stage 5: Default Command ──────────────────────────────────────────────────
# When someone runs the container, this command launches the calculator
CMD ["python", "calculator.py"]