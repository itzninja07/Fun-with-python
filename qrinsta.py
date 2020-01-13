# Import QRCode from pyqrcode 
import pyqrcode 
from pyqrcode import QRCode 


# String which represent the QR code 
s = "www.instagram.com/itz_mr_ninja07"

# Generate QR code 
url = pyqrcode.create(s) 

# Create and save the png file naming "myqr.png" 
url.svg("insta.svg", scale = 8) 

