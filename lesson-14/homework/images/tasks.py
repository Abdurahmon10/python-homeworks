from PIL import Image
import random
import numpy as np
import os

img=Image.open("birds.jpg","r")
img_arr=np.array(img)

#1

flipped_vertically=np.array(img_arr[::-1])

flipped_y_image=Image.fromarray(flipped_vertically,mode="RGB")
flipped_y_image.save("flipped_y_birds.jpg")

flipped_horizontally=np.array(img_arr[:,::-1])

flipped_x_image=Image.fromarray(flipped_horizontally,mode="RGB")
flipped_x_image.save("flipped_x_birds.jpg")

#2
noise=np.random.randint(0,50,img_arr.shape)

noisy_arr=img_arr+noise
noisy_arr=np.clip(noisy_arr,0,255)
noisy_arr=noisy_arr.astype(np.uint8)
noisy_image=Image.fromarray(noisy_arr,mode=img.mode)
noisy_image.save("noisy_image.jpg")

#3

brighter=np.array([[[1,0,0] for i in range(720)] for j in range(720)])
brighter_arr=img_arr+brighter
brighter_arr=np.clip(brighter_arr,0,255)
brighter_img=Image.fromarray(brighter_arr,mode=img.mode)
brighter_img.save("brighter_red.jpg")


#4
new_arr=np.array([[ img_arr[i,j] if ((i<310 or i>410) and (j<310 or j>410)) else [0,0,0] for j in range(img_arr.shape[1])] for i in range(img_arr.shape[0])])
new_img=Image.fromarray(new_arr,mode=img.mode)
print(new_img)
new_img.save("masked.jpg")