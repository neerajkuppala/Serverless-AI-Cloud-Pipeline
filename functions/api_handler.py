import json

def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*', # This allows your Amplify site to call the API
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Methods': 'OPTIONS,POST'
        },
        'body': json.dumps({
            "summary": "[BETA SUMMARIZER]: Your connection is successful! Replace this with AI logic once the quota is approved."
        })
    }