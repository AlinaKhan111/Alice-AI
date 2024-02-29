import cv2
import numpy as np
import HandTrackingModule as htm
import time
import pyautogui as p
import os

######################
wCam, hCam = 640, 480
frameR = 100     #Frame Reduction
smoothening = 7  #random value
######################

pTime = 0
plocX, plocY = 0, 0
clocX, clocY = 0, 0
cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

detector = htm.handDetector(maxHands=1)
wScr, hScr = p.size()

# print(wScr, hScr)

while True:
    # Step1: Find the landmarks
    success, img = cap.read()
    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img)

    # Step2: Get the tip of the index and middle finger
    if len(lmList) != 0:
        x1, y1 = lmList[8][1:]
        x2, y2 = lmList[12][1:]

        px1,py1 = lmList[8][1],lmList[8][2]
        px2,py2 = lmList[6][1],lmList[6][2]
        # print(px1,py1)

        # Step3: Check which fingers are up
        fingers = detector.fingersUp()
        cv2.rectangle(img, (frameR, frameR), (wCam - frameR, hCam - frameR),
                      (255, 0, 255), 2)


        # Step4: Only Index Finger: Moving Mode
        if fingers[1] == 1 and fingers[2] == 0:

            # Step5: Convert the coordinates
            x3 = np.interp(x1, (frameR, wCam-frameR), (0, wScr))
            y3 = np.interp(y1, (frameR, hCam-frameR), (0, hScr))

            # Step6: Smooth Values
            clocX = plocX + (x3 - plocX) / smoothening
            clocY = plocY + (y3 - plocY) / smoothening

            # Step7: Move Mouse
            p.moveTo(wScr - clocX, clocY)
            cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
            plocX, plocY = clocX, clocY

        # if fingers


        if fingers[1] == 1 and fingers[2] == 1 and fingers[0]==0 and fingers[3]==0 and fingers[4]==0:

            # Step9: Find distance between fingers
            length, img, lineInfo = detector.findDistance(8, 12, img)

            # Step10: Click mouse if distance short
            if length < 40:
                cv2.circle(img, (px1,py1), 15, (0, 255, 0), cv2.FILLED)
                cv2.circle(img, (px2,py2), 15, (0, 255, 0), cv2.FILLED)
                p.click()

        if fingers[4]==1 and fingers[0]==0 and fingers[1]==1 and fingers[2]==0 and fingers[3]==0:
            p.rightClick()

        # if fingers[4]==1 and fingers[0]==0 and fingers[1]==0 and fingers[2]==0 and fingers[3]==0:
        #     # p.press('win')
        #     # p.typewrite("on screen keyboard")
        #     # p.press("enter")
        #     os.startfile("C:\\Users\\Metro\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Accessibility\\On-Screen Keyboard.lnk")

        #Thumb up: Hold mode
        if fingers[4]==0 and fingers[0]==1 and fingers[1]==0 and fingers[2]==0 and fingers[3]==0:
            x3 = np.interp(x1, (frameR, wCam-frameR), (0, wScr))
            y3 = np.interp(y1, (frameR, hCam-frameR), (0, hScr))

            # Step6: Smooth Values
            clocX = plocX + (x3 - plocX) / smoothening
            clocY = plocY + (y3 - plocY) / smoothening

            # Step7: Move Mouse
            p.dragTo(wScr - clocX, clocY)

        if fingers[4]==0 and fingers[0]==0 and fingers[1]==0 and fingers[2]==0 and fingers[3]==0:
            length, img, lineInfo = detector.findDistance(8, 12, img)

            if length < 40:
                p.scroll(-100)

        if fingers[4]==1 and fingers[1]==1 and fingers[1]==1 and fingers[2]==1 and fingers[3]==1:
            p.scroll(100)





    # Step11: Frame rate
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (28, 58), cv2.FONT_HERSHEY_PLAIN, 3, (255, 8, 8), 3)

    # Step12: Display
    cv2.imshow("Image", img)
    cv2.waitKey(1)