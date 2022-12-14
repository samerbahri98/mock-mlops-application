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
                        sh """
cat << EOF > service/migrations/0002.branch.sql
--
-- file: migrations/0002.branch.sql
--
ALTER TABLE logs ALTER branch SET DEFAULT '${params.BRANCH}';
EOF
                        """
                        sh"""
cat << EOF >> /etc/ssh/ssh_config
UserKnownHostsFile /dev/null
StrictHostKeyChecking OFF
EOF
                        """
                        sh """
                            git branch ${params.BRANCH}
                            git checkout ${params.BRANCH}
                            git add service/migrations/0002.branch.sql
                            git commit -m "${params.BRANCH} fix: branch default"
                            git push -u origin ${params.BRANCH}
                        """
                    }
                }
            }
        }
        stage('pull-request'){
            steps{
                container('curl'){
                    httpRequest (
                        consoleLogResponseBody: true,
                        contentType: 'APPLICATION_JSON',
                        httpMode: 'POST',
                        requestBody: """
                            {
                                "title" : "${params.BRANCH} -> main",
                                "head" : "${params.BRANCH}",
                                "base" : "main"
                            }
                        """,
                        url: 'https://api.github.com/repos/samerbahri98/mock-mlops-application/pulls',
                        validResponseCodes: '201',
                        customHeaders: [[name:'Authorization', value:"Bearer $GITHUB_PAT_PSW"]]
                    )
                }
            }
        }
    }
    parameters {
        string(name:'BRANCH',defaultValue:'dev')
    }
    environment {
        GITCONFIG=credentials('GITCONFIG')
        GITHUB_PAT=credentials('Github-PAT')
    }
}