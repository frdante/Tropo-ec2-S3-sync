# Tropo-ec2-S3-sync
Saving DLR results as a JSON document on your S3 bucket usinng ec2 instances as DLR URL.

This Python script will upload the Tropo DLR results from an AWS ec2 instance to your S3 bucket.

You just need to install Boto3 (https://boto3.readthedocs.io/en/latest/) from terminal doing *pip install boto3* and add your S3 Key, Secret Key in the script.

You may have to configure the default region on "config" file by doing:

Connect to your instance and type:

$ cd .aws
$ vim config

Type:

**[default]
region = your_default_region**

Then, run the script.

