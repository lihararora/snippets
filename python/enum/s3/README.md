# s3check.py
Maintains a state of all s3 buckets associated with a specific AWS account.

## Requirements:
1. python2.7
2. boto3 https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html

## Setup
1. pip install boto3
2. Configure your aws access key as described here: https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html#configuration.
3. NOTE: The AWS key must have a minumum of following permissions: "s3:ListAllMyBuckets", "s3:GetBucketAcl".

Example of sample policy:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
                "s3:ListAllMyBuckets",
                "s3:GetBucketAcl"
            ],
            "Resource": "*"
        }
    ]
}

```

## Usage
$ python s3check.py

(This checks for any local state (bucket_state.txt file) and updates the local state with the latest results from the scan.)
