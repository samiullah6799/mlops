pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/samiullah6799/mlops.git']])
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip3 install -r requirements.txt'
            }
        }

        stage('Testing') {
            steps {
                sh 'python3 test.py'
            }
        }

        stage('Deploy') {
            script {
                def branchName = "${env.BRANCH_NAME}"
                deploy(branchName)

                
            }
        }
    }
}

def void deploy(String branchName) {
    if (branchName == "main") {
        println("Deploying to Production")
    } else if (branchName == "dev") {
        println("Deploying to UAT")
    }
}