import cv2
import random
import dropbox
import time
starttime = time.time()

def takesnapshot():
    number = random.randint(0, 100)

    #starts your webcam
    videocaptureobject = cv2.VideoCapture(0)
    result = True

    while(result):
        #reads the frame while camera is on
        ret, frame = videocaptureobject.read()
        imagename = "img"+str(number)+".png"
        cv2.imwrite(imagename, frame)
        starttime = time.time
        result = False

    return imagename

    print('Snapshot taken')

    videocaptureobject.release()
    cv2.destroyAllWindows()

def upload_file(imagename):
    accesstoken = 'S8YZN8SfkGEAAAAAAAAAARZ131qsHtEx_fj7q7MxkuJQPMCu5layUy97Qd6CDGai'

    source = imagename
    dest = '/images/'+imagename

    dbx = dropbox.Dropbox(accesstoken)
    with open(source, 'rb') as f:
        dbx.files_upload(f.read(), dest, mode=dropbox.files.WriteMode.overwrite)
        print('File uploaded')

def main():
    while(True):
        if ((time.time()-starttime)>=300):
            name = takesnapshot()
            upload_file(name)
            
main()