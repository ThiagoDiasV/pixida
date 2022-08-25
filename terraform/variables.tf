variable "REGION" {
  type    = string
  default = "us-east-1"
}

variable "RDS_DB_NAME" {
  type = string
}

variable "RDS_USERNAME" {
  type = string
}

variable "RDS_PASSWORD" {
  type = string
}

variable "S3_ORIGIN_ID" {
  type    = string
  default = "pixida-static-assets-"
}