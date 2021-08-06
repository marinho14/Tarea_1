import cv2
from Clase import basicColor as bs ## Importar la clase del archivo clase.py

if __name__ == '__main__':
    ## Definicones de la ruta del archivo
    dir = input("Ingrese la dirección de su imagen: ")
    nom = input("Ingrese el nombre de su imagen: ")
    ## Llamdado de la clase
    imagen = bs(dir, nom)
    ## Se usa el metodo DisplayProperties para visualizar los pixeles y canales
    imagen.displayProperties()
    ## Se usa el metodo Otsu y se visualiza la imagen en blanco
    Ibw_otsu = imagen.makeBW()
    cv2.imshow("Image", Ibw_otsu)
    cv2.waitKey(0)
    ## Se define h y se usa el metodo colorize para ver la imagen colorizada
    h = int(input("Ingrese un valor de h entre 0 y 179: "))
    print(h)
    image_hue_bgr = imagen.colorize(h)
    cv2.imshow("Image", image_hue_bgr)
    cv2.waitKey(0)



