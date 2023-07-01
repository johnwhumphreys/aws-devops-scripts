import boto3

asg_name = "your-asg-name-in-aws-console"
region = "us-east-1"
tag_name = "some-name"
tag_value = "some-value"

# create boto3 session
session = boto3.Session(region_name=region)

# Create Auto Scaling client
asg_client = session.client('autoscaling')

# Create EC2 resource object
ec2_resource = session.resource('ec2')

# Get the details of the Auto Scaling group
response = asg_client.describe_auto_scaling_groups(
    AutoScalingGroupNames=[
        asg_name,
    ]
)

# Get the list of EC2 instance IDs.
instances_ids = [instance['InstanceId'] for instance in response['AutoScalingGroups'][0]['Instances']]

# Add the given tag to all instances
ec2_resource.create_tags(
    Resources=instances_ids,
    Tags=[
        {
            'Key': tag_name,
            'Value': tag_value
        }
    ]
)
