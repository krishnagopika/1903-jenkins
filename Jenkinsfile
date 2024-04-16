pipeline {
    agent any 
    stages {
        stage('Build') { 
            steps {
                sh 'python -m py_compile src/add2vals.py src/calc.py' 
                stash(name: 'compiled-results', includes: 'src/*.py*') 
            }
        }
    }
}