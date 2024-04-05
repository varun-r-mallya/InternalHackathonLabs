import cv2

filename = "MUOQRCode.png"

image = cv2.imread(filename)

detector = cv2.QRCodeDetector()

data, vertices_array, binary_qrcode = detector.detectAndDecode(image)

if vertices_array is not None:
  print("QRCode data:")
  print(data)
  for i in data:
      print(hex(ord(i)))
else:
  print("There was some error")