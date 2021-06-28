import dropbox
class TransferData:
    def __init__(self, accessToken):
        self.accessToken=accessToken
    def upload_file(self, file_from, file_to):
        dbx=dropbox.Dropbox(self.accessToken)

        with open(file_from,'rb') as f:
            dbx.files_upload(f.read(),file_to)

def main():
    accessToken='4798EHQdWdYAAAAAAAAAAW26qTttHI-f1hiC36ZyevZWfhcu4N2lqbEdvwKpEeau'
    transferData=TransferData(accessToken)
    file_from=input("Enter file path: ")
    file_to=input("Enter the dropbox path: ")
    transferData.upload_file(file_from, file_to)
    print("file has been moved")
if __name__== '__main__':
    main()