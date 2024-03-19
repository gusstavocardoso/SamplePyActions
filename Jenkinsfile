pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Setup Python') {
            steps {
                bat 'choco install python3 -y'
                bat 'python -m venv venv'
                bat 'venv\\Scripts\\activate'
            }
        }
        stage('Instalar Dependencias') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Executar Testes') {
            steps {
                sh 'pytest'
            }
        }
    }
}
