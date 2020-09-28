import boto3
from urllib.parse import unquote_plus

s3 = boto3.resource('s3')


def lambda_handler(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = unquote_plus(event['Records'][0]['s3']['object']['key'])
    new_key = key.replace("firehose", "firehose_gzip")
    new_key = new_key + '.gz'

    print("Creating a new key: " + new_key + " for bucket " + bucket)
    copySource = bucket + '/' + key

    s3.Object(bucket, new_key).copy_from(CopySource=copySource)
    s3.Object(bucket, key).delete()

    return {

    }