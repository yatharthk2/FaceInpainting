import cv2
import os
import natsort 

image_folder = '../snapshots/default/images_100k/'
video_name = 'video.avi'

images = [img for img in os.listdir(image_folder) if img.endswith(".jpg")]
# print(sorted(images, key=int))
images = natsort.natsorted(images,reverse=False)
frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = frame.shape

video = cv2.VideoWriter(video_name, 0, 60, (width,height))
count = 0
for image in images:
    if count % 10 == 0:
        video.write(cv2.imread(os.path.join(image_folder, image)))

    count += 1

cv2.destroyAllWindows()
video.release()