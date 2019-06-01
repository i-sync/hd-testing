pipeline {
    agent {node 'windows'}
    stages {
        stage('Virtual ENV') {
            steps {
                echo 'Create Virtual ENV'
                sh 'virtualenv venv'
            }
            steps {
                echo 'Activate Virtual ENV'
                sh '. venv/Scripts/activate'
            }
            steps {
                echo 'Restore package'
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Testing') {
            steps {
                echo 'Start testing'
                sh 'pytest --env=live -m debug --html=report/report-$(date +%Y%m%d-%H%M%S).html'
            }
        }
        stage('End') {
            steps {
                echo 'Deactive ENV'
                bat 'venv/Scripts/deactivate.bat'
            }
        }
    }
    post{
		always {
			echo 'Complete!'
		}
	}
}