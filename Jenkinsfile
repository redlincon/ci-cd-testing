pipeline {
    agent any
   
    stages {
         stage('Checkout') { // Checkout (git clone ...) the projects repository
            steps {
                    checkout scm
                }
        }
        stage('Setup') { // Install any dependencies you need to perform testing
            steps {
                script {
                    sh """
                       pip install -r requirements.txt \n
                    """
                    }
                }
            }
            stage("Testing"){                  
                steps {
                    script {

                sh """"
                cd /var/lib/jenkins/workspace/monitoring/ \n
                python -m unittest test_PaymentHubMonitor.py \n
                deactivate \n
                exit \n
                """"
                    }
                }
            }
            stage("Deploy"){
                steps {
                    script {
                                
                            sh """
                            zip -r PaymentHubMonitoring.zip * \n
                            aws cloudformation deploy --template-file cft.json --stack-name jenkinscftplugin-s3 --region us-east-1 --no-fail-on-empty-changeset \n
                            aws s3 cp PaymentHubMonitoring.zip s3://paymenthubchecker \n
                            """

                            }
                        }
            }


    }

}
