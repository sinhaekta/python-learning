import boto3
print(boto3.__version__)

# Create an S3 client
s3 = boto3.client("s3")

response = s3.list_buckets() # call the list_buckets method (aws api)

for bucket in response["Buckets"]:
    print(bucket["Name"])

# Create an EC2 resource
ec2 = boto3.resource("ec2")

for instance in ec2.instances.all():
    print(instance.id, instance.state["Name"])

# client vs resource
# client → low-level service access, requires more code to interact with AWS services
# resource → high-level, object-oriented interface, easier to use for common tasks