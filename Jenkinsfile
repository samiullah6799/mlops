pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/samiullah6799/mlops.git']])
            }
        }
        
        stage('Installing Dependencies') {
            steps {
                sh 'pip3 install -r requirements.txt'
            }
        }
        
        stage('Execution of Unit Testcases') {
            steps {
                sh 'python3 test.py'
            }
        }
    }
}

