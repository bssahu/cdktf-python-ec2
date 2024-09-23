import os
import json
from dotenv import load_dotenv

# Load environment variables from .env file (if required)
load_dotenv()

class Config:
    # Load JSON configuration file
    with open('config.json', 'r') as f:
        config_data = json.load(f)

    REGION = os.getenv("REGION", "us-east-1")
    AMI_ID = os.getenv("AMI_ID", "ami-0c55b159cbfafe1f0")
    INSTANCE_TYPE = os.getenv("INSTANCE_TYPE", "t2.micro")
    VPC_CIDR = os.getenv("VPC_CIDR", "10.0.0.0/16")
    SUBNET_CIDR = os.getenv("SUBNET_CIDR", "10.0.1.0/24")

    # Values from the JSON file
    INSTANCE_NAME = config_data["instance_name"]
    EC2_NAME_TAG = config_data["ec2_name_tag"]
    STACK_ID = config_data["stack_id"]
