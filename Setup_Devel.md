# Ambiente de testes
Para iniciar vamos criar uma virtualenv para isolar o projeto e poder brincar com as libs.
Instalamos as primeiras libs que iremos usar e partimos daí.
Resolvi usar a lib do Google ao invés da AWS (que tenho mais experiência) para poder aprender sobre ela na prática.
É preciso fazer um registro para utilizar as API's do Google Cloud.

## Fazer registro na Google Cloud
Fazer o registro é simples, mas você precisa inserir um cartão de crédito. Recebi $300,00 de bônus para gastar em até 1 ano. Meu objetivo é utilizar até o free tier mensal. Acesse: https://cloud.google.com/products/ para ver mais informações.

## Instalação
Criar uma virtualenv para o projeto `$ virtualenv --distribute --no-site-packages venv`. Ative sua nova **venv**: `$ source venv/bin/activate`. E depois instale a lib `$ pip install --upgrade google-cloud-vision`

## Autentificação
Vá ao GCP Console [https://console.cloud.google.com/apis/credentials/serviceaccountkey](https://console.cloud.google.com/apis/credentials/serviceaccountkey) e crie sua service account. Crie uma variável de ambiente para o arquivo de autenticação baixado `$ export GOOGLE_APPLICATION_CREDENTIALS="/home/user/service-account-file.json"`

## Vincular projeto a uma conta de faturamento
Verifique o link mostrado no seu console no retorno de erro ao fazer uma requisição a API.


## Ativar Cloud Vision API
Para ativar Google Cloud Vision acesse [https://console.cloud.google.com/apis/library/vision.googleapis.com](https://console.cloud.google.com/apis/library/vision.googleapis.com) e siga os passos para ativação.
