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
  alias  = "ue1"
  # Configuration options
}

provider "aws" {
  region = "eu-west-1"
  alias  = "ew1"
  # Configuration options
}

resource "aws_s3_bucket" "example" {
  bucket   = "scooterk-bucket"
  provider = aws.ue1

  tags = {
    Name        = "My bucket"
    Environment = "Dev"
  }
}

resource "aws_s3_bucket" "example_2" {
  bucket   = "scooterk-bucket"
  provider = aws.ew1

  tags = {
    Name        = "My bucket"
    Environment = "Dev"
  }
}