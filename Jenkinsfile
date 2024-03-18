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
                sh 'python -m venv venv'
               
                sh '. venv/bin/activate'
                
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
