# Tensors:
# Tensors is a container/datastructure to store Numbers (also stores characters or strings but its very rare)
# 1. 0D Tensors/Scalar:  1. Stores single numbers.
#                        2. Example: import Numpy as np 
#                                    a = np.array(4)
#                                    print(a)  --> array(4) 
#                                    print(a.ndim) --> 0

# 2. 1D Tensors/Vector:  1. Stores Multiple numbers
#                        2. Example: import Numpy as np 
#                                    a = np.array([1,2,3,4])
#                                    print(a)  --> array([1,2,3,4]) 
#                                    print(a.ndim) --> 1
#                        3. Tensors is 1 Dimensionals But, vector here is 4 Dimensional in above Example.

# 3. 2D Tensors/Matrices: 1. collection of vectors.
#                         2. Example: import Numpy as np 
#                                    a = np.array([[1,2,3],[4,5,6],[7,8,9]])
#                                    print(a)  --> array([[1,2,3],[4,5,6],[7,8,9]]) 
#                                    print(a.ndim) --> 2


# Rank, Axes, Shapes:
#   Axes: x,y,z
#   Rank: 1. Number of Axes = Number of Dimensions. 
#         2. Calculate using ndim.
#   Shapes: Dimersion along each axes.
#           Ex: [[1,2]
#                [3,4]
#                [5,6]]  shape: (3,2)
#   Size/Number of items of a tensor:Muliply shape of tensors  
# Note: N-dimensional array and Tensors are the same.


# 3D Tensors: Used in NLP.
#    For Example: 1. Hi Rohit
#                 2. Hi Mohit
#                 3. Hi Ronit

#                 Hi | Rohit | Mohit | Ronit
#                 1  | 0     |  0    | 0 
#                 0  | 1     |  0    | 0 
#                 0  | 0     |  1    | 0
#                 0  | 0     |  0    | 1  

#   "Hi Rohit": [[1,0,0,0], [0,1,0,0]]   2D tensors
#   "Hi Mohit": [[1,0,0,0], [0,0,1,0]]   2D tensors
#   "Hi Ronit": [[1,0,0,0], [0,0,0,1]]   2D tensors

#  collection of all sentensce which is a 2D tensors is a 3D Tensors.

# 4D Tensors: Image Based Data. 
#             Suppose there are 3 colors in Images pixels RGB.
#             For representing each pixels we use a matrix which is a 
#             2D Tensors, Now collection of this entire pixels to make 
#             a Image is 3D Tensors. Now the, collection / Batches of 
#             this entire series of photos/ Images are then 4D tensors. 

# 5D Tensors: Videos. 1 video clip here is considered to be a 4D Tesors.
#             Now, collection of multiple videoclips will be 5D Tensors. 



# Creation a Virtual Environment:
# 1. creating a virtual environment: python -m venv venv
# 2. Activate the Environment: venv/Scripts/activate
# 3. Install all dependencies: pip install -r requirements.txt
# 4. Saving new dependencies in requirements.txt file: 
#    "pip freeze > requirements.txt"