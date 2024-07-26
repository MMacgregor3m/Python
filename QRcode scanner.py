# qrcode scanner
import qrcode

myqr = qrcode.make("https://jasemedical.com/?rstr=14870")
myqr.save("jace.png")