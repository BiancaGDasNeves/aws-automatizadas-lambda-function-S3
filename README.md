## ☁️ Desafio DIO: Executando Tarefas Automatizadas com AWS Lambda e S3
# 📘 Descrição do Projeto

Este projeto foi desenvolvido como parte do desafio da Digital Innovation One (DIO), com o objetivo de aplicar na prática os conceitos de computação serverless e automação de tarefas utilizando AWS Lambda e Amazon S3.
A proposta é criar uma função Lambda automatizada que reage a eventos do S3, executando tarefas pré-definidas — como processar, converter, ou mover arquivos — e documentar toda a experiência técnica de forma organizada.

# 🧩 Objetivos de Aprendizagem

Ao concluir este desafio, fui capaz de:

* Implementar uma integração entre AWS Lambda e S3;
* Entender o funcionamento de eventos S3 (ObjectCreated, ObjectRemoved);
* Automatizar processos através de funções serverless;
* Documentar e versionar o projeto técnico utilizando o GitHub.

#🏗️ Arquitetura do Projeto

A solução segue o fluxo:

Usuário envia arquivo → Bucket S3 → Trigger (evento) → Lambda Function → Ação automatizada


Exemplo de automação:
* Quando um arquivo é enviado ao bucket S3 (ObjectCreated), a função Lambda é executada automaticamente para processar o arquivo e mover para outro bucket.
**Redimensionar uma imagem;
**Gerar logs;
**Converter formatos (ex: .csv → .json);
**Mover o arquivo para outro bucket.


#⚙️ Tecnologias Utilizadas

* AWS Lambda
* Amazon S3
* AWS CloudFormation (opcional)
* AWS IAM (para permissões)
* Python / Node.js
* AWS CloudWatch
* Git & GitHub
* Markdown

#🪜 Passo a Passo da Implementação
1️⃣ Criação do Bucket S3

* Criei um bucket chamado bianca-lambda-automation-s3 (ou nome similar);
* Configurei as permissões e as notificações de eventos para acionar a função Lambda.
2️⃣ Desenvolvimento da Função Lambda
* A função foi desenvolvida em Python 3.9 e configurada para ser acionada automaticamente ao detectar um novo arquivo no bucket.

Exemplo de código (Python):

import json
import boto3

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    bucket = event['Records'][0]['s3']['bucket']['name']
    arquivo = event['Records'][0]['s3']['object']['key']

    print(f"Novo arquivo detectado: {arquivo} no bucket {bucket}")

    # Exemplo de ação: copiar o arquivo para outro bucket
    destino = 'bianca-lambda-output'
    s3.copy_object(Bucket=destino, CopySource={'Bucket': bucket, 'Key': arquivo}, Key=arquivo)

    return {
        'statusCode': 200,
        'body': json.dumps(f"Arquivo {arquivo} processado com sucesso!")
    }

3️⃣ Deploy via Console ou CloudFormation

* Fiz o deploy da função Lambda e configurei a trigger S3;
* Testei o fluxo enviando arquivos e monitorando a execução via CloudWatch Logs.

4️⃣ Validação

* Realizei o upload de arquivos no bucket S3;
* Confirmei que a função foi acionada automaticamente e executou a automação configurada.

#🧠 Insights e Aprendizados

Durante o desenvolvimento deste desafio, aprendi:
* Como Lambda Functions podem automatizar processos sem servidores;
* A importância de configurar IAM Roles corretamente;
* Como o Amazon S3 e o CloudWatch interagem com Lambda para monitoramento;
* O valor de documentar e compartilhar o processo técnico para aprendizado contínuo.

#📚 Referências

[Documentação AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) 

[Documentação Amazon S3](https://docs.aws.amazon.com/s3/)

[Automatizar a configuração do S3 Object Lambda com CloudFormation](https://docs.aws.amazon.com/AmazonS3/latest/userguide/olap-cloudformation-template.html)

[GitHub Markdown Guide](https://guides.github.com/features/mastering-markdown/)


#💼 Autora

👩‍💻 Bianca Gonçalves das Neves
📧 biancagneves@gmail.com
💼 linkedin.com/in/biancagneves
🌐 [github.com/biancagdasneves](https://github.com/BiancaGDasNeves)
