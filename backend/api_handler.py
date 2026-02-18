import json

def lambda_handler(event, context):
    # This allows your Amplify site to talk to this Lambda
    headers = {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "POST, GET, OPTIONS",
        "Access-Control-Allow-Headers": "Content-Type"
    }

    try:
        # Check if we got a body
        body = json.loads(event.get('body', '{}'))
        user_text = body.get('text_to_summarize', 'No text provided')

        return {
            'statusCode': 200,
            'headers': headers,
            'body': json.dumps({
                'message': 'Success!',
                'summary': f"AI Summary: {user_text[:50]}..." # Placeholder logic
            })
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'headers': headers,
            'body': json.dumps({'error': str(e)})
        }