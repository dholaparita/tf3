
resource "aws_iam_user" "user" {
  name = "paritadhola"

  tags = {
    Name = "CLOD1003_Project"
  }
}

resource "aws_iam_user_policy" "user_policy" {
  name = "access_policy"
  user = aws_iam_user.user.name

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = [
          "s3:*",
        ]
        Effect = "Allow"

        Resource = [var.resource]

      },
    ]
  })
}
