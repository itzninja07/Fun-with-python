# Import QRCode from pyqrcode 
import pyqrcode 
from pyqrcode import QRCode 


# String which represent the QR code 
s = "www.github.com/vishal7448"

# Generate QR code 
url = pyqrcode.create(s) 

# Create and save the png file naming "myqr.png" 
url.svg("myqr.svg", scale = 8) 

