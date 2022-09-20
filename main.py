#  for all images in a folder convert the ratio to 2:3


import os
from PIL import Image
import datetime

date = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
files = os.listdir('.')


# create a guide for the user
print('This script will convert all images in the current folder to a 2:3 ratio')
print(f'The new images will be saved in a new folder called "{date}"')
# ask the user if he wants to continue
answer = input('Do you want to continue? (y/n) ')
if answer == 'y':
    # create a new folder
    os.mkdir(date)
    # loop through all files in the current folder
    for file in files:
        # check if the file is an image
        if file.endswith('.jpg') or file.endswith('.png')or file.endswith('.PNG') or file.endswith('.JPG'):
            # open the image
            img = Image.open(file).convert('RGBA')
        



            # get the width and height of the image
            width, height = img.size
            # calculate the new height
            new_height = int(width * 3 / 2)
            # calculate the difference between the new height and the old height
            diff = int((height - new_height) / 2)
            #fill  space with white
            new_image = Image.new('RGBA', (width, new_height), (255, 255, 255, 255))
            # paste the image in the new image
            new_image.paste(img, (0, -diff))






            # crop the image
            img = img.crop((0, diff, width, height - diff))

            



            #change file to RGB
            #img = img.convert('RGB')
            new_image = new_image.convert('RGB')






            # save the image in the new folder
            new_image.save(f'{date}/{file}')












            # save image
            #img.save(f'{date}/{file}')
    print (f'All images have been converted and saved in the "{date}" folder')
elif len(files) == 0:
        print('There are no images in this folder')

elif answer == 'n':
    # create a guide for the user
    print('The script has been canceled')
#if there are no images in the folder  inform the user

else:
    print('Please restart the program and  enter a valid answer Y or N')

