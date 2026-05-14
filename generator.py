#qr code
#simple appraoch


import qrcode


#img = qrcode.make(input("Enter the text or URL: ").strip())


#img.save(input("Enter the filename: ").strip())


#we need to strip to get rid of white space


#video way -custom qr code 
data = input('Enter the text or URL: ').strip()
filename = input('Enter the filename: ').strip()
qr = qrcode.QRCode(box_size = 10, border = 4)
qr.add_data(data)
image = qr.make_image(fill_color = 'black' , back_color = 'white')
image.save(filename)
print(f' QR code saved as')