output "s3_bucket_details" {
  description = "Outputs attributes of our S3 bucket"
  value = [
    "Bucket Id: ${aws_s3_bucket.scooterk-bucket.id}",
    "Bucket ARN: ${aws_s3_bucket.scooterk-bucket.arn}",
    "Bucket Domain: ${aws_s3_bucket.scooterk-bucket.bucket_domain_name}"
  ]
}
