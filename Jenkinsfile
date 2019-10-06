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
               echo "TODO: publish"
            }
        }
        stage('Deploy') {
            steps {
                echo "TODO: deploy"
            }
        }
    }
}
