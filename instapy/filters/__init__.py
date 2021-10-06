import numpy as np
import cv2 as cv
from numba import jit

def grayscale_image(in_file, out_file=None, implementation="python", scale=1.0):
    """
    Grayscales an image.
        
        Args:
            in_file (str): Name of the image to be grayscaled
            out_file (str): (Optional) The grayscaled image. 
                If no argument, returns image as modified in_file_grayscale.jpeg
            implementation (str): (Optional) The method to be used for applying the gray filter. 
                Uses python by default.
            scale (float): (Optional) Scaling factor for the image. default is 1.0

        Creates:
            out_file (file): The grayscaled image. Alternatively;
            in_file_grayscale (file): Grayscaled image if out_file is not given.

        Raises:
            ValueError: If in_file not a string.
            ValueError: If out_file is not None or a string.
            ValueError: If implementation is not a valid implementation method.

        Returns:
            gray_image (array): array of gray values.
    """
    if type(in_file) != str:
        raise ValueError("Name of input image must be a string")
    if type(out_file) != str and out_file != None:
        raise ValueError("Name of output image must be a string or None")
    
    image = cv.imread(in_file)
    image = cv.resize(image , (0, 0), fx=scale, fy=scale)
    gray_image = image.copy()
    
    if implementation == "python":
        for i in range(len(image)):
            for j in range(len(image[i])):
                gray = 0.07*image[i][j][0] +0.72*image[i][j][1] + 0.21*image[i][j][2]
                gray_image[i][j][0] = gray_image[i][j][1] = gray_image[i][j][2] = gray

    elif implementation == "numpy":
        gray = 0.07*image[:,:,0] + 0.72*image[:,:,1] + 0.21*image[:,:,2]
        gray_image[:,:,0] = gray; gray_image[:,:,1] = gray; gray_image[:,:,2] = gray

    elif implementation == "numba":
        @jit
        def graying(arr):
            "Function for the graying process."
            gray_arr = arr.copy()
            for i in range(len(arr)):
                for j in range(len(arr[i])):
                    gray = 0.07*arr[i][j][0] +0.72*arr[i][j][1] + 0.21*arr[i][j][2]
                    gray_arr[i][j][0] = gray_arr[i][j][1] = gray_arr[i][j][2] = gray
            return gray_arr
        gray_image = graying(image)

    else:
        raise ValueError("Not a valid implementation. Use python, numpy, or numba.")

    gray_image = gray_image.astype("uint8")
    if out_file == None:
        name = in_file.split(".")[0]
        cv.imwrite(f"{name}_grayscale.jpeg", gray_image)
    else:
        cv.imwrite(f"{out_file}", gray_image)
    
    return gray_image

def sepia_image(in_file, out_file=None, implementation="python", scale=1.0, level=1.0):
    """
    Applies a sepia filter to an image.
        
        Args:
            in_file (str): Name of the image to have the sepia filter applied
            out_file (str): (Optional) The image with sepia filter. 
                If no argument, returns image as modified in_file_sepia.jpeg
            implementation (str): (Optional) The method to be used for applying the sepia filter. 
                Uses python by default.
            scale (float): (Optional) Scaling factor for the image. default is 1.0
            level (float): (Optional) The level of sepia. default is 1.0

        Creates:
            out_file (file): The sepia image. Alternatively;
            in_file_grayscale (file): sepia image if out_file is not given.

        Raises:
            ValueError: If level is not in the interval [0,1].
            ValueError: If in_file not a string.
            ValueError: If out_file is not None or a string.
            ValueError: If implementation is not a valid implementation method.

        Returns:
            sepiafilter_image (array): array of sepia values values.
    """

    if level > 1.0 or level < 0:
        raise ValueError("level must be between 0 and 1")
    if type(in_file) != str:
        raise ValueError("Name of input image must be a string")
    if type(out_file) != str and out_file != None:
        raise ValueError("Name of output image must be a string or None")
    
    image = cv.imread(in_file)
    image = cv.resize(image , (0, 0), fx=scale, fy=scale)
    sepiafilter_image = image.copy()

    sepia_matrix = [[0.393, 0.769, 0.189] \
                ,[0.349, 0.686, 0.168]\
                ,[0.272, 0.534, 0.131]]

    if implementation == "python":
        for i in range(len(image)):
            for j in range(len(image[i])):
                for k in range(3):
                    sepia_value = min(255, (sepia_matrix[2-k][2])*image[i][j][0] + \
                        sepia_matrix[2-k][1]*image[i][j][1] + sepia_matrix[2-k][0]*image[i][j][2])
                    sepiafilter_image[i][j][k] = (1-level)*image[i][j][k]+level*sepia_value
    
    elif implementation == "numba":
        @jit
        def sepiaing(arr):
            "Function for sepiaing an image array"
            sepia_arr = arr.copy()
            sepia_matrix = [[ 0.393, 0.769, 0.189] , [ 0.349, 0.686, 0.168] , [ 0.272, 0.534, 0.131]]

            for i in range(len(arr)):
                for j in range(len(arr[i])):
                    for k in range(3):
                        sepia_value = min(255, sepia_matrix[2-k][2]*arr[i][j][0] \
                            + sepia_matrix[2-k][1]*arr[i][j][1] + sepia_matrix[2-k][0]*arr[i][j][2])
                        sepia_arr[i][j][k] = (1-level)*arr[i][j][k]+level*sepia_value

            return sepia_arr
        sepiafilter_image = sepiaing(image)
    
    elif implementation == "numpy":
        sepia_matrix = np.flip(sepia_matrix)
        for i in range(3):
            sepiafilter_image[:,:,i] = (1-level)*image[:,:,i] + level*np.clip(sepia_matrix[i,0]*image[:,:,0]\
                 + sepia_matrix[i,1]*image[:,:,1] + sepia_matrix[i,2]*image[:,:,2],None,255)
        #sepiafilter_image[:,:,1] = (1-level)*image[:,:,1] + level*np.clip(sepia_matrix[1,0]*image[:,:,0]\
        #     + sepia_matrix[1,1]*image[:,:,1] + sepia_matrix[1,2]*image[:,:,2],None,255)
        #sepiafilter_image[:,:,2] = (1-level)*image[:,:,2] + level*np.clip(sepia_matrix[2,0]*image[:,:,0]\
        #     + sepia_matrix[2,1]*image[:,:,1] + sepia_matrix[2,2]*image[:,:,2],None,255)
    
    else:
        raise ValueError("Not a valid implementation. Use python, numpy, or numba.")

    sepiafilter_image = sepiafilter_image.astype("uint8")
    if out_file == None:
        name = in_file.split(".")[0]
        cv.imwrite(f"{name}_sepia.jpeg", sepiafilter_image)
    else:
        cv.imwrite(f"{out_file}", sepiafilter_image)
    
    return sepiafilter_image