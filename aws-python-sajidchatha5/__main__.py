import pulumi
import pulumi_aws as aws
import os

# Replace this with your desired AWS region
aws_region = "us-east-1"

# Replace this with your desired bucket name
bucket_name = "my-s3-bucket"

# Create an S3 bucket with versioning enabled
bucket = aws.s3.Bucket(
    bucket_name,
    versioning={
        "enabled": True,
    },
)

# Export the bucket name and ARN to be able to access them later
pulumi.export("bucket_name", bucket.id)
pulumi.export("bucket_arn", bucket.arn)

# Get a list of all .txt files in the local directory
local_directory = "./"  # Replace this with your local directory path
txt_files = [f for f in os.listdir(local_directory) if f.endswith(".txt")]

# Upload each .txt file to the S3 bucket
for txt_file in txt_files:
    file_path = os.path.join(local_directory, txt_file)
    aws.s3.BucketObject(
        txt_file,
        bucket=bucket_name,
        source=pulumi.FileAsset(file_path),
    )

