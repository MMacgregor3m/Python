# qrcode scanner
import qrcode

myqr = qrcode.make("https://www.blackoutcoffee.com?p=SJpQ-nbLh")
myqr.save("Blackout.png")