# Instagram filter package

### Prerequisites

opencv-python      4.5.3.56  
numpy              1.19.1  
numba              0.54.0  

### Functionality

A package and various python scripts for adding filters to images  
Currently has a grayscale filter and a sepia filter  

### Missing Functionality

No important missing functions.

### Installation

Package can be installed through pip while in the instapy folder
```bash  
pip install .
```

### Usage

How to use the package:  
  
In a python file one can use

```python  
import instapy.filters

#Creates a grayscale version of the image in_file, and returns an array of gray values for the image.
grayscale_image(in_file, out_file=None , implementation="python", scale=1.0)

#Creates a sepia filtered version of the image in_file, and returns an array of sepia values of the image.
sepia_image(in_file, out_file=None , implementation="python", scale=1.0, level=1.0)

#The images created by the functions above will have name out_file if it's not None.
#They created images will be created with the chosen implementation of either python, numpy, or numba.
#scale scales the image by the given factor, and level chooses the level of sepia for the image.
```

It is also possible to call the package directly from the command line, by
```bash  
instapy -f FILE -g/-se
```

For additional functionalities for all the possible command line arguments, write
```bash  
instapy -h
```
