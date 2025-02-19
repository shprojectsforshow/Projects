#configure AWS 
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = ">= 5.5.0"
    }
  }
}

provider "aws" {
  region = "us-east-2"
}

data "aws_ami" "ubuntu" {
    most_recent = "true"

    filter {
        name="virtualization-type"
        values=["hvm"]
    }
    owners = [679593333241]
}

resource "aws_instance" "primary_vpn" {
    ami = data.aws_ami.ubuntu.id
    instance_type = "t2.micro"
    key_name = "ose"
    
    tags= {
        name="Primary_vpn"
    }
}

output "IP" {
    value=aws_instance.primary_vpn.public_ip
}