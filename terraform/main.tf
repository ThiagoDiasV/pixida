terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 3.37"
    }
  }
  required_version = ">= 0.15.0"
}

provider "aws" {
  region     = var.REGION
}
