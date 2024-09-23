from cdktf import App, TerraformStack
from constructs import Construct
from cdktf_cdktf_provider_aws.provider import AwsProvider
from cdktf_cdktf_provider_aws.vpc import Vpc
from cdktf_cdktf_provider_aws.subnet import Subnet
from cdktf_cdktf_provider_aws.instance import Instance


from config import Config  # Import the configuration

def create_vpc(stack: TerraformStack):
    """Create and return a VPC resource."""
    return Vpc(stack, "MyVPC",
               cidr_block=Config.VPC_CIDR,
               enable_dns_support=True,
               enable_dns_hostnames=True)

def create_subnet(stack: TerraformStack, vpc_id: str):
    """Create and return a Subnet resource."""
    return Subnet(stack, "MySubnet",
                  vpc_id=vpc_id,
                  cidr_block=Config.SUBNET_CIDR)

def create_ec2_instance(stack: TerraformStack, subnet_id: str):
    """Create and return an EC2 instance resource."""
    return Instance(stack, Config.INSTANCE_NAME,
                    ami=Config.AMI_ID,
                    instance_type=Config.INSTANCE_TYPE,
                    subnet_id=subnet_id,
                    tags={"Name": Config.EC2_NAME_TAG})

class MyEc2Stack(TerraformStack):
    def __init__(self, scope: Construct, id: str):
        super().__init__(scope, id)

        # Configure AWS Provider
        AwsProvider(self, "AWS", region=Config.REGION)

        # Create resources
        vpc = create_vpc(self)
        subnet = create_subnet(self, vpc.id)
        create_ec2_instance(self, subnet.id)

app = App()
MyEc2Stack(app, Config.STACK_ID)  # Use stack ID from JSON
app.synth()
