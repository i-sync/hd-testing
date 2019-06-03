pipeline {
    agent {node 'Windows_node'}
    stages {
        stage('Testing') {
            steps {
                echo 'Start Testing'
                bat '''
                    if not exist venv virtualenv venv
                    call venv\\Scripts\\activate.bat
                    pip install -r requirements.txt
                    pytest -n 2 --env=live --headless=True -m live_checker --html=report/report-${BUILD_NUMBER}.html
                    deactivate
                '''
            }
        }
    }
    post{
        failure {
            emailext body: """<p>FAILED: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]':</p>
                <p>Check console output at &QUOT;<a href='${env.BUILD_URL}'>${env.JOB_NAME} [${env.BUILD_NUMBER}]</a>&QUOT;</p>""",
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