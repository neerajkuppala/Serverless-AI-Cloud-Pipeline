# 1. THE STORAGE
resource "aws_s3_bucket" "my_bucket" {
  bucket        = "neeraj-serverless-project-v2-2026"
  force_destroy = true 
}

# 2. THE SECURITY (IAM)
resource "aws_iam_role" "lambda_role" {
  name = "microservice_lambda_role_v3"
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Action    = "sts:AssumeRole"
      Effect    = "Allow"
      Principal = { Service = "lambda.amazonaws.com" }
    }]
  })
}

resource "aws_iam_role_policy_attachment" "lambda_logs" {
  role       = aws_iam_role.lambda_role.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
}

# 3. THE ZIPPER
data "archive_file" "lambda_zip" {
  type        = "zip"
  source_file = "${path.module}/../backend/api_handler.py"
  output_path = "${path.module}/lambda_function_payload.zip"
}

# 4. THE BRAIN (Lambda)
resource "aws_lambda_function" "my_microservice" {
  filename         = data.archive_file.lambda_zip.output_path
  function_name    = "NeerajMicroserviceAPI_v2"
  role             = aws_iam_role.lambda_role.arn
  handler          = "api_handler.lambda_handler"
  runtime          = "python3.11"
  source_code_hash = data.archive_file.lambda_zip.output_base64sha256
}

# 5. THE FRONT DOOR (API Gateway with CORS fix)
resource "aws_apigatewayv2_api" "lambda_api" {
  name          = "NeerajMicroserviceGateway_v2"
  protocol_type = "HTTP"

  # THIS FIXES CORS: It tells the browser your website is allowed to call this API
  cors_configuration {
    allow_origins = ["*"]
    allow_methods = ["POST", "OPTIONS", "GET"]
    allow_headers = ["content-type"]
    max_age       = 300
  }
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

# THE POST ROUTE
resource "aws_apigatewayv2_route" "lambda_route" {
  api_id    = aws_apigatewayv2_api.lambda_api.id
  route_key = "POST /hello"
  target    = "integrations/${aws_apigatewayv2_integration.lambda_integration.id}"
}

# THE OPTIONS ROUTE (For Browser Pre-flight)
resource "aws_apigatewayv2_route" "options_route" {
  api_id    = aws_apigatewayv2_api.lambda_api.id
  route_key = "OPTIONS /hello"
  target    = "integrations/${aws_apigatewayv2_integration.lambda_integration.id}"
}

# 6. DATABASE
resource "aws_dynamodb_table" "project_db" {
  name         = "UserUploads_v2"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "UserId"
  attribute {
    name = "UserId"
    type = "S"
  }
}

# 7. PERMISSIONS
resource "aws_lambda_permission" "api_gw" {
  statement_id  = "AllowExecutionFromAPIGateway"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.my_microservice.function_name
  principal     = "apigateway.amazonaws.com"
  source_arn    = "${aws_apigatewayv2_api.lambda_api.execution_arn}/*/*"
}

# OUTPUTS
output "base_url" {
  value = "${aws_apigatewayv2_api.lambda_api.api_endpoint}/hello"
}