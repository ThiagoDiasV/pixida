resource "aws_s3_bucket" "static-assets-pixida" {
  bucket = var.S3_ORIGIN_ID
  force_destroy = true
}

resource "aws_s3_bucket_acl" "pixida_acl" {
    bucket = aws_s3_bucket.static-assets-pixida.id
    acl = "public-read"
}

resource "aws_s3_bucket_public_access_block" "public_access_block" {
  bucket = aws_s3_bucket.static-assets-pixida.id

  ignore_public_acls = false
  restrict_public_buckets = false
  block_public_acls   = false
  block_public_policy = false
}

resource "aws_s3_bucket_policy" "app_static" {
  bucket = aws_s3_bucket.static-assets-pixida.id
  policy = jsonencode({
    Version = "2008-10-17"
    Id      = "PolicyForCloudFrontPrivateContent"
    Statement = [
      {
        Sid    = "1"
        Effect = "Allow"
        Principal = {
          AWS = "arn:aws:iam::cloudfront:user/CloudFront Origin Access Identity ${aws_cloudfront_origin_access_identity.origin_access_identity.id}"
        },
        Action   = "s3:GetObject",
        Resource = "${aws_s3_bucket.static-assets-pixida.arn}/*"
      }
    ]
  })
}