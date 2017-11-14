# ############################################### #
# @author anshulgupta217@gmail.com ############## #
# this script uploads, delete file from s3 bucket #
###################################################

import boto3
from boto3.session import Session


class AwsS3Manager(object):
	__AWS_KEY = ""
	__AWS_SECRET = ""

	def __init__(self, bucket_name):
		self.__bucket_name = bucket_name
		self.__session = Session(aws_access_key_id=self.__AWS_KEY,
                  				 aws_secret_access_key=self.__AWS_SECRET,
                  				 )
		self.s3 = self.__session.resource('s3')

	def upload_file(self,file_name,filepath=None, filedata=None):
		if filepath != None:
			data = open(filepath, 'rb')
		else:
			data = filedata
		object_ = self.s3.Bucket(self.__bucket_name).put_object(Key=file_name, Body=data, ACL='public-read')
		s3client = self.__session.client('s3')
		url = s3client.generate_presigned_url('put_object', Params={'Bucket': self.__bucket_name, 'Key': object_.key})
		return {"url":url,"key":object_.key}

