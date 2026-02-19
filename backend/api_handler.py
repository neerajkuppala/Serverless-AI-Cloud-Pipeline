import json
import boto3
import uuid
from datetime import datetime

# Make sure this name matches your AWS Console EXACTLY (Case-Sensitive!)
TABLE_NAME = 'NeerajSummariesTable' 

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
        text = body.get('text_to_summarize', 'No text')
        summary = f"Summary: {text[:50]}..."

        # SAVE ATTEMPT
        print(f"Saving to {TABLE_NAME} with file_id...")
        table.put_item(
            Item={
                'file_id': str(uuid.uuid4()), # Matches your Partition Key exactly
                'text_content': text,
                'summary_text': summary,
                'date': datetime.now().isoformat()
            }
        )
        
        return {
            'statusCode': 200,
            'headers': headers,
            'body': json.dumps({'summary': summary, 'db_status': 'saved'})
        }
    except Exception as e:
        # This print will tell us the EXACT error in CloudWatch
        print(f"CRITICAL ERROR: {str(e)}")
        return {
            'statusCode': 500,
            'headers': headers,
            'body': json.dumps({'error': str(e)})
        }