import hashlib
import boto3

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    obj = s3.get_object(Bucket=bucket, Key=key)
    data = obj['Body'].read()
    hash_md5 = hashlib.md5(data).hexdigest()
    print(f'MD5 hash: {hash_md5}')
    return {'hash': hash_md5}
