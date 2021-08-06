import cv2
from Clase import basicColor as bs

dir = input("Ingrese la dirección de su imagen: ")
nom = input("Ingrese el nombre de su imagen: ")
imagen = bs(dir, nom)

imagen.displayProperties()

Ibw_otsu = imagen.makeBW()
cv2.imshow("Image", Ibw_otsu)
cv2.waitKey(0)

h = int(input("Ingrese un valor de h entre 0 y 179: "))
print(h)
image_hue_bgr = imagen.colorize(h)
cv2.imshow("Image", image_hue_bgr)
cv2.waitKey(0)



