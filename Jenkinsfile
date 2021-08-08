pipeline {
    agent any
   
    stages {
         stage('Checkout') { // Checkout (git clone ...) the projects repository
            steps {
                    checkout scm
                }
        }
        stage('Setup') { //Initiating Virtual Environment & Install any dependencies you need to perform testing
            steps {
                script {
                    sh "virtualenv -p python3 py3env"
                    sh "source py3env/bin/activate"
                    sh "pip3 install -r ./requirement.txt"
                    }
                }
            }
            stage("Testing"){ // Run Tests                  
                steps {
                    script {

                sh "cd /var/lib/jenkins/workspace/monitoring/"
                sh "python3 -m unittest test_PaymentHubMonitor.py"               
                
                    }
                }
            }
            stage("Deploy To S3"){ //Deploy to S3
                steps {
                    script {
                                
                            sh "zip -r PaymentHubMonitoring.zip * "
                            sh "aws cloudformation deploy --template-file cft.json --stack-name jenkinscftplugin-s3 --region us-east-1 --no-fail-on-empty-changeset"
                            sh "aws s3 cp PaymentHubMonitoring.zip s3://paymenthubchecker"

                    }
                }
            }
            stage("Update lambda"){ //Deploy to S3
                            steps {
                                script {
                                        sh "aws lambda update-function-code --function-name PaymentHubMonitoring --region us-east-1 --s3-bucket s3://paymenthubchecker"

                                }
                            }
                        }


    }

}
