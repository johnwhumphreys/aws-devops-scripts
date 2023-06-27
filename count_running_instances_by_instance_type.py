import boto3
from collections import Counter

# Create a session using your current profile
session = boto3.Session()

# Create a resource object for 'ec2' service
ec2_resource = session.resource('ec2')

# Getting all running instances
instances = ec2_resource.instances.filter(
    Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])

# Count instances by instance type
instance_types = Counter([instance.instance_type for instance in instances.all()])

# Calculate total number of instances
total_instances = sum(instance_types.values())

# Calculate percentage for each instance type and sort
percentages = {instance_type: (count / total_instances) * 100
               for instance_type, count in instance_types.items()}
percentages_sorted = dict(sorted(percentages.items(), key=lambda item: item[1], reverse=True))

# Print the top 5 instance types by percentage and count
for instance_type, percentage in list(percentages_sorted.items())[:5]:
    print(f'Instance Type: {instance_type}, Count: {instance_types[instance_type]}, Percentage: {round(percentage)}%')
