pipeline {
    agent any

    environment {
        COMPOSE_PROJECT_NAME = "fastapi_project"
    }

    stages {

        stage('Clone Repository') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/shayan-alimoradi/FastAPI-Wishlist'
            }
        }

        stage('Stop Old Containers') {
            steps {
                sh """
                docker-compose down || true
                """
            }
        }

        stage('Build & Deploy') {
            steps {
                sh """
                docker-compose pull || true
                docker-compose build
                docker-compose up -d
                """
            }
        }
    }

    post {
        success {
            echo "🚀 Deployment completed successfully!"
        }
        failure {
            echo "❌ Deployment failed!"
        }
    }
}
