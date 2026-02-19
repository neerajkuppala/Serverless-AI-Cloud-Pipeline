import json
import boto3
import uuid
from datetime import datetime

# 1. Initialize the DynamoDB resource
# Make sure 'us-east-1' matches your AWS region!
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('YourExactTableNameHere') 

def lambda_handler(event, context):
    headers = {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "POST, OPTIONS",
        "Access-Control-Allow-Headers": "Content-Type"
    }

    # Handle OPTIONS pre-flight
    http_method = event.get('requestContext', {}).get('http', {}).get('method')
    if http_method == 'OPTIONS':
        return {'statusCode': 204, 'headers': headers, 'body': ''}

    try:
        body_str = event.get('body', '{}')
        body = json.loads(body_str)
        text = body.get('text_to_summarize', 'No text provided')

        # AI Summary Logic
        summary = f"Summary of your text: {text[:100]}..."

        # 2. THE FIX: Using 'file_id' to match your AWS Partition Key
        table.put_item(
            Item={
                'file_id': str(uuid.uuid4()),  # THIS MUST BE 'file_id'
                'original_text': text,
                'summary_result': summary,
                'created_at': datetime.now().isoformat()
            }
        )

        return {
            'statusCode': 200,
            'headers': headers,
            'body': json.dumps({
                'message': 'Saved successfully!',
                'summary': summary
            })
        }
    except Exception as e:
        print(f"ERROR: {str(e)}")
        return {
            'statusCode': 500,
            'headers': headers,
            'body': json.dumps({'error': str(e)})
        }