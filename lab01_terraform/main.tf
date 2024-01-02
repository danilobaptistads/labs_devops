terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.16"
    }
  }

  required_version = ">= 1.2.0"
}

provider "aws" {
  region  = "sa-east-1"
}

resource "aws_instance" "lab01_terrafom" {
  ami           = "ami-0b6c2d49148000cd5"
  instance_type = "t2.micro"
  key_name	= "Key01"
}
