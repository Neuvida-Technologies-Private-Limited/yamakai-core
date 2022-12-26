import boto3


s3 = boto3.resource(
    service_name='s3')
import boto3
import os


def upload_files(path):
    session = boto3.Session(
    region_name='us-east-1',
    aws_access_key_id='AKIAQGBZASKSU2FI5XYF',
    aws_secret_access_key='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')
    s3 = session.resource('s3')
    bucket = s3.Bucket('paraphrasing-models')

    for subdir, dirs, files in os.walk(path):
        for file in files:
            full_path = os.path.join(subdir, file)
            with open(full_path, 'rb') as data:
                bucket.put_object(Key=full_path[len(path) + 1:], Body=data)


if __name__ == "__main__":
    upload_files('OPT_Paraphraser/pushkar_OPT_paraphaser')