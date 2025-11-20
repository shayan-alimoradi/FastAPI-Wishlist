pipeline {
    agent any

    environment {
        GIT_CREDENTIALS = 'github-token'
        COMPOSE_PROJECT_NAME = "fastapi_project"
    }

    stages {

        stage('Clone Repository') {
            steps {
                git branch: 'master',
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
                // Make sure env vars are available
                sh '''
                if [ -f $DOTENV ]; then
                    export $(grep -v '^#' $DOTENV | xargs)
                fi
                docker-compose -f docker-compose.yml pull
                docker-compose -f docker-compose.yml build
                docker-compose -f docker-compose.yml up -d
                '''
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
