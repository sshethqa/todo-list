pipeline {
    agent any
    environment {
        DATABASE_URI = credentials("DATABASE_URI")
        SECRET_KEY = credentials("SECRET_KEY")
    }
    stages {
        stage('Install Dependencies') {
            steps {
                sh "bash jenkins/install.sh"
            }
        }
        stage('Testing') {
            steps {
                sh "bash jenkins/test.sh"
            }
        }
        stage('Deploy') {
            steps {
                sh 'bash jenkins/deploy.sh'
            }
        }
    }
    post {
        always {
            cobertura coberturaReportFile: 'coverage.xml', failNoReports: false
            junit 'junit/test-results.xml'
        }
    }
}