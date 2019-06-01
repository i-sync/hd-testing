pipeline {
    agent {node 'Windows_node'}
    stages {
        stage('Testing') {
            steps {
                echo 'Start Testing'
                sh '''
                    if [ ! -d "venv" ]; then
                        virtualenv venv
                    fi
                    source venv/Scripts/activate
                    pip install -r requirements.txt
                    pytest --env=live -m live_checker --html=report/report-$(date +%Y%m%d-%H%M%S).html
                    deactivate
                '''
            }
        }
    }
    post{
		always {
			echo 'Complete!'
		}
	}
}