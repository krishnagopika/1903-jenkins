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
                sh 'sudo docker build . -t app'
                sh 'sudo docker run -p -d 8000:8000 app' 
            }
        }
    }
}