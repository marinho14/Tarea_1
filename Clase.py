#Importar los paquetes necesarios
import cv2
import numpy as np
import os

# Definición de la clase
class basicColor: # Se crea la clase Basic Color

  def __init__(self, path, image_name):
    path_file = os.path.join(path, image_name)
    self.image = cv2.imread(path_file)

  def displayProperties(self):
    carac = self.image.shape
    Pix   = carac[0] * carac[1]
    cana  = carac[2]
    print("El numero de MP es: " + str(Pix/1000000) + "\n" + "El numero de canales es: " + str(cana))

  def makeBW(self):
    image_gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
    ret, Ibw_otsu = cv2.threshold(image_gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return Ibw_otsu

  def colorize(self,h1):
      if(h1>179 or h1<0):
          print("El valor debe estar entre 0 y 179")
      else:
          image_hsv = cv2.cvtColor(self.image, cv2.COLOR_BGR2HSV)
          h, s, v = cv2.split(image_hsv)
          h = h1 * np.ones_like(s)
          image_hue = cv2.merge((h, s, v))
          image_hue_bgr = cv2.cvtColor(image_hue, cv2.COLOR_HSV2BGR)
          return image_hue_bgr



