# 1. THE STORAGE (S3 Bucket)
resource "aws_s3_bucket" "my_bucket" {
  bucket        = "neeraj-serverless-project-2026"
  force_destroy = true 
}

# 2. THE SECURITY (IAM Role)
resource "aws_iam_role" "lambda_role" {
  name = "microservice_lambda_role_v2"
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Action    = "sts:AssumeRole"
      Effect    = "Allow"
      Principal = { Service = "lambda.amazonaws.com" }
    }]
  })
}

# S3 Permissions
resource "aws_iam_role_policy" "s3_access" {
  name = "lambda_s3_policy"
  role = aws_iam_role.lambda_role.id
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Action   = ["s3:GetObject", "s3:ListBucket"]
      Effect   = "Allow"
      Resource = ["${aws_s3_bucket.my_bucket.arn}", "${aws_s3_bucket.my_bucket.arn}/*"]
    }]
  })
}

# 3. THE ZIPPER (Points to your backend folder)
data "archive_file" "lambda_zip" {
  type        = "zip"
  source_file = "${path.module}/../backend/api_handler.py"
  output_path = "${path.module}/lambda_function_payload.zip"
}

# 4. THE BRAIN (Lambda Function)
resource "aws_lambda_function" "my_microservice" {
  filename         = data.archive_file.lambda_zip.output_path
  function_name    = "NeerajMicroserviceAPI"
  role             = aws_iam_role.lambda_role.arn
  handler          = "api_handler.lambda_handler"
  runtime          = "python3.11"
  source_code_hash = data.archive_file.lambda_zip.output_base64sha256
}

# 5. THE FRONT DOOR (API Gateway)
resource "aws_apigatewayv2_api" "lambda_api" {
  name          = "NeerajMicroserviceGateway"
  protocol_type = "HTTP"
}

resource "aws_apigatewayv2_stage" "lambda_stage" {
  api_id      = aws_apigatewayv2_api.lambda_api.id
  name        = "$default"
  auto_deploy = true
}

resource "aws_apigatewayv2_integration" "lambda_integration" {
  api_id           = aws_apigatewayv2_api.lambda_api.id
  integration_type = "AWS_PROXY"
  integration_uri  = aws_lambda_function.my_microservice.invoke_arn
}

resource "aws_apigatewayv2_route" "lambda_route" {
  api_id    = aws_apigatewayv2_api.lambda_api.id
  route_key = "GET /hello"
  target    = "integrations/${aws_apigatewayv2_integration.lambda_integration.id}"
}

# 6. DATABASE (DynamoDB)
resource "aws_dynamodb_table" "project_db" {
  name         = "UserUploads"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "UserId"
  attribute {
    name = "UserId"
    type = "S"
  }
}

# OUTPUTS
output "base_url" {
  value = "${aws_apigatewayv2_api.lambda_api.api_endpoint}/hello"
}