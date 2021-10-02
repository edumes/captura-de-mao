import cv2
from cvzone.HandTrackingModule import HandDetector

#definindo a captura
captura = cv2.VideoCapture(0)

#resolução
captura.set(3, 900)
captura.set(4, 600)

#detetor de mãos e seus parametros
detector = HandDetector(detectionCon=0.8, maxHands=1)

#execução
while True:
    success, img = captura.read() 
    img = detector.findHands(img) #achar mãos
    lmList, bboxInfo = detector.findPosition(img) #achar posição
    cv2.imshow("Detector de mão", img) #titulo da janela
    cv2.waitKey(1)
    

 




