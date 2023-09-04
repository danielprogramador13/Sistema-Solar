import cv2

img = cv2.imread("solar-system.jpg")

#Texto do sol
cv2.putText(img,"Sol",(100,80),cv2.FONT_HERSHEY_COMPLEX,2,(0,196,255))

#Texto de mercurio
cv2.putText(img,"Mercurio",(125,190),cv2.FONT_HERSHEY_COMPLEX,0.3,(128,128,128))

#Texto de vênus
cv2.putText(img,"Venus",(195,175),cv2.FONT_HERSHEY_COMPLEX,0.4,(0,119,255))

#Texto de terra
cv2.putText(img,"Terra",(290,165),cv2.FONT_HERSHEY_COMPLEX,0.4,(255,144,30))

#Texto de Marte
cv2.putText(img,"Marte", (380,170), cv2.FONT_HERSHEY_COMPLEX,0.4, (0,0,255))

#Texto de Júpiter
cv2.putText(img,"Jupiter", (560,60), cv2.FONT_HERSHEY_COMPLEX,0.8, (119,197,255))

#Texto de Saturno
cv2.putText(img,"Saturno", (760, 100), cv2.FONT_HERSHEY_COMPLEX,0.8, (119,197,255))

#Texto de Urano
cv2.putText(img,"Urano", (955, 110), cv2.FONT_HERSHEY_COMPLEX,0.8, (255,255,0))

#Texto de Netuno
cv2.putText(img,"Netuno", (1100, 110), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,0,0))

cv2.imshow("Planetas e seus nomes", img)

cv2.imwrite("solar-system.png", img)

cv2.waitKey(0)