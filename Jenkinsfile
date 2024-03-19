pipeline {
    agent any

    options{
        // Max number of build logs to keep and days to keep
        buildDiscarder(logRotator(numToKeepStr: '5', daysToKeepStr: '5'))
        // Enable timestamp at each job in the pipeline
        timestamps()
    }

    environment{
        registry = 'tuanht2/news-summarization'
        registryCredential = 'dockerhub'
    }

    stages {
        stage('Test') {
            agent {
                docker {
                    image 'python:3.8'
                }
            }
            steps {
                echo 'Testing model correctness..'
                sh 'pip install -r requirements.txt'
                sh 'make test'
            }
        }
        stage('Build') {
            when {
                branch 'master'
            }
            steps {
                script {
                    echo 'Building image for deployment..'
                    dockerImage = docker.build registry + ":$BUILD_NUMBER"
                    echo 'Pushing image to dockerhub..'
                    docker.withRegistry( '', registryCredential ) {
                        dockerImage.push()
                        dockerImage.push('latest')
                    }
                    sh 'docker system prune --all --force'
                }
            }
        }
        stage('Deploy') {
            when {
                branch 'master'
            }
            agent {
                kubernetes {
                    containerTemplate {
                        name 'helm' // Name of the container to be used for helm upgrade
                        image 'duong05102002/jenkins-k8s:latest' // The image containing helm
                    }
                }
            }
            steps {
                script {
                    steps
                    container('helm') {
                        sh("helm upgrade --install news-summarization --set image.repository=${registry} \
                        --set image.tag=v${BUILD_NUMBER} ./helm-charts/model-deployment --namespace model-serving")
                    }
                }
            }
        }
    }
}
