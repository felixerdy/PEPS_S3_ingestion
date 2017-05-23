import zipfile
import os
import folderToS3
import auth
import shutil

def extract(zipFilepath):
    zip_ref = zipfile.ZipFile(zipFilepath, 'r')
    # extract zip file to current folder
    zip_ref.extractall("./")
    zip_ref.close()
    os.remove(zipFilepath)

    withSafePath = zipFilepath.split(".zip")[0] + ".SAFE"
    return withSafePath.split("./")[1]

def uploadToS3(folderPath):
    print "uploading %s to %s" % (folderPath, auth.AWS_S3_BUCKET_NAME)
    os.system("aws s3 sync %s s3://%s/%s" % (folderPath, auth.AWS_S3_BUCKET_NAME, folderPath))
    shutil.rmtree(folderPath)
    print "delete folder..."

def beamMeUpScotty(zipFilepath):
    folderPath = extract(zipFilepath)
    uploadToS3(folderPath)
