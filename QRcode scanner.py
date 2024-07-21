# qrcode scanner
import qrcode

myqr = qrcode.make("https://www.youtube.com/@Wyco_Nomad")
myqr.save("myqr.png")