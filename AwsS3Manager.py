# ############################################### #
# @author anshulgupta217@gmail.com ############## #
# this script uploads, delete file from s3 bucket #
###################################################

import boto3
from boto3.session import Session


class AwsS3Manager(object):
	__AWS_KEY = "your aws key"
	__AWS_SECRET = "your aws secret"

	def __init__(self, bucket_name):
		print(" AwsS3Manager Initilized.")
		self.__bucket_name = bucket_name
		self.__session = Session(aws_access_key_id=self.__AWS_KEY,
                  				 aws_secret_access_key=self.__AWS_SECRET,
                  				 )
		self.s3 = self.__session.resource('s3')

	def upload_file(self,file_name,filepath):
		data = open(filepath, 'rb')
		object_ = self.s3.Bucket(self.__bucket_name).put_object(Key=file_name, Body=data)
		s3client = self.__session.client('s3')
		url = s3client.generate_presigned_url('put_object', Params={'Bucket': self.__bucket_name, 'Key': object_.key})
		return {"url":url,"key":object_.key}

