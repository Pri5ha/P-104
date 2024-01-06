import cv2

img = cv2.imread("solar-system.jpg")

cv2.putText(img,
            "Sun",
            (20,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255))

cv2.putText(img,
            "Mercury",
            (120,180),
            cv2.FONT_HERSHEY_COMPLEX_SMALL,
            0.5,
            (255,255,255))

cv2.putText(img,
            "Venus",
            (197,260),
            cv2.FONT_HERSHEY_COMPLEX_SMALL,
            0.5,
            (255,255,255))

cv2.putText(img,
            "Earth",
            (295,263),
            cv2.FONT_HERSHEY_COMPLEX_SMALL,
            0.5,
            (255,255,255))

cv2.putText(img,
            "Mars",
            (390,250),
            cv2.FONT_HERSHEY_COMPLEX_SMALL,
            0.5,
            (255,255,255))

cv2.putText(img,
            "Jupiter",
            (600,100),
            cv2.FONT_HERSHEY_COMPLEX_SMALL,
            0.5,
            (255,255,255))

cv2.putText(img,
            "Saturn",
            (800,150),
            cv2.FONT_HERSHEY_COMPLEX_SMALL,
            0.5,
            (255,255,255))

cv2.putText(img,
            "Uranus",
            (975,145),
            cv2.FONT_HERSHEY_COMPLEX_SMALL,
            0.5,
            (255,255,255))

cv2.putText(img,
            "Neptune",
            (1120,280),
            cv2.FONT_HERSHEY_COMPLEX_SMALL,
            0.5,
            (255,255,255))

cv2.imwrite("Solar_systemwithname.jpg",img)

cv2.imshow("output", img)
cv2.waitKey(0)