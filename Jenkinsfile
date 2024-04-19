pipeline {
    environment {
        IMAGE = "krishnagopika4/demo-cicd-1903"
        dockerHubCredentials = 'dockerhub'
    }
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
                script {
                dockerImage = docker.build "${IMAGE}:latest"
                }
            }
        }

        stage('Push image to docker hub') {
            steps {
                    script {
                     docker.withRegistry( '', registryCredential ) { 
                        dockerImage.push() 
                     }
                }
            }
            
    }
}
