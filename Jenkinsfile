pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "vinnie9999/scientific-calculator"
        DOCKER_TAG = "latest"
        EMAIL_RECIPIENT = "vinniesinghsisodia@gmail.com"
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
            echo 'Pipeline completed successfully!'
            emailext(
                to: "${EMAIL_RECIPIENT}",
                subject: "BUILD SUCCESS - Scientific Calculator #${BUILD_NUMBER}",
                body: """
                    <html>
                    <body>
                        <h2 style="color:green;">Build Successful!</h2>
                        <p><b>Project:</b> Scientific Calculator</p>
                        <p><b>Build Number:</b> #${BUILD_NUMBER}</p>
                        <p><b>Status:</b> SUCCESS</p>
                        <p><b>Docker Image:</b> vinnie9999/scientific-calculator:latest</p>
                        <p><b>All Stages Passed:</b></p>
                        <ul>
                            <li>Checkout</li>
                            <li>Unit Tests (19 tests passed)</li>
                            <li>Docker Image Built</li>
                            <li>Pushed to Docker Hub</li>
                            <li>Deployed with Ansible</li>
                        </ul>
                        <p>Check details at: <a href="${BUILD_URL}">${BUILD_URL}</a></p>
                    </body>
                    </html>
                """,
                mimeType: 'text/html'
            )
        }

        failure {
            echo 'Pipeline failed!'
            emailext(
                to: "${EMAIL_RECIPIENT}",
                subject: "BUILD FAILED - Scientific Calculator #${BUILD_NUMBER}",
                body: """
                    <html>
                    <body>
                        <h2 style="color:red;">Build Failed!</h2>
                        <p><b>Project:</b> Scientific Calculator</p>
                        <p><b>Build Number:</b> #${BUILD_NUMBER}</p>
                        <p><b>Status:</b> FAILED</p>
                        <p>Please check the console output for errors:</p>
                        <p><a href="${BUILD_URL}console">${BUILD_URL}console</a></p>
                    </body>
                    </html>
                """,
                mimeType: 'text/html'
            )
        }

        always {
            bat "docker rmi ${DOCKER_IMAGE}:${DOCKER_TAG} || exit 0"
        }
    }
}