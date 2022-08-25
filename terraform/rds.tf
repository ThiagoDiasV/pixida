resource "aws_db_instance" "pixida" {
  identifier                 = "pixida"
  allocated_storage          = 20
  storage_type               = "gp2"
  engine                     = "postgres"
  engine_version             = "14.3"
  instance_class             = "db.t3.micro"
  name                       = var.RDS_DB_NAME
  username                   = "postgres"
  password                   = var.RDS_PASSWORD
  port                       = 5432
  publicly_accessible        = true
  availability_zone          = "us-east-1a"
  security_group_names       = []
  vpc_security_group_ids     = [aws_security_group.default.id]
  parameter_group_name       = "default.postgres14"
  multi_az                   = false
  backup_retention_period    = 0
  backup_window              = "00:05-00:35"
  maintenance_window         = "sun:00:50-sun:08:50"
  auto_minor_version_upgrade = false
  copy_tags_to_snapshot      = true
  skip_final_snapshot        = true
}