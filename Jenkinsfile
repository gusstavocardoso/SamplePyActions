pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Instalar Dependências') {
            steps {
                bat 'pip install --upgrade pip'
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
