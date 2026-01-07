terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0" # This ensures we use a modern 2026-ready version
    }
  }
}

provider "aws" {
  region = "us-east-1" # This is the data center location
}