# psycopg2
lambda execution role


provider "aws"{
  region = "us-west-2"  # Specify your region
}

resource "aws_iam_role""lambda_vpc_access_role"{
  name = "lambda-vpc-access-role"
  assume_role_policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
            {
       Effect = "Allow",
        Principal = {
          Service = "lambda.amazonaws.com"
                },
        Action = "sts:AssumeRole"
            }
        ]
    })
}

resource "aws_iam_role_policy_attachment""vpc_access_policy"{
  role       = aws_iam_role.lambda_vpc_access_role.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaVPCAccessExecutionRole"
}
