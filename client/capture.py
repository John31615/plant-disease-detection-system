import cv2
import base64
import requests

API_URL = "http://localhost:5000/api/crop-images"

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

ret, frame = cap.read()
cap.release()

if not ret:
    print("Failed to capture image")
    exit()

_, buffer = cv2.imencode(".jpg", frame)
img_base64 = base64.b64encode(buffer).decode("utf-8")

data = {
    "plantingId": 1,
    "deviceId": 1,
    "image": img_base64
}

response = requests.post(API_URL, json=data)

print(response.status_code, response.text)
