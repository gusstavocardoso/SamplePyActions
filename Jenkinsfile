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
                bat 'winget install Python --silent'
            }
        }
        stage('Instalar Dependencias') {
            steps {
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
