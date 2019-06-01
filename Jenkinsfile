pipeline {
    agent {node 'Windows_node'}
    stages {
        stage('Create Virtual ENV') {
            steps {
                echo 'Create Virtual ENV'
                sh 'virtualenv venv'
            }
        }
        stage('Activate Virtual ENV') {
            steps {
                echo 'Activate Virtual ENV'
                sh '. venv/Scripts/activate'
            }
        }
        stage('Restore package') {
            steps {
                echo 'Restore package'
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Start Testing') {
            steps {
                echo 'Start testing'
                sh 'pytest --env=live -m live_checker --html=report/report-$(date +%Y%m%d-%H%M%S).html'
            }
        }
        stage('End') {
            steps {
                echo 'Deactive ENV'
                sh 'deactivate'
            }
        }
    }
    post{
		always {
			echo 'Complete!'
		}
	}
}