import dropbox
import os
from dropbox.files import WriteMode
class Transfer_data:
    def __init__(self,access_token):
        self.access_token=access_token
    
    def uploadFile(self,files_from,file_to):
        dbx=dropbox.Dropbox(self.access_token)
        for root,dirs,files in os.walk(files_from):
            for file_name in files:
                local_path=os.path.join(root,file_name)
                relative_path=os.path.relpath(local_path,files_from)
                dropbox_path=os.path.join(file_to,relative_path)

                f=open(local_path,'rb')
                dbx.files_upload(f.read(),dropbox_path,mode=WriteMode('overwrite'))

def main():
    access_token='FJTSY5-9ryEAAAAAAAAAAXbYr_p8YlTFKVbTxW6ZZxcwLjli1IP3mgR2NKqcsRef'
    storage=Transfer_data(access_token)
    files_from=input('ENTER THE FILE TO TRANSFER')
    file_to=input('ENTER THE PATH TO UPLOAD IN DROPBOX')
    storage.uploadFile(files_from,file_to)
    print('THE FILE HAS BEEN MOVED')

main()