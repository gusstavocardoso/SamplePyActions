pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Instalar Dependencias') {
            steps {
                bat 'python -m venv venv'
                // bat 'venv\\Scripts\\activate'
                bat 'pip install -r requirements.txt'
            }
        }
        stage('Executar Testes') {
            steps {
                bat 'pytest'
            }
        }
    }
}
