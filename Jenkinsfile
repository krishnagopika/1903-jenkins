pipeline {
    agent any 
    stages {
        stage('Build') { 
            steps {
                sh 'sudo docker build . -t app'
                sh 'sudo docker run -p -d 8000:8000 app' 
            }
        }
    }
}