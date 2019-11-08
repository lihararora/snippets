import boto3
import json

s3_resource = boto3.resource('s3')
s3_client = boto3.client('s3')

# Prints out the last known state of S3 buckets
def get_bucket_state():
    try:
        f = open('bucket_state.txt', 'r')
    except:
        print "Current state not found"
        return
    bucket_state = f.read()
    print "Current state:"
    print bucket_state
    f.close()

# This method checks if a bucket is public or not
def is_public(b):
    try:
        result = s3_client.get_bucket_acl(Bucket=b)
    except:
        print "Check permissions of you aws key"
        return
    grants = result.get('Grants')
    for grant in grants:
        grantee = grant.get('Grantee')
        g_type = grantee.get('Type')
        g_uri = grantee.get('URI')
        if g_type == 'Group' and g_uri == "http://acs.amazonaws.com/groups/global/AllUsers":
            return True
    return False

# This method updates local state to latest by checking the latest state on AWS
def update_bucket_state():
    latest_bucket_state = {}
    for bucket in s3_resource.buckets.all():
        if is_public(bucket.name):
            latest_bucket_state[bucket.name] = "Public"
        else:
            latest_bucket_state[bucket.name] = "Not Public"
    f = open('bucket_state.txt','w')
    f.write(str(latest_bucket_state))
    f.close()
    print "Latest state:"
    print latest_bucket_state

get_bucket_state()
update_bucket_state()
