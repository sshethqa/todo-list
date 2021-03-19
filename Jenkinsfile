pipeline {
    agent any
    stages {
        stage('Install Dependencies') {
            steps {
                sh "python3 -m venv venv"
                sh "source venv/bin/activate"   
                sh "pip install -r requirements.txt"
                sh "pip install pytest pytest-cov"
            }
        }
        stage('Test') {
            steps {
                //
                sh "echo test here!"
            }
        }
        stage('Deploy') {
            steps {
                //
                sh "echo deployment here!"
            }
        }
    }
}
