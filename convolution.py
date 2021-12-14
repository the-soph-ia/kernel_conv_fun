from PIL import Image
import numpy as np

# Change image here! 
img = Image.open('rivers.jpg')
bw = img.convert('L')
mat1 = np.asarray(bw)

# Horizontal Edge Detector
kernel = np.array([[1, 2, 1],
                   [0, 0, 0],
                   [-1, -2, -1]])

new_img = np.zeros([mat1.shape[0], mat1.shape[1]])

for y in range(new_img.shape[0]-kernel.shape[0]+1):
    for x in range(new_img.shape[1]-kernel.shape[1]+1):
        new_img[y+1][x+1] = np.sum((kernel)*np.asarray([[mat1[y][x],mat1[y][x+1],mat1[y][x+2]],[mat1[y+1][x],mat1[y+1][x+1],mat1[y+1][x+2]],[mat1[y+2][x],mat1[y+2][x+1],mat1[y+1][x+2]]]))

print(np.asarray(new_img//1))

filtered = Image.fromarray(new_img)

bw.show(title="Original")
filtered.show(title="Filtered")
