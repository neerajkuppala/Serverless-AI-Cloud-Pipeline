import json

def lambda_handler(event, context):
    # Standard headers required for the browser to "trust" the response
    headers = {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "POST, OPTIONS",
        "Access-Control-Allow-Headers": "Content-Type"
    }

    # Handle the 'OPTIONS' pre-flight request sent by browsers automatically
    # This is crucial for fixing "Connection Failed"
    http_method = event.get('requestContext', {}).get('http', {}).get('method')
    if http_method == 'OPTIONS':
        return {
            'statusCode': 204,
            'headers': headers,
            'body': ''
        }

    try:
        # Load the incoming text
        body_str = event.get('body', '{}')
        body = json.loads(body_str)
        text = body.get('text_to_summarize', 'No text provided')

        # Logic: Your "AI" processing
        summary = f"Summary of your text: {text[:100]}..."

        return {
            'statusCode': 200,
            'headers': headers,
            'body': json.dumps({
                'message': 'Success!',
                'summary': summary
            })
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'headers': headers,
            'body': json.dumps({'error': str(e)})
        }