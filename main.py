#!/usr/bin/env python
from constructs import Construct
from cdktf import App, TerraformStack
from cdktf_cdktf_provider_aws.provider import AwsProvider
from cdktf_cdktf_provider_aws.instance import Instance
from cdktf_cdktf_provider_aws.subnet import Subnet
from cdktf_cdktf_provider_aws.vpc import Vpc

class MyStack(TerraformStack):
    def __init__(self, scope: Construct, id: str):
        super().__init__(scope, id)

        #Configure AWS provider
        self.provider = AwsProvider(self, "aws", region="us-east-1");
        #create a vpc
        self.vpc = Vpc(self, "vpc", cidr_block="10.0.0.0/16", enable_dns_hostnames=True, enable_dns_support=True) # type: ignore

        #create a subnet
        self.subnet = Subnet(self, "subnet", vpc_id=self.vpc.id, cidr_block="10.0.1.0/24", availability_zone="us-east-1a")  

        #create ec2 instance
        self.instance = Instance(self, "instance", 
                                 ami="ami-0b5eea76982371e91", 
                                 instance_type="t2.micro", 
                                 subnet_id=self.subnet.id,
                                 tags={"Name": "my-ec2-instance"} ) 
        


app = App()
MyStack(app, "my-ec2-instance")

app.synth()
