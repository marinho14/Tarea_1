#Importar los paquetes necesarios
import cv2
import numpy as np
import os

# Definición de la clase
class basicColor: # Se crea la clase Basic Color

  def __init__(self, path, image_name):
    path_file = os.path.join(path, image_name)
    self.image = cv2.imread(path_file)

  def displayProperties(self): # Se crea el metodo display properties
    carac = self.image.shape  # Se usa el comando shape para encontrar las caracterisiticas de la imagen
    Pix   = carac[0] * carac[1]  ## Se encuentra el número de pixeles
    cana  = carac[2]             # Se define el numero de canales
    print("El numero de MP es: " + str(Pix/1000000) + "\n" + "El numero de canales es: " + str(cana))  # Se imprimen las caracteristicas

  def makeBW(self):   ##  Se crea el metodo BW
    image_gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)  # La imagen se transforma a grises
    ret, Ibw_otsu = cv2.threshold(image_gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)  ## Se usa el metodo Otsu
    return Ibw_otsu  ## Se retorna la imagen

  def colorize(self,h1):
    if(h1>179 or h1<0): ## se pregunta si h esta dentro de lo establecido
        print("El valor debe estar entre 0 y 179")
    else:
        image_hsv = cv2.cvtColor(self.image, cv2.COLOR_BGR2HSV) # Se transforma la imagen a HSV
        h, s, v = cv2.split(image_hsv) # Se encuentran los parametros
        h = h1 * np.ones_like(s)       # Se define el nuevo h
        image_hue = cv2.merge((h, s, v)) # s y v se dejan igual, cambia h
        image_hue_bgr = cv2.cvtColor(image_hue, cv2.COLOR_HSV2BGR) # Se transforma la imagen a BGR
        return image_hue_bgr # Se retorna la imagen colorizada



