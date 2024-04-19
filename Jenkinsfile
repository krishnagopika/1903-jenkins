pipeline {
    agent any 
    stages {
        stage('checkout') {
                steps {
                git branch: 'main',
                url: 'https://github.com/krishnagopika/1903-jenkins.git'
                }
        }
        stage('Build') {
            steps {
                sh 'docker build -t krishnagopika4/demo-cicd-1903'
            }
        }
    }
}
