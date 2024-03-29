pipeline {
    environment {
      branchname =  env.BRANCH_NAME.toLowerCase()
      kubeconfig = getKubeconf(env.branchname)
      registryCredential = 'jenkins_registry'
      namespace = "${env.branchname == 'develop' ? 'projetosrapidos-dev' : env.branchname == 'homolog' ? 'projetosrapidos-hom' : env.branchname == 'homolog-r2' ? 'projetosrapidos-hom2' : 'sme-projetosrapidos' }"
    }
  
    agent { kubernetes { 
              label 'python36'
              defaultContainer 'builder'
            }
          }

    options {
      buildDiscarder(logRotator(numToKeepStr: '15', artifactNumToKeepStr: '15'))
      disableConcurrentBuilds()
      skipDefaultCheckout()
    }
  
    stages {

        stage('CheckOut') {            
            steps { checkout scm }            
        }        

        stage('AnaliseCodigo') {
          when { branch 'homolog' }
          steps {
              withSonarQubeEnv('sonarqube-local'){
                sh 'echo "[ INFO ] Iniciando analise Sonar..." && sonar-scanner \
                -Dsonar.projectKey=SME-ProjetosRapidos-BackEnd \
                -Dsonar.sources=.'
            }
          }
        }        

        stage('Build') {
          when { anyOf { branch 'master'; branch 'main'; branch "story/*"; branch 'development'; branch 'develop'; branch 'release'; branch 'homolog';  } }
          agent { kubernetes { 
              label 'builder'
              defaultContainer 'builder'
            }
          } 
          steps {
          checkout scm
            script {
              imagename1 = "registry.sme.prefeitura.sp.gov.br/${env.branchname}/projetosrapidos-back"
              dockerImage1 = docker.build(imagename1, "-f Dockerfile .")
              docker.withRegistry( 'https://registry.sme.prefeitura.sp.gov.br', registryCredential ) {
              dockerImage1.push()
              }
              sh "docker rmi $imagename1"
            }
          }
        }
        
        stage('Deploy'){
            when { anyOf {  branch 'master'; branch 'main'; branch 'develop'; branch 'development'; branch 'release'; branch 'homolog';  } }
            agent { kubernetes { 
              label 'builder'
              defaultContainer 'builder'
            }
          }        
            steps {
            checkout scm
                script{                        
                    withCredentials([file(credentialsId: "${kubeconfig}", variable: 'config')]){
                        sh('cp $config '+"$home"+'/.kube/config')
                        sh 'kubectl rollout restart deployment/projetosrapidos-back -n ${namespace}'                            
                    }                    
                }
            }           
        } 

    }
}


def getKubeconf(branchName) {
    if("main".equals(branchName)) { return "config_prd"; }
    else if ("master".equals(branchName)) { return "config_prd"; }
    else if ("homolog".equals(branchName)) { return "config_release"; }
    else if ("release".equals(branchName)) { return "config_release"; }
    else if ("development".equals(branchName)) { return "config_release"; }
    else if ("develop".equals(branchName)) { return "config_release"; }
}
