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
                sh "bash test.sh"
            }
        }
        stage('Deploy') {
            steps {
                //
                sh "bash deploy.sh"
            }
        }
    }
}
