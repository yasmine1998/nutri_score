from django.shortcuts import render, redirect
from imutils.video import VideoStream
from pyzbar import pyzbar
import argparse
import datetime
import imutils
import time
import cv2
import openfoodfacts as food

def welcome(request):
    return render (request, 'scan/welcome.html')

def nutri_code(request):
    return render (request, 'scan/nutri_code.html')

def scan(request):
    vs = VideoStream(src=0).start()
    barcodeData = ""
    while True:
        frame = vs.read()
        frame = imutils.resize(frame, width=400)
        barcodes = pyzbar.decode(frame)
        for barcode in barcodes:
            (x, y, w, h) = barcode.rect
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            barcodeData = barcode.data.decode("utf-8")
            cv2.putText(frame, barcodeData, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        cv2.imshow("code scanner", frame)
        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            break
    products = food.get_product("6191507220214")
    if products["status"]==0:
        product_name = 'no name'
        brands_tag = 'no brand'
        image = "No image to display"
        nutriments = 'no nutriments'
        nova = 'None'
        fat = 0
        fruits = 0
        sugars = 0
        energy = 0
        sod = 0
        proteins = 0
        sucres = 0
        energie = 0
        fruitleg = 0
        graisse = 0
        sodium = 0
        proteines = 0
        fibres = 0
        fibers = 0
    else :
        product = products['product']
        try:
            nutriments = product['nutriments']
        except:
            nutriments = 'no nutriments'
        try:
            product_name = product['product_name']
        except:
            product_name = 'no name'
        try:
            brands_tag = product['brands_tags']
        except:
            brands_tag = 'no brand'
        try:
            nova = nutriments['nova-group']
        except:
            nova = 'None'
        try:
            fat = float(nutriments['saturated-fat'])
        except:
            fat = 0
        try:
            sod = float(nutriments['sodium'])
        except:
            sod = 0
        try:
            fruits = float(nutriments['fruits-vegetables-nuts-estimate-from-ingredients_100g'])
        except:
            fruits = 0
        try:
            sugars = float(nutriments['sugars'])
        except:
            sugars = 0
        try:
            energy = float(nutriments['energy'])
        except:
            energy = 0
        try:
            proteins = float(nutriments['proteins'])
        except:
            proteins = 0
        try:
            fibers = float(nutriments['fibers'])
        except:
            fibers = 0
        try :
            image = product['selected_images']['front']['display']
            image= list(image.values())[0]
        except :
            image = 'No image to display'
    if (("lait" or "eau" or "water" or "milk" or "boisson" or "jus" ) in product_name.lower()):
        if (sugars <= 4.5):
            sucres = 0
        elif (9 >= sugars > 4.5):
            sucres = 1
        elif (13.5 >= sugars > 9):
            sucres = 2
        elif (18 >= sugars > 13.5):
            sucres = 3
        elif (22.5 >= sugars > 18):
            sucres = 4
        elif (27 >= sugars > 22.5):
            sucres = 5
        elif (31 >= sugars > 27):
            sucres = 6
        elif (36 >= sugars > 31):
            sucres = 7
        elif (40 >= sugars > 36):
            sucres = 8
        elif (45 >= sugars > 40):
            sucres = 9
        else:
            sucres = 10
        if (energy <= 0):
            energie = 0
        elif (30 >= energy > 0):
            energie = 1
        elif (60 >= energy > 30):
            energie = 2
        elif (90 >= energy > 60):
            energie = 3
        elif (120 >= energy > 90):
            energie = 4
        elif (150 >= energy > 120):
            energie = 5
        elif (180 >= energy > 150):
            energie = 6
        elif (210 >= energy > 180):
            energie = 7
        elif (240 >= energy > 210):
            energie = 8
        elif (270 >= energy > 240):
            energie = 9
        else:
            energie = 10
        if (fruits <= 40):
            fruitleg = 0
        elif (60 >= fruits > 40):
            fruitleg = 2
        elif (80 >= fruits > 60):
            fruitleg = 4
        else:
            fruitleg = 10
    else:
        if (sugars <= 0):
            sucres = 0
        elif (1.5 >= sugars > 0):
            sucres = 1
        elif (3 >= sugars > 1.5):
            sucres = 2
        elif (4.5 >= sugars > 3):
            sucres = 3
        elif (6 >= sugars > 4.5):
            sucres = 4
        elif (7.5 >= sugars > 6):
            sucres = 5
        elif (9 >= sugars > 7.5):
            sucres = 6
        elif (10.5 >= sugars > 9):
            sucres = 7
        elif (12 >= sugars > 10.5):
            sucres = 8
        elif (13.5 >= sugars > 12):
            sucres = 9
        else:
            sucres = 10
        if (energy <= 335):
            energie = 0
        elif (670 >= energy > 335):
            energie = 1
        elif (1005 >= energy > 670):
            energie = 2
        elif (1340 >= energy > 1005):
            energie = 3
        elif (1675 >= energy > 1340):
            energie = 4
        elif (2010 >= energy > 1675):
            energie = 5
        elif (2345 >= energy > 2010):
            energie = 6
        elif (2680 >= energy > 2345):
            energie = 7
        elif (3015 >= energy > 2680):
            energie = 8
        elif (3350 >= energy > 3015):
            energie = 9
        else:
            energie = 10
        if (fruits <= 40):
            fruitleg = 0
        elif (60 >= fruits > 40):
            fruitleg = 1
        elif (80 >= fruits > 60):
            fruitleg = 2
        else:
            fruitleg = 5
    if (fat <= 1):
        graisse = 0
    elif (2 >= fat > 1):
        graisse = 1
    elif (3 >= fat > 2):
        graisse = 2
    elif (4 >= fat > 3):
        graisse = 3
    elif (5 >= fat > 4):
        graisse = 4
    elif (6 >= fat > 5):
        graisse = 5
    elif (7 >= fat > 6):
        graisse = 6
    elif (8 >= fat > 7):
        graisse = 7
    elif (9 >= fat > 8):
        graisse = 8
    elif (10 >= fat > 9):
        graisse = 9
    else:
        graisse = 10
    if (sod <= 0.09):
        sodium = 0
    elif (0.18 >= sod > 0.09):
        sodium = 1
    elif (0.27 >= sod > 0.18):
        sodium = 2
    elif (0.36 >= sod > 0.27):
        sodium = 3
    elif (0.45 >= sod > 0.36):
        sodium = 4
    elif (0.54 >= sod > 0.45):
        sodium = 5
    elif (0.63 >= sod > 0.54):
        sodium = 6
    elif (0.72 >= sod > 0.63):
        sodium = 7
    elif (0.81 >= sod > 0.72):
        sodium = 8
    elif (0.9 >= sod > 0.81):
        sodium = 9
    else:
        sodium = 10
    if (proteins <= 1.6):
        proteines = 0
    elif (3.2 >= proteins > 1.6):
        proteines = 1
    elif (4.8 >= proteins > 3.2):
        proteines = 2
    elif (6.4 >= proteins > 4.8):
        proteines = 3
    elif (8 >= proteins > 6.4):
        proteines = 4
    else:
        proteines = 5
    if (fibers <= 0.7):
        fibres = 0
    elif (1.4 >= fibers > 0.7):
        fibres = 1
    elif (2.1 >= fibers > 1.4):
        fibres = 2
    elif (2.8 >= fibers > 2.1):
        fibres = 3
    elif (3.5 >= fibers > 2.8):
        fibres = 4
    else:
        fibres = 5
    n = sucres + energie + graisse + sodium
    if (n >= 11):
        if (fruitleg == 5):
            s = n - (fruitleg + proteines + fibres)
        else:
            s = n - (fruitleg + fibres)
    else:
        s = n - (fruitleg + proteines + fibres)
    cv2.destroyAllWindows()
    vs.stop()
    return render (request, 'scan/nutri_code.html', {'products':products,'image':image, 'nova':nova,'product_name':product_name,'brands_tag':brands_tag,'nutriments':nutriments,'fat':fat,'fruits':fruits,'sucres':sucres,'energie':energie,'fruitleg':fruitleg,'graisse':graisse,'sodium':sodium,'proteines':proteines,'fibres':fibres,'s':s})
