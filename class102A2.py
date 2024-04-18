import cv2
import dropbox
import time
import random

start_time = time.time()

def take_snapshot():
    number = random.randint(0, 100)
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while result:
        ret, frame = videoCaptureObject.read()
        img_name = "img" + str(number) + ".png"
        cv2.imwrite(img_name, frame)
        result = False
    videoCaptureObject.release()
    cv2.destroyAllWindows()
    print("snapshot taken")  # Moved the print statement here
    return img_name

def upload_file(img_name):
    access_token ="sl.Bzj54QRo1XzyZJsPHco-mWlDL3Yql_w-r-OTHweYAIM8uUDSTi94AxAB-i8aQ1nA15dnrCFIdYAYLicJVPiAUyYIZk8RYTZLvRPcZ2SSl2eiUUl7Z1cZpiQR__9xPdb7sUiigqQeqmFp"
    file_from = img_name
    file_to = "/testFolder/" + img_name
    dbx = dropbox.Dropbox(access_token)

    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(), file_to, mode=dropbox.files.WriteMode.overwrite)
        print("file uploaded")

def main():
    global start_time  # Define start_time as global
    while True:
        if (time.time() - start_time) >= 5:
            name = take_snapshot()
            upload_file(name)
            start_time = time.time()  # Update start_time

main()