import boto3
import os

class S3Connect:
    AWS_ACCESS_KEY_ID = 'AKIATPZLBFL5WKL5MSPX'
    AWS_SECRET_ACCESS_KEY = '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'

    def __init__(self):
        self.s3 = boto3.resource(
                service_name='s3',
                region_name='us-east-1',
                aws_access_key_id=self.AWS_ACCESS_KEY_ID,
                aws_secret_access_key=self.AWS_SECRET_ACCESS_KEY
        )
        self.s3 = boto3.resource('s3')
    
    def uploadFile(self, file_local, file_s3, BUCKET = "test-s3-ammper"):
        self.s3.Bucket(BUCKET).upload_file(file_local, file_s3)
        #os.remove(file_local)
    
    def uploadObject(self, object_data, file_s3, BUCKET = "test-s3-ammper"):
        object = self.s3.Object(BUCKET, file_s3)
        object.put(Body=object_data)
