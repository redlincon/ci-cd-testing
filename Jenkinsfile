pipeline {
    agent any
    stages {
            stage("Testing"){
                steps {
                sh "virtualenv -p python3 py3env"
                sh "source py3env/bin/activate"
                sh "source py3env/bin/activate"
                sh "cd /var/lib/jenkins/workspace/monitoring/"
                sh "python -m unittest test_PaymentHubMonitor.py"
                sh "deactivate"
                sh "exit"

                }
            }
            stage("Deploy"){
                            steps {
                            sh "zip -r PaymentHubMonitoring.zip *"
                            sh "aws cloudformation deploy --template-file cft.json --stack-name jenkinscftplugin-s3 --region us-east-1 --no-fail-on-empty-changeset"
                            sh "aws s3 cp PaymentHubMonitoring.zip s3://paymenthubchecker"

                            }
                        }


    }

}