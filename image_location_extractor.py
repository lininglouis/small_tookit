'''
before run the code, install three following library
pip install gpsphoto
pip install piexif
pip install exifread 
'''


from GPSPhoto import gpsphoto
from PIL import Image
from glob import glob


 
for imgPath in glob(r'./images_dir/*.jpg'):
    data = gpsphoto.getGPSData(imgPath)
    lat = data['Latitude']
    lng = data['Longitude']
    print(lat, lng)