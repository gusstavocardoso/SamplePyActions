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
                sh 'choco install python3 -y'
                sh 'python -m venv venv'
                sh '. venv/bin/activate'
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
