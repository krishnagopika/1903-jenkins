pipeline {
    environment {
        IMAGE = "krishnagopika4/demo-cicd-1903"
        registryCredential = 'dockerhub'
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
                def dockerImage = docker.build "${IMAGE}:latest"
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

        stage('run the docker container') {
            steps {
                script {
                    docker.image('$IMAGE:latest').pull("")
                    docker.image('$IMAGE:latest').run("-p 80:80 -d")  
                }
            }
        
        } 
    }
}
