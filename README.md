# lambda-gzip-extension
This repo is a temporary workaround for the issue https://github.com/logstash-plugins/logstash-input-s3/issues/180#


## How to use this function
AWS Firehose creates a destination folder in bucket specified in the configartion.
Add a Event Rule on the S3 Bucket to trigger a Lambda function.
This Lambda function will download the file and upload it with a extension which Logstash can read and process the documents.

Make sure to use following policy so that Lambda has eneded access:

`{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "CloudWatchAllow",
            "Effect": "Allow",
            "Action": [
                "logs:CreateLogStream",
                "logs:PutLogEvents",
                "logs:CreateLogGroup"
            ],
            "Resource": "*"
        },
        {
            "Sid": "S3Allow",
            "Effect": "Allow",
            "Action": [
                "s3:PutObject",
                "s3:GetObject",
                "s3:DeleteObject"
            ],
            "Resource": "my-bucket/*"
        }
    ]
}`

Resource in the id S3Allow section should be your bucket ARN. The function reuses the same bucket.
