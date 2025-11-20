pipeline {
    agent any

    environment {
        GIT_CREDENTIALS = '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'
        COMPOSE_PROJECT_NAME = "fastapi_project"
    }

    stages {

        stage('Clone Repository') {
            steps {
                git branch: 'main',
                    credentialsId: env.GIT_CREDENTIALS,
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
