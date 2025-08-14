pipeline {
    agent any

    environment {
        VENV = "venv"
        PYTHON = "/usr/local/bin/python3"   // Change if 'which python3' gives a different path
    }

    stages {
        stage('Clone GitHub Repo') {
            steps {
                git branch: 'main', url: 'https://github.com/AVVAVAISHNAVI/Pipelining_pythonApp.git'
            }
        }

        stage('Setup Python Environment') {
            steps {
                sh '${PYTHON} -m venv ${VENV}'
                sh '. ${VENV}/bin/activate && pip install --upgrade pip'
                sh '. ${VENV}/bin/activate && pip install -r requirements.txt'
            }
        }

        stage('Run Flask App') {
            steps {
                sh '. ${VENV}/bin/activate && python app.py'
            }
        }
    }
}






