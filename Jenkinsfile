pipeline {
    agent {node 'windows'}
    stages {
        stage('Testing') {
            steps {
                echo 'Start testing'
                sh 'pytest --env=live -m debug --html=report/report-$(date +%Y%m%d-%H%M%S).html'
            }
        }
    }
    post{
		always {
			echo 'Complete!'
		}
	}
}