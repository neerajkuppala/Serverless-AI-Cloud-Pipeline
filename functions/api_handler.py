import json
import boto3
from botocore.exceptions import ClientError

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    bucket_name = 'neeraj-serverless-project-2026'
    
    # IMPORTANT: Change this to match the EXACT file name in your S3 bucket!
    # Looking at your previous screenshot, it was 'WhatsApp Image...' 
    file_name = 'test.txt' 

    # This creates a secure, temporary link for the file
    try:
        download_url = s3.generate_presigned_url('get_object',
            Params={'Bucket': bucket_name, 'Key': file_name},
            ExpiresIn=3600)
    except ClientError:
        download_url = "#"

    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Neeraj Cloud Dashboard</title>
        <style>
            body {{ font-family: 'Segoe UI', sans-serif; background: #f4f4f9; text-align: center; padding: 50px; }}
            .card {{ background: white; padding: 40px; border-radius: 20px; box-shadow: 0 10px 25px rgba(0,0,0,0.1); display: inline-block; max-width: 500px; }}
            .status-btn {{ background: #28a745; color: white; padding: 5px 15px; border-radius: 20px; font-weight: bold; font-size: 0.8em; }}
            .download-btn {{ background: #ff9900; color: white; padding: 15px 25px; text-decoration: none; border-radius: 8px; font-weight: bold; display: inline-block; margin-top: 25px; transition: 0.3s; }}
            .download-btn:hover {{ background: #e68a00; transform: translateY(-2px); }}
        </style>
    </head>
    <body>
        <div class="card">
            <h1>🚀 Neeraj's Serverless Dashboard</h1>
            <p>Status: <span class="status-btn">ACTIVE</span></p>
            <hr style="border: 0.5px solid #eee; margin: 20px 0;">
            <p>Your API is running perfectly on <strong>AWS Lambda</strong>!</p>
            <p>The S3 Bucket <strong>{bucket_name}</strong> is connected.</p>
            
            <a href="{download_url}" class="download-btn">📂 Download File from S3</a>
        </div>
    </body>
    </html>
    """

    return {
        'statusCode': 200,
        'headers': {'Content-Type': 'text/html'},
        'body': html_content
    }