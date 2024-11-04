terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "5.73.0"
    }
  }
}

provider "aws" {
  region = "us-east-1"
# Configuration options
}

resource "aws_s3_bucket" "example" {
  bucket = "scooterk-bucket"

  tags = {
    Name        = "My bucket"
    Environment = "Dev"
  }
}