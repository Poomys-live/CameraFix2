import cv2 as cv #อิมพอตopencv-python
import requests #อิมพอตrequests 

camera = cv.VideoCapture(0) #Cameraของเรา
url = 'https://notify-api.line.me/api/notify'#ลิ้งไลน์เรา
token = 'hGiaE2lAQ5N8aO3L5FAPhSnj5jN28JLnSvTUBCPS7iM'#Tokenไลน์เรา
headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Authorization': 'Bearer ' + token #เพื่อระบุว่า token คืออะไร
}