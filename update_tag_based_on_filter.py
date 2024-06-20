import boto3

# Initialize EC2 client
ec2_client = boto3.client('ec2', region_name="us-east-1")

#Tag to update change it accordingly.
tag_to_update = "Name"
new_tag_value = "kk"

# Define the environment tag to filter by
filters = [{'Name':'tag:Environmet', 'Values':['Production']},
           {'Name':'instance-state-name', 'Values':['running']}]

# Use describe_instances with filters
response = ec2_client.describe_instances(Filters=filters)

# Collect instance IDs that match the filter
instance_ids = [instance['InstanceId'] for reservation in response['Reservations'] for instance in reservation['Instances']]
print("*"*60)
print("Number of instances based on filter :",len(instance_ids))
print("*"*60)

if instance_ids:
    # Update the "Environment" tag value for these instances
    ec2_client.create_tags(
        Resources=instance_ids,
        Tags=[
            {
                'Key': tag_to_update,
                'Value': new_tag_value
            }
        ]
    )
    print(f'Successfully updated the "{tag_to_update}" tag to "{new_tag_value}" for instances: {instance_ids}')
    print("*"*60)
else:
    print('No instances found with the specified tag value.')
