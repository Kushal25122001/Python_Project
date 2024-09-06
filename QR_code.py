import qrcode as qr
img = qr.make("https://www.youtube.com/watch?v=TGpG56pg3UU")

img.save("song.png")
