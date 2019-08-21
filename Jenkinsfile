pipeline {
    agent {node 'Windows_node'}
    triggers {
        cron('H 13 * * *')
    }
    stages {
        stage('Testing') {
            steps {
                echo 'Start Testing'
                bat '''
                    if not exist venv virtualenv venv
                    call venv\\Scripts\\activate.bat
                    pip install -r requirements.txt
                    pytest -n 2 --env=live --headless=True -m live_checker --html=report/report-${BUILD_NUMBER}.html
                    exit %ERRORLEVEL%
                    deactivate
                '''
            }
        }
    }
    post{
        failure {
            emailext body: '''${SCRIPT, template="groovy-html.template"}''',
                mimeType: 'text/html',
                subject: "[Jenkins] ${currentBuild.fullDisplayName}",
                to: "michael.tian@profero.com, libby.qin@mullenloweprofero.com, ben.zhang@mullenloweprofero.com",
                replyTo: "michael.tian@profero.com, libby.qin@mullenloweprofero.com, ben.zhang@mullenloweprofero.com",
                recipientProviders: [[$class: 'CulpritsRecipientProvider']]
        }
		always {
			echo 'Complete!'
		}
	}
}