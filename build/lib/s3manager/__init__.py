# ############################################### #
# @author anshulgupta217@gmail.com ############## #
# this script uploads, delete file from s3 bucket #
###################################################

import os
import zipfile
from mimetypes import MimeTypes

import boto3
import botocore
from boto3.session import Session


class S3manager(object):
    """
    This manager is for uploading and deleting files from S3 bucket
    to run this manager you should have AWS_KEY and AWS_SECRET in os enviornment variables
    Attributes:
        bucket_name :- this is the s3 bucket name.
    """
    __AWS_KEY = os.environ.get('AWS_KEY', None)
    __AWS_SECRET = os.environ.get('AWS_SECRET', None)

    def __init__(self, bucket_name, access_key, access_secret):
        self.__AWS_KEY = access_key
        self.__AWS_SECRET = access_secret
        self.__bucket_name = bucket_name
        self.__session = Session(aws_access_key_id=self.__AWS_KEY,
                                 aws_secret_access_key=self.__AWS_SECRET,
                                 )
        self.s3 = self.__session.resource('s3')

    def upload_file(self, file_name, filepath=None, acl='public-read'):
        """Do upload_file and return dict of url and key.
        @:param file_name :- this is string.
        @:param filepath :- this is the path of the file to upload.
        @:param acl :-
        """
        mime = MimeTypes()
        mime_type = mime.guess_type(filepath)[0]
        data = open(filepath, 'rb')
        object_ = self.s3.Bucket(self.__bucket_name).put_object(Key=file_name, Body=data, ACL=acl,
                                                                ContentType=mime_type)
        s3client = self.__session.client('s3')
        url = s3client.generate_presigned_url(
            'put_object', Params={'Bucket': self.__bucket_name, 'Key': object_.key})
        return {"url": url, "key": object_.key,
                "public_url": "https://" + self.__bucket_name + ".s3.amazonaws.com/" + file_name}

    def delete_file(self, file_name):
        """Do delete_file and return True."""
        s3 = self.__session.resource("s3")
        obj = s3.Object(self.__bucket_name, file_name)
        obj.delete()
        return True

    def download_file(self, file_name):
        """This method will download the file in your current directory.
        """
        try:
                self.s3.Bucket(self.__bucket_name).download_file(file_name, os.path.join(os.getcwd(), str(file_name.split('/')[-1])))
        except botocore.exceptions.ClientError as e:
                if e.response['Error']['Code'] == "404":
                    print("The object does not exist.")
                else:
                    raise

    def download_files_in_zip(self, file_object_key_list, zip_file_name):
        """This method will download the file and will make zip current directory.
        @:param file_object_key_list :- this is list of filekeyobject of s3.
        """
        for KEY in file_object_key_list:
            try:
                self.s3.Bucket(self.__bucket_name).download_file(KEY, KEY.split('/')[-1])
            except botocore.exceptions.ClientError as e:
                if e.response['Error']['Code'] == "404":
                    print("The object does not exist.")
                else:
                    raise
        zf = zipfile.ZipFile(os.path.join(os.getcwd(), str(zip_file_name + ".zip")), "w")
        for KEY in file_object_key_list:
            KEY = KEY.split('/')[-1]
            zf.write(KEY)
        zf.close()
        for KEY in file_object_key_list:
            os.remove(KEY.split('/')[-1])

        return str(zip_file_name + ".zip")
