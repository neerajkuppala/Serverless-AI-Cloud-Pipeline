import json
import boto3
import uuid
from datetime import datetime

# 1. Initialize the DynamoDB resource outside the handler
dynamodb = boto3.resource('dynamodb')
# REPLACE 'YourTableNameHere' with your actual DynamoDB table name from AWS
table = dynamodb.Table('YourTableNameHere') 

def lambda_handler(event, context):
    headers = {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "POST, OPTIONS",
        "Access-Control-Allow-Headers": "Content-Type"
    }

    http_method = event.get('requestContext', {}).get('http', {}).get('method')
    if http_method == 'OPTIONS':
        return {'statusCode': 204, 'headers': headers, 'body': ''}

    try:
        body_str = event.get('body', '{}')
        body = json.loads(body_str)
        text = body.get('text_to_summarize', 'No text provided')

        # Your Summary Logic
        summary = f"Summary of your text: {text[:100]}..."

        # 2. SAVE TO DYNAMODB (The missing part!)
        table.put_item(
            Item={
                'id': str(uuid.uuid4()),        # Creates a unique ID for each entry
                'original_text': text,
                'summary_result': summary,
                'timestamp': datetime.now().isoformat()
            }
        )

        return {
            'statusCode': 200,
            'headers': headers,
            'body': json.dumps({
                'message': 'Success and Saved!',
                'summary': summary
            })
        }
    except Exception as e:
        print(f"Error: {str(e)}") # This helps you see errors in CloudWatch
        return {
            'statusCode': 500,
            'headers': headers,
            'body': json.dumps({'error': str(e)})
        }