# Python Script to upload files to AWS

This script is a wrapper over boto3 which makes developer easy to upload files to AWS

## Getting Started

Steps to get started:-
1. pip install s3manager

Steps to Use:-
1. from s3manager import S3manager
2. s3_object_manager = S3manager(bucket_name="bucketname", access_key=<access_key>, access_secret=<access_secret>)
3. s3_object_manager.upload_file(file_name=<file_name>, filepath=<filepath>, acl='public-read')
4. In response result will have url to the file uploaded and the key name of file in bucket
5. to delete the object s3_object_manager.delete_file(key)


### Prerequisites

boto3 should be installed



## Built With

* [python3]
* [boto3]




## Authors

* **Anshul Gupta** - *Initial work* - [AwsS3Manager]


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details



