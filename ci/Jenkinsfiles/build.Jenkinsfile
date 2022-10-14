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
        DOCKER_HOST="ssh://rundeck@thebahrimedia.com"
    }
    stages{
        stage('build'){
            steps {
                container('dind'){
                    sshagent (credentials: ['GITHUB-SSH']) {
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