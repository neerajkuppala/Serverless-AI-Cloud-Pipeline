import json
import boto3
import uuid
from datetime import datetime

# Table Name matches your AWS setup
TABLE_NAME = 'UserUploads_v2' 

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table(TABLE_NAME)

def lambda_handler(event, context):
    headers = {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "POST, OPTIONS",
        "Access-Control-Allow-Headers": "Content-Type"
    }

    if event.get('requestContext', {}).get('http', {}).get('method') == 'OPTIONS':
        return {'statusCode': 204, 'headers': headers, 'body': ''}

    try:
        body = json.loads(event.get('body', '{}'))
        text = body.get('text_to_summarize', 'No text provided')
        
        generated_summary = f"Summary: {text[:100]}..."

        # SAVE ATTEMPT
        # THE FIX: Changed 'file_id' to 'UserId' to match your Partition Key
        table.put_item(
            Item={
                'UserId': str(uuid.uuid4()), 
                'original_text': text,
                'summary': generated_summary,
                'timestamp': datetime.now().isoformat()
            }
        )

        return {
            'statusCode': 200,
            'headers': headers,
            'body': json.dumps({
                'summary': generated_summary
            })
        }

    except Exception as e:
        print(f"ERROR: {str(e)}")
        return {
            'statusCode': 200, 
            'headers': headers,
            'body': json.dumps({
                'summary': f"Error: {str(e)}"
            })
        }