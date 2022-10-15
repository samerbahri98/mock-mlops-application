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

                    sh """
                    curl \
                    -X POST \
                    -H "Accept: application/vnd.github+json" \
                    -H "Authorization: Bearer $GITHUB_PAT_PSW" \
                    https://api.github.com/repos/samerbahri98/mock-mlops-application/pulls \
                    -d '{"head":"${params.BRANCH}","base":"main"}'
                    """
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