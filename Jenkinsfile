
pipeline {
    agent any

    environment {
        VENV = "venv"
    }

    stages {
        stage('Clone GitHub Repo') {
            steps {
                git branch: 'main', credentialsId: 'github-https', url: 'https://github.com/AVVAVAISHNAVI/Pipelining_pythonApp.git'
            }
        }

        stage('Setup Python Env') {
            steps {
                sh '/opt/homebrew/bin/python3 -m venv venv'
                sh '. venv/bin/activate && pip install --upgrade pip'
                sh '. venv/bin/activate && pip install -r requirements.txt'
            }
        }

        stage('Run Script') {
            steps {
                sh '. venv/bin/activate && python app.py'
            }
        }
    }
}




