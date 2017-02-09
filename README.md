# Tropo-ec2-S3-sync
Saving DLR JSON results as a TXT document on your S3 bucket using AWS ec2 instance as server.

This Python script will upload the Tropo DLR results from an AWS ec2 instance to your S3 bucket using *itty* webserver on PORT 8888.

You just need to install [Boto3](https://boto3.readthedocs.io/en/latest/) from terminal typing **pip install boto3** and add your S3 Key, Secret Key in the script.

You may have to configure the *default region* on "config" file by typing the follwoing from terminal:

```
$ cd .aws
$ vim config
```

Then, add to the file:

```
[default]
region = your_default_region
```

Then, run the script.

Note that you may have to add PORT 8888 as inbound **Custom TCP Rule** in the ec2 Security Group, otherwise, you have just to change the port in the script to those you use as TCP connection.
