# Python Script to upload files to AWS

This script is a wrapper over boto3 which makes developer easy to upload files to AWS

## Getting Started

Steps to get started:-
1. Download the script 'AwsS3Manager'
2. Place it in you project
3. set you AWS secret and key into class 'AwsS3Manager'
4. Just instanciate it where ever you wnat in you project
    eg:- aws_obj = AwsS3Manager('your bucket name')
5. Now to upload object just call
	result = aws_obj.upload_file('file_name','filepath')
6. In response result will have url to the file uploaded and the key name of file in bucket


### Prerequisites

boto3 should be installed



## Built With

* [python3]
* [boto3]




## Authors

* **Anshul Gupta** - *Initial work* - [AwsS3Manager]


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details


