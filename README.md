# Install cdktf globally
npm install -g cdktf-cli

# Install pipenv for managing Python dependencies
pip install pipenv

python -m ensurepip

mkdir my-ec2-instance
cd my-ec2-instance
cdktf init --template=python
Python -m venv venv
source venv/bin/activate
pip install cdktf-cdktf-provider-aws


