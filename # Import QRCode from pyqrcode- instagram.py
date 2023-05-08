# Import QRCode from pyqrcode
import pyqrcode
import png
from pyqrcode import QRCode


# String which represents the QR code
s = "www.instagram.com/_akshaya_renu/"

# Generate QR code
url = pyqrcode.create(s)

# Create and save the svg file naming "myqr.svg"
url.svg("myqr.svg", scale = 15)

# Create and save the png file naming "myqr.png"
url.png('myqr.png', scale = 7)