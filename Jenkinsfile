pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh './build.sh'            
            }
        }
        stage('Test') {
            steps {
                sh './tests.sh'
            }
        }
        stage('Package') {
            steps {
                sh './package.sh'
            }
        }
        stage('Publish') {
            steps {
                  ansiblePlaybook become: true, disableHostKeyChecking: true, playbook: 'playbook_publish.yml'
            }
        }
    }
}
