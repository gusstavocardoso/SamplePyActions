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
