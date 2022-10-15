pipeline {
    agent {
        kubernetes {
            yamlFile 'ci/pod-templates.yml'
        }
    }
    parameters {
        string(name:'IMAGE',defaultValue:'training')
        string(name:'TAG',defaultValue:'misc')
        string(name:'BRANCH',defaultValue:'main')
        string(name:'CONTEXT',defaultValue:'.')
        string(name:'DOCKERFILE',defaultValue:'.')
        string(name:'REPO',defaultValue:'mock-mlops-application')
    }
    environment {
        DOCKER_HOST=credentials('DOCKER_HOST')
    }
    stages{
        stage('build'){
            steps {
                container('dind'){
                    sshagent (credentials: ['GITHUB-SSH']) {
                        checkout scm
                        sh'''
cat << EOF >> /etc/ssh/ssh_config
UserKnownHostsFile /dev/null
StrictHostKeyChecking OFF
EOF
                        '''
                    }
                }
            }
        }
    }
}