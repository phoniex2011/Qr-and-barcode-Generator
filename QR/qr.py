import pyqrcode
from barcode import EAN13

pure_red = "\033[0;31m"
yellow = "\033[0;93m"


print(yellow + 'type help to list commands \n')
print("verison 1.0")

while True:
    command = input('').strip()
    if command == 'help':
        print('create-qr: to create a qr code \n')
        print('create-bc: to create a barcode  ') 
        

    elif  command == "create-qr":
        url = input('https://'  + 'enter url here '   + yellow + '("https:// is alredy added.)" ' )
        file = input('enter file name here: ')
        qr = pyqrcode.create(url)
        qr.svg(file + '.svg', scale = 8)

    elif command == "create-bc":
        number = input(yellow + 'enter string here(only numbers are allowed and code length must be 12 numbers)')
        code = EAN13(number)
        code.save("barcode")

 

    else :
        print(pure_red + 'error(invalid command)')


        
