# Python Script to upload files to AWS

This script is a wrapper over boto3 which makes developer easy to upload files to AWS

## Getting Started

Steps to get started:-
1. pip install s3manager

Steps to Use:-


```
from s3manager import S3manager
s3_object_manager = S3manager(bucket_name="bucketname", access_key=<access_key>, access_secret=<access_secret>)
```
To upload file to s3
```
s3_object_manager.upload_file(file_name=<file_name>, filepath=<filepath>, acl='public-read')
```
In response result will have url to the file uploaded and the key name of file in bucket

to delete the object
```
s3_object_manager.delete_file(key)
```

to download the zip of multiple files
```python
s3_object_manager.download_files_in_zip(['fileobjkey1', 'fileobjkey2'],'nameofnewzip')
```
this will create a zip file in current directory and will return zip file name
### Prerequisites

boto3 should be installed



## Built With

* [python3]
* [boto3]




## Authors

* **Anshul Gupta** - *Initial work* - [AwsS3Manager]


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details



