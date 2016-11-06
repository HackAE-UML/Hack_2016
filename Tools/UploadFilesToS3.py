import boto3
import botocore
import sys
import os
import csv
import os.path

def print_bucket_files(s3):
        """Prints out all of the files in all of my buckets"""
        for bucket in s3.buckets.all():
                print(bucket.name)
                for ob in bucket.objects.all():
                        print("\t+" + ob.__str__())

#Constants
BUCKET_NAME = 'generationu-userfiles-mobilehub-762974824'

s3 = boto3.resource('s3')

##set environment vairables from rootkey.csv
vals = [];
if not os.path.exists('rootkey.csv'):
	print "rootkey.csv not found"
	exit()
	
with open('rootkey.csv', 'rb') as csvfile:
	reader = csv.reader(csvfile,delimiter='=')
	for row in reader:
	   vals.append(row[1]) 

if(len(vals) != 2):
	print "Incorrectly formatted rootkey file"
        exit()
		
os.environ['AWS_ACCESS_KEY_ID'] = vals[0]
os.environ['AWS_SECRET_ACCESS_KEY'] = vals[1]
os.environ['AWS_DEFAULT_REGION'] = 'us-east-1'


print"Updated S3 environment variables"

	
#Input Params
if len(sys.argv) == 1:
	print "Usage:\n"
	print "\tpython UploadFilesToS3.py filename\n"
	print "Uploads to SeniorProfiles/ by default"
	sys.exit(0)
else:
	fileName = sys.argv[1]

print "Uploading File\n"
print "AWS_ACCESS_KEY_ID = " + os.environ['AWS_ACCESS_KEY_ID']
print "AWS_SECRET_ACCESS_KEY = " +os.environ['AWS_SECRET_ACCESS_KEY']
s3.Object(BUCKET_NAME,'SeniorProfiles/' +fileName).put(Body=open( fileName,'rb'))

print "File " + fileName + " should be added."

print_bucket_files(s3)


                        
