import boto3
import botocore
import sys
import os

#Constants
BUCKET_NAME = 'generationu-userfiles-mobilehub-762974824'

#Hardcoding credentials which is bad practice, but this is quick and dirty.
os.environ['AWS_ACCESS_KEY_ID'] = 'AKIAJZRFXAQ6CB2W3SKQ'
os.environ['AWS_SECRET_ACCESS_KEY'] = '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'
os.environ['AWS_DEFAULT_REGION'] = 'us-east-1'

s3 = boto3.resource('s3')

#Input Params
if len(sys.argv) == 1:
	print "Usage:\n"
	print "\tpython UploadFilesToS3.py filename\n"
	print "Uploads to SeniorProfiles/ by default"
	sys.exit(0)
else:
	fileName = sys.argv[1]

print "Uploading File\n"
s3.Object(BUCKET_NAME,'SeniorProfiles/' +fileName).put(Body=open( fileName,'rb'))

print "File " + fileName + " should be added."
