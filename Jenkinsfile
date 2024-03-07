pipeline {
    agent any
    stages {
        stage ('Checkout') {
            steps {
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/samiullah6799/mlops.git']])
            }
        }

        stage ('Installing Dependencies') {
            steps {
                sh "pip3 install -r requirements.txt"
            }
        }

        stage ('Testing') {
            steps {
                sh "pytest test.py"
            }
        }

        stage ('Deploy') {
            steps {
                script {
                    def branchName = "${env.BRANCH_NAME}"

                    if (branchName == 'main') {
                        echo "Deploying to production"
                    } else if (brancheName == 'dev') {
                        echo "Deploying to UAT."
                    }
                }
            }
        }
    }
}
//This is jenkinsfile