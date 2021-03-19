pipeline {
    agent any
    stages {
        stage('Install Dependencies') {
            steps {
                sh "bash install.sh"
            }
        }
        stage('Test') {
            steps {
                //
                sh "bash python3 -m pytest --cov=application --junitxml=junit.xml --cov-report=xml"
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
