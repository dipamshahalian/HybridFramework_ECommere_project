pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/dipamshahalian/HybridFramework_ECommere_project.git'
            }
        }
        stage('Setup Python Environment') {
            steps {
                sh 'python -m venv venv'
                sh 'source venv/bin/activate'
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run Selenium Tests') {
            steps {
                sh 'pytest --alluredir=allure-results'
            }
        }
        stage('Generate Allure Report') {
            steps {
                allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]
            }
        }
    }
}
