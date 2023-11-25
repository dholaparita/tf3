

provider "aws" {
  region     = "us-east-1"
  access_key = "AKIARUA2ZLMD5M5UNR64"
  secret_key = "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"

}

module "aws_instance" {
  depends_on      = [module.aws_security_group]
  source          = "./modules/ec2"
  var_counter     = var.var_counter
  create_inst_ec2 = var.create_inst_ec2
  sg              = module.aws_security_group.security_group_id
}

module "aws_s3_bucket" {
  source = "./modules/s3"
}


module "iam" {
  source   = "./modules/iam"
  resource = module.aws_s3_bucket.s3_arn
}

module "aws_security_group" {
  source = "./modules/sg"
}


