################
# Varonis Task
################

#pip install pydrive
#pip install google_auth_oauthlib
#pip install pyzipper

import hashlib
from zipfile import ZipFile
from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth

ZIP_PATH = r'./Protected.zip'
ZIP_CONTENT_FILE_PATH = './task.py'
DriveFolderID = '1x-jl2QJm4PtuHeMeFXryivlRLnZptdGx'

def uploadFile(filepath):
	file = drive.CreateFile({'parents': [{'id': DriveFolderID}]})
	file.SetContentFile(filepath)
	file.Upload()
	return file


myZip = ZipFile(ZIP_PATH, 'w')
# Adds the desired file to the archive
myZip.write(ZIP_CONTENT_FILE_PATH)
myZip.close()

###########################

gauth = GoogleAuth()           
drive = GoogleDrive(gauth)

remoteZipFile = uploadFile(ZIP_PATH)

DOWNLOAD_PATH = "Downloaded_zip"
remoteZipFile.GetContentFile(DOWNLOAD_PATH)

###########################

with open(DOWNLOAD_PATH,"rb") as f:
    f_byte= f.read()
    sha = hashlib.sha256(f_byte)

SHA_FILE = "sha.txt"
with open(SHA_FILE, "w") as f:
    f.write(sha.hexdigest())

SHA_ZIP_FILE_PATH = "zipped_sha.zip"
shaZip = ZipFile(SHA_ZIP_FILE_PATH, 'w')
# Adds the desired file to the archive
shaZip.write(SHA_FILE)
shaZip.close()

uploadFile(SHA_ZIP_FILE_PATH)

###########################