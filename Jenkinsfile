pipeline {
    agent any
    environment{
        CONTAINER_COUNT = 1
    }
    stages{
        stage('Build Python Docker Image'){
            steps{
                echo 'Building the python app docker image ...'
                bat "buildPythonAppImage.bat"
            }
        }
        stage('Launch Python Docker Containers'){
            steps{
                echo 'Launching the python app docker containers ...'
                bat "startPythonApp.bat ${CONTAINER_COUNT}"
            }
        }
    }
}