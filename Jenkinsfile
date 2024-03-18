pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Setup Env') {
            steps {
                bat 'python -m venv venv'
               
                bat '. venv/bin/activate'
                
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
