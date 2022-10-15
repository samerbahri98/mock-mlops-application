pipeline {
    agent {
        kubernetes {
            yamlFile 'ci/pod-templates.yml'
        }
    }
    stages{
        stage('change'){
            steps{
                container('dind'){
                    sshagent (credentials: ['GITHUB-SSH']) {
                        sh "ln -s $GITCONFIG ~/.gitconfig"
                        checkout scm
                        sh '''
                            cat << EOF > service/migrations/0002.branch.sql
                            --
                            -- file: migrations/0002.branch.sql
                            --
                            ALTER TABLE `logs` ALTER `branch` SET DEFAULT '${params.BRANCH}';
                            EOF
                        '''
                        sh '''
                            git branch ${BRANCH}
                            git checkout ${BRANCH}
                            git add service/migrations/0002.branch.sql
                            git commit -m "${params.BRANCH} fix: branch default"
                            git push -u origin ${params.BRANCH}
                        '''
                    }
                }
            }
        }
        stage('pull-request'){
            steps{
                container('curl'){
                    def command = """
                        {
                            \"head\" : \"${BRANCH}\",
                            \"base\" : \"main\"
                        }
                    """
                    httpRequest (
                        consoleLogResponseBody: true,
                        contentType: 'APPLICATION_JSON',
                        httpMode: 'POST',
                        requestBody: command,
                        url: ' https://api.github.com/repos/samerbahri98/mock-mlops-application/pulls',
                        validResponseCodes: '201'
                    )
                }
            }
        }
    }
    parameters {
        string(name:'BRANCH',defaultValue:'main')
    }
    environment {
        GITCONFIG=credentials('GITCONFIG')
    }
}