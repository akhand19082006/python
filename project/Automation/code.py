import cv2
import time
import random
import dropbox
startTime = time.time()
def snapshot():
    number=random.randint(1,100)
    videocaptureobject=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame=videocaptureobject.read()
        print(ret)
        imageName="img"+str(number)+".jpg"
        cv2.imwrite(imageName,frame)
        startTime=time.time()
        result=False
    return imageName
    videocaptureobject.release()
    cv2.destroyAllWindows()
def upload_file(imageName):
        accessToken='4798EHQdWdYAAAAAAAAAAW26qTttHI-f1hiC36ZyevZWfhcu4N2lqbEdvwKpEeau'
        file=imageName
        file_from=file
        file_to="/Pictures/"+(imageName)
        dbx=dropbox.Dropbox(accessToken)
        with open(file_from,'rb') as f:
            dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)
            print("file uploaded")
def main():
    while(True):
        if((time.time()-startTime) >=5):
            name=snapshot()
            upload_file(name)
main()
