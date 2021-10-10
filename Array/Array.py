class Array:

    def __init__(self, shape, *values):
        """
        
        Initialize an array of n-dimensionality. Elements can only be of type:
        - int
        - float
        - bool
        
        Args:
            shape (tuple): shape of the array as a tuple.
            *values: The values in the array. Preferably of the same type.
        Raises:
            ValueError: If the values are not of the accepted type.
            ValueError: If the number of values does not fit with the shape.
        """
        shape_len = 1
        for x in shape:
            shape_len = shape_len*x

        if len(values) != shape_len:
            raise ValueError("The number of values does not fit with the shape.")

        make_float = False
        for i in range(shape[0]):
            if isinstance(values[i], float) != True and isinstance(values[i], int) != True and isinstance(values[i], bool) != True:
                raise ValueError("The values are not float, integers or boolean")
            elif type(values[i]) != type(values[0]) and make_float != True:
                make_float = True
        
        #If make_float is True, then the elements of the array have different types, and so they become float
        if make_float == True:
            values = [float(i) for i in values]
        
        #Trippel for-loop for creating the array from the innermost arrays an upwards.
        arr = []
        val = values
        for j in range(1, 1 + len(shape)):
            n_array = int(len(val)/shape[-j])
            arr = []
            for i in range(0, n_array):
                arra = []
                for k in range(0, shape[-j]):
                    arra.append(val[k+i*shape[-j]])
                arr.append(arra)
            val = arr
        
        self.values = values
        self.array = val[0]
        self.shape = shape
    
    def flat_array(self):
        """ Flattens the N-dimensional array of values into a 1-
        dimensional array.
        Returns:
        list: flat list of array values.
        """
        flat_array = list(self.values)
        return flat_array

    def __getitem__(self , item):
        """ Returns value of item in array.
        Args:
            item (int): Index of value to return.
        Returns:
            value: Value of the given item.
        Raises:
            ValueError: if the item is larger than the array index.
            ValueError: if the item is not an integer
        """
        if isinstance(item, int) == False:
            raise ValueError("Needs to be an integer")
        elif abs(item) >= self.shape[0]:
            raise ValueError("Item larger than the arrays index")
        
        return self.array[item]
        
    def __str__(self):
        """Returns a nicely printable string representation of the array.
        Returns:
            str: A string representation of the array.
        """
        string = "["
        for i in range(self.shape[0]):
            string = string+f"{self.array[i]}, "
        
        return string[:-2]+"]"

    def __add__(self, other):
        """Element-wise adds Array with another Array or number.
        Args:
            other (Array, float, int): The array or number to add element-wise to this array.
        Returns:
            Array: the sum as a new array.
        """
        
        if isinstance(other, float) or isinstance(other, int) or isinstance(other, bool):
            oth = Array((1,), other)
        else:
            oth = other
        
        values = []
        A = self.flat_array()
        B = oth.flat_array()

        if oth.shape != self.shape and oth.shape[0] != 1:
            return NotImplemented
        elif oth.shape[0] == 1:
            for i in range(len(A)):
                values.append(A[i] + B[0])
        else:
            for i in range(len(A)):
                values.append(A[i] + B[i])

        return Array(self.shape, *values)

    def __radd__(self, other):
        """Element-wise adds Array with another Array or number.
        Args:
            other (Array, float, int): The array or number to add element-wise to this array.
        Returns:
            Array: the sum as a new array.
        """
        return self.__add__(other)

    def __sub__(self, other):
        """Element-wise subtracts an Array or number from this Array.
        
        Args:
            other (Array, float, int): The array or number to subtract element-wise from this array.
        Returns:
            Array: the difference as a new array.
        """

        if isinstance(other, float) or isinstance(other, int) or isinstance(other, bool):
            oth = Array((1,), other)
        else:
            oth = other
        
        values = []
        A = self.flat_array()
        B = oth.flat_array()
        
        if oth.shape != self.shape and oth.shape[0] != 1:
            return NotImplemented
        elif oth.shape[0] == 1:
            for i in range(len(A)):
                values.append(A[i] - B[0])
        else:
            for i in range(len(A)):
                values.append(A[i] - B[i])

        return Array(self.shape, *values)

    def __rsub__(self, other):
        """Element-wise subtracts this Array from a number or Array.
        Args:
            other (Array, float, int): The array or number being subtracted from.
        Returns:
            Array: the difference as a new array.
        """
        if isinstance(other, float) or isinstance(other, int) or isinstance(other, bool):
            oth = Array((1,), other)
        else:
            oth = other
        
        values = []
        A = self.flat_array()
        B = oth.flat_array()
        
        if oth.shape != self.shape and oth.shape[0] != 1:
            return NotImplemented
        elif oth.shape[0] == 1:
            for i in range(len(A)):
                values.append(B[0] - A[i])
        else:
            for i in range(len(A)):
                values.append(B[i] - A[i])
        
        return Array(self.shape, *values)

    def __mul__(self, other):
        """Element-wise multiplies this Array with a number or array.
        
        Args:
            other (Array, float, int): The array or number to multiply element-wise to this array.
        Returns:
            Array: a new array with every element multiplied with `other`.
        """

        if isinstance(other, float) or isinstance(other, int) or isinstance(other, bool):
            oth = Array((1,), other)
        else:
            oth = other
        
        values = []
        A = self.flat_array()
        B = oth.flat_array()
        
        if oth.shape != self.shape and oth.shape[0] != 1:
            return NotImplemented
        elif oth.shape[0] == 1:
            for i in range(len(A)):
                values.append(A[i] * B[0])
        else:
            for i in range(len(A)):
                values.append(A[i] * B[i])
        
        return Array(self.shape, *values)

    def __rmul__(self, other):
        """Element-wise multiplies this Array with a number or array.
        Args:
            other (Array, float, int): The array or number to multiply element-wise to this array.
        Returns:
            Array: a new array with every element multiplied with `other`.
        """
        
        return self.__mul__(other)


    def __eq__(self, other):
        """Compares an Array with another Array.
        
        Args:
            other (Array): The array to compare with this array.
        Returns:
            bool: True if the two arrays are equal (identical). False otherwise.
        """
        A = self.flat_array()
        B = other.flat_array()

        eq = True
        #We assume they are equal, and then check if they are not.
        if other.shape != self.shape:
            eq = False
        elif type(B[0]) != type(A[0]):
            eq = False
        else:
            for i in range(len(A)):
                if A[i] != B[i]:
                    eq = False; break
        
        return eq

    def is_equal(self, other):
        """Compares an Array element-wise with another Array or number.

        Args:
            other (Array, float, int): The array or number to compare with this array.
        Returns:
            Array: An array of booleans with True where the two arrays match and False where they do not.
                   Or if `other` is a number, it returns True where the array is equal to the number and False
                   where it is not.
        Raises:
            TypeError: If other is not an array or a number.
            ValueError: if the shape of self and other are not equal.
        """
        if isinstance(other, Array) == False and isinstance(other, float) == False and isinstance(other, int) == False:
            raise TypeError("Not an array or a number")
        
        if isinstance(other, Array) == True and other.shape != self.shape:
            raise ValueError("The two arrays are of different shapes")
        
        A = self.flat_array()
        eqlist = []

        if isinstance(other, Array) == True:
            B = other.flat_array()
            for i in range(len(A)):
                if A[i] == B[i]:
                    eqlist.append(True)
                else:
                    eqlist.append(False)

        else:
            for i in range(len(A)):
                if A[i] == other:
                    eqlist.append(True)
                else:
                    eqlist.append(False)

        return Array(self.shape, *eqlist)

    def min_element(self):
        """Returns the smallest value of the array.
        Returns:
            float: The value of the smallest element in the array.
        """
        smallest = float('inf')
        A = self.flat_array()

        for i in range(len(A)):
            if A[i] < smallest:
                smallest = A[i]
            
        return smallest