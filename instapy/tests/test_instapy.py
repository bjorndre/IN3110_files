from filters import *
from random import randint
import numpy as np
import cv2 as cv
from numba import jit

def test_grayscale():
    test_array = np.array([[[randint(0,255),randint(0,255),randint(0,255)] for i in range(3)] for j in range(2)])
    test_grayval = 0.07*test_array[:,:,0] + 0.72*test_array[:,:,1] + 0.21*test_array[:,:,2]
    cv.imwrite(f"test_image.jpeg", test_array)

    test_array[:,:,0] = test_array[:,:,1] = test_array[:,:,2] = test_grayval

    test_grayscale_python = grayscale_image("test_image.jpeg", "test_grayimage.jpeg")
    test_grayscale_numpy = grayscale_image("test_image.jpeg", "test_grayimage.jpeg", "numpy")
    test_grayscale_numba = grayscale_image("test_image.jpeg", "test_grayimage.jpeg", "numba")
    
    test_gray_array = test_array.astype("uint8")

    np.allclose(test_gray_array, test_grayscale_python)
    np.allclose(test_gray_array, test_grayscale_numpy)
    np.allclose(test_gray_array, test_grayscale_numba)

def test_sepia_image():
    test_array = np.array([[[randint(0,255),randint(0,255),randint(0,255)] for i in range(3)] for j in range(2)])
    cv.imwrite(f"test_image.jpeg", test_array)

    sepia_matrix = np.flip(np.array([[ 0.393, 0.769, 0.189] , [ 0.349, 0.686, 0.168] , [ 0.272, 0.534, 0.131]]))
    test_sepia = test_array.copy()
    test_sepia[:,:,0] = np.clip(sepia_matrix[0,0]*test_array[:,:,0] + sepia_matrix[0,1]*test_array[:,:,1] + \
        sepia_matrix[0,2]*test_array[:,:,2],None,255)
    test_sepia[:,:,1] = np.clip(sepia_matrix[1,0]*test_array[:,:,0] + sepia_matrix[1,1]*test_array[:,:,1] + \
        sepia_matrix[1,2]*test_array[:,:,2],None,255)
    test_sepia[:,:,2] = np.clip(sepia_matrix[2,0]*test_array[:,:,0] + sepia_matrix[2,1]*test_array[:,:,1] + \
        sepia_matrix[2,2]*test_array[:,:,2],None,255)

    test_sepia = test_sepia.astype("uint8")
    print(test_sepia)
    test_sepia_python = grayscale_image("test_image.jpeg", "test_sepiaimage.jpeg")
    test_sepia_numpy = grayscale_image("test_image.jpeg", "test_sepiaimage.jpeg", "numpy")
    test_sepia_numba = grayscale_image("test_image.jpeg", "test_sepiaimage.jpeg", "numba")
    np.allclose(test_sepia, test_sepia_python)
    np.allclose(test_sepia, test_sepia_numpy)
    np.allclose(test_sepia, test_sepia_numba)