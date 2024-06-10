# main.tf

provider "aws" {
  region = "us-east-1"  # Change this to your desired region
}

# Create an IAM role for the Lambda function
resource "aws_iam_role" "lambda_role" {
  name = "lambda_rds_role"
  assume_role_policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Action = "sts:AssumeRole",
        Principal = {
          Service = "lambda.amazonaws.com"
        },
        Effect   = "Allow",
        Sid      = ""
      }
    ]
  })
}

# Create a Lambda Layer for the dependencies
resource "aws_lambda_layer_version" "dependencies_layer" {
  filename         = "lambda_layer.zip"
  layer_name       = "dependencies_layer"
  compatible_runtimes = ["python3.8"]
}

# Define the Lambda function
resource "aws_lambda_function" "check_rds_connectivity" {
  function_name = "check_rds_connectivity_lambda"
  role          = aws_iam_role.lambda_role.arn
  handler       = "lambda_function.lambda_handler"
  runtime       = "python3.8"

  # Reference the local zip file for the function code
  filename      = "lambda_function.zip"
  source_code_hash = filebase64sha256("lambda_function.zip")

  # Attach the layer to the Lambda function
  layers        = [aws_lambda_layer_version.dependencies_layer.arn]

}

# Optional: Define a CloudWatch log group to capture Lambda logs
resource "aws_cloudwatch_log_group" "lambda_log_group" {
  name              = "/aws/lambda/check_rds_connectivity_lambda"
  retention_in_days = 7
}
