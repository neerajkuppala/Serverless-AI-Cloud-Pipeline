import json

def lambda_handler(event, context):
    # These headers tell the browser: "It is safe to show this data on Amplify"
    headers = {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "POST, OPTIONS",
        "Access-Control-Allow-Headers": "Content-Type"
    }

    # Handle the 'OPTIONS' pre-flight request sent by browsers
    if event.get('requestContext', {}).get('http', {}).get('method') == 'OPTIONS':
        return {'statusCode': 204, 'headers': headers}

    try:
        body = json.loads(event.get('body', '{}'))
        text = body.get('text_to_summarize', 'No text provided')

        return {
            'statusCode': 200,
            'headers': headers,
            'body': json.dumps({
                'message': 'Success!',
                'summary': f"Processed: {text[:50]}..." 
            })
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'headers': headers,
            'body': json.dumps({'error': str(e)})
        }