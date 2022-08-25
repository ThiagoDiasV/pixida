resource "aws_iam_role" "exec_lambda" {
  name = "exec_lambda"
  path = "/"
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Principal = {
          Service = [
            "lambda.amazonaws.com"
          ]
        },
        Action = "sts:AssumeRole"
      },
    ]
  })
}
resource "aws_iam_policy" "exec_lambda_policy" {
  name        = "exec_lambda_policy"
  description = "Lambda policy"

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow",
        Action = [
          "lambda:InvokeFunction",
        ],
        Resource = "*"
      },
    ]
  })
}

resource "aws_iam_role_policy_attachment" "attach_role" {
  role       = aws_iam_role.exec_lambda.name
  policy_arn = aws_iam_policy.exec_lambda_policy.arn
}