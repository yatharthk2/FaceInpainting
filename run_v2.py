import argparse
import torch
from torchvision import transforms
import numpy as np
import cv2 as cv
import sys
#python run.py --photo D:\trash\mountain.jpg


import opt
from places2 import Places2
from evaluation import evaluate
from net import PConvUNet
from util.io import load_ckpt

parser = argparse.ArgumentParser()
# training options
parser.add_argument('--root', type=str, default='./data')
parser.add_argument('--snapshot', type=str, default=r"../snapshots/default/ckpt/345000.pth")
parser.add_argument('--image_size', type=int, default=256)
parser.add_argument('--photo', type=str, default='./xyz')

args = parser.parse_args()

# OpenCV Utility Class for Mouse Handling
class Sketcher:
    def __init__(self, windowname, dests, colors_func):
        self.prev_pt = None
        self.windowname = windowname
        self.dests = dests
        self.colors_func = colors_func
        self.dirty = False
        self.show()
        cv.setMouseCallback(self.windowname, self.on_mouse)

    def show(self):
        cv.imshow(self.windowname, self.dests[0])
        cv.imshow(self.windowname + ": mask", self.dests[1])

    # onMouse function for Mouse Handling
    def on_mouse(self, event, x, y, flags, param):
        pt = (x, y)
        if event == cv.EVENT_LBUTTONDOWN:
            self.prev_pt = pt
        elif event == cv.EVENT_LBUTTONUP:
            self.prev_pt = None

        if self.prev_pt and flags & cv.EVENT_FLAG_LBUTTON:
            for dst, color in zip(self.dests, self.colors_func()):
                cv.line(dst, self.prev_pt, pt, color, 5)
            self.dirty = True
            self.prev_pt = pt
            self.show()


def main():

    print("Usage: python run.py")
    print("Keys: ")
    print("t - inpaint using FMM")
    print("n - inpaint using NS technique")
    print("r - reset the inpainting mask")
    print("ESC - exit")

    # Read image in color mode
    img = cv.imread(args.photo, cv.IMREAD_COLOR)

    # If image is not read properly, return error
    if img is None:
        print('Failed to load image file: {}'.format(args["image"]))
        return

    # Create a copy of original image
    img_mask = img.copy()
    # Create a black copy of original image
    # Acts as a mask
    inpaintMask = np.zeros(img.shape[:2], np.uint8)
    # Create sketch using OpenCV Utility Class: Sketcher
    sketch = Sketcher('image', [img_mask, inpaintMask], lambda : ((255, 255, 255), 255))
    

    #img = sketch
    #img = img.save("sketch.jpeg")

    while True:
        ch = cv.waitKey()
        if ch == 27:
            break
        if ch == ord('s'):
            
            filename1 = './data/val_large/Mask_Image.jpg'
            filename2 = './data/mask_root/Inverted_Inpaint_Image.jpg'
            cv.imwrite(filename1, img)
            cv.imwrite(filename2, (cv.bitwise_not(inpaintMask)))
            print('Masked image saved in data')
            device = torch.device('cuda')

            size = (args.image_size, args.image_size)
            img_transform = transforms.Compose(
                [transforms.Resize(size=size), transforms.ToTensor(),
                transforms.Normalize(mean=opt.MEAN, std=opt.STD)])
            mask_transform = transforms.Compose(
                [transforms.Resize(size=size), transforms.ToTensor()])

            dataset_val = Places2(args.root,"./data/mask_root/", img_transform, mask_transform, 'val')

            model = PConvUNet().to(device)
            load_ckpt(args.snapshot, [('model', model)])
            print('output is saved in result.jpg')

            model.eval()
            evaluate(model, dataset_val, device, 'result 2.jpg')
            break



if __name__ == '__main__':
    main()
    cv.destroyAllWindows()



        



