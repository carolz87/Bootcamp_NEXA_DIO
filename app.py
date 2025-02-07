import boto3

def lambda_handler(event, context):
    textract = boto3.client('textract')
    response = textract.detect_document_text(
        Document={'S3Object': {'Bucket': event['bucket'], 'Name': event['name']}}
    )
    return response