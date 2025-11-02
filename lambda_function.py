import json
import boto3
import urllib.parse

# Inicializa o cliente S3
s3 = boto3.client('s3')

def lambda_handler(event, context):
    """
    Função Lambda - Automatização de tarefas com AWS S3
    Desenvolvido por: Bianca Gonçalves das Neves
    Descrição:
        - Detecta novos arquivos enviados ao bucket S3 (evento ObjectCreated)
        - Copia o arquivo automaticamente para um bucket de saída
        - Gera logs no CloudWatch sobre o processo executado
    """

    # Loga o evento recebido (para debug)
    print("Evento recebido:")
    print(json.dumps(event, indent=4))

    # Extrai informações do evento S3
    source_bucket = event['Records'][0]['s3']['bucket']['name']
    source_key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'])
    destination_bucket = "bianca-output-bucket"  # Substitua pelo nome do seu bucket de saída

    try:
        print(f"📥 Novo arquivo detectado: {source_key}")
        print(f"📦 Bucket de origem: {source_bucket}")
        print(f"🚀 Copiando para bucket de destino: {destination_bucket}")

        # Copia o arquivo para o bucket de saída
        copy_source = {'Bucket': source_bucket, 'Key': source_key}
        s3.copy_object(Bucket=destination_bucket, CopySource=copy_source, Key=source_key)

        print(f"✅ Arquivo '{source_key}' copiado com sucesso para '{destination_bucket}'!")

        # Retorno da função (visível nos logs)
        return {
            'statusCode': 200,
            'body': json.dumps({
                'mensagem': 'Arquivo processado com sucesso!',
                'arquivo': source_key,
                'bucket_origem': source_bucket,
                'bucket_destino': destination_bucket
            })
        }

    except Exception as e:
        print(f"❌ Erro ao processar o arquivo: {str(e)}")
        raise e
