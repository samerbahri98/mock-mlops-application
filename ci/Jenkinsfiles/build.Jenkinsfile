pipeline {
    agent {
        kubernetes {
            yamlFile 'ci/pod-templates/dind.pod-template.yml'
        }
    }
    parameters {
        string(name:'IMAGE',defaultValue:'training')
        string(name:'TAG',defaultValue:'main')
    }
    environment {
        DOCKER_HOST=credentials('DOCKER_HOST')
    }
    stages{
        stage('build'){
            steps {
                container('build'){
                    sshagent (credentials: ['GITHUB-SSH']) {
                        checkout scm
                        sh'''
cat << EOF >> /etc/ssh/ssh_config
UserKnownHostsFile /dev/null
StrictHostKeyChecking OFF
EOF
                        '''
                        sh "docker image ls"
                    }
                }
            }
        }
    }
}