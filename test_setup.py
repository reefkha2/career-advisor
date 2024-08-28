import boto3
from faker import Faker

fake = Faker()

print("Testing boto3 and Faker installations:")
print(f"Generated name: {fake.name()}")
print("AWS S3 buckets:")
try:
    s3 = boto3.client('s3')
    buckets = [bucket['Name'] for bucket in s3.list_buckets()['Buckets']]
    print(buckets)
except Exception as e:
    print(f"Error connecting to AWS: {e}")
    print("Make sure you've configured your AWS credentials correctly.")