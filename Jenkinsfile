pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "vinnie9999/scientific-calculator"
        DOCKER_TAG = "latest"
    }

    stages {

        // ── Stage 1: Pull latest code from GitHub ──────────────────────────────
        stage('Checkout') {
            steps {
                echo 'Pulling latest code from GitHub...'
                checkout scm
            }
        }

        // ── Stage 2: Run Unit Tests ────────────────────────────────────────────
        stage('Test') {
            steps {
                echo 'Running unit tests with PyUnit...'
                bat 'python -m unittest test_calculator.py -v'
            }
        }

        // ── Stage 3: Build Docker Image ────────────────────────────────────────
        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image...'
                bat "docker build -t ${DOCKER_IMAGE}:${DOCKER_TAG} ."
            }
        }

        // ── Stage 4: Push to Docker Hub ────────────────────────────────────────
        stage('Push to Docker Hub') {
            steps {
                echo 'Pushing Docker image to Docker Hub...'
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-credentials',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    bat "docker login -u %DOCKER_USER% -p %DOCKER_PASS%"
                    bat "docker push ${DOCKER_IMAGE}:${DOCKER_TAG}"
                }
            }
        }
        // ── Stage 5: Deploy with Ansible ──────────────────────────────────────────
        stage('Deploy with Ansible') {
            steps {
                echo 'Deploying with Ansible...'
                bat 'wsl ansible-playbook -i ansible/inventory.ini ansible/playbook.yml'
            }
        }

    }

    post {
        success {
            echo 'Pipeline completed successfully! Image pushed to Docker Hub.'
        }
        failure {
            echo 'Pipeline failed! Check the logs above for errors.'
        }
        always {
            bat "docker rmi ${DOCKER_IMAGE}:${DOCKER_TAG} || exit 0"
        }
    }
}