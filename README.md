# VaronisTask

README:

dependencies:
# pip install pydrive

open terminal from the python script path
make sure that in this directory, there is a file named "client_secrets.json", which includes the information for OAUTH in 
order to login to Google Drive. you can get this information from google cloud api console -> credentials -> download OAUTH client

in task.py:
there is a param DriveFolderID - the id of the folder in google Drive.
In order to get this id - go to the desired folder, and copy the entire last part of the url
example: the url of my folder is https://drive.google.com/drive/folders/1x-jl2QJm4PtuHeMeFXryivlRLnZptdGx, so the id is 1x-jl2QJm4PtuHeMeFXryivlRLnZptdGx
