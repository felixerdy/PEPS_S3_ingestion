# PEPS to S3 ingestion

## Installation
```
git clone ...
cd PEPS_S3_ingestion
```
#### AWS CLI
Please [install](http://docs.aws.amazon.com/cli/latest/userguide/installing.html) and [configure](http://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) the AWS CLI to be able to upload data to S3.
#### python
```
pip install -r requirements.txt
```

## Configuration
#### auth
Insert your AWS and PEPS credentials to `auth.py.example` and save it as `auth.py`. Also add the S3 bucket name where you want to save the data.

#### extend
In `extend.py` add the bounding box as well as the start and end date of the data you want to ingest.

## Run
```
python start.py
```

## Dependencies
`peps_download.py` taken from https://github.com/olivierhagolle
