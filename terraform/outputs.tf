output "cf_domain" {
  value = aws_cloudfront_distribution.static_distribution.domain_name
}
output "db_domain" {
  value = aws_db_instance.pixida.address
}
output "exec_lambda_role" {
  value = aws_iam_role.exec_lambda.arn
}
output "security_group_id" {
  value = aws_security_group.default.id
}