import numpy as np

#Function to compute Y=mX+c. m & c being paramter variables and X being input channel data array
def function1(parameters,inputs):

    #Scalars cannot be added to arrays as the dimensions don't match, therefore, parameter c is
    #multiplied by an identity matrix of size input array.
    Y = (parameters[0]*inputs) + (np.identity(len(inputs))*parameters[1])

    #Returns matrix Y
    return Y

#Function to compute B=A+Y & the mean of the result.
def function2(parameters,inputs):

    Y = function1(parameters,inputs)
    A = function3(parameters,inputs)

    B = A + Y

    b = np.mean(B)

    #Returns float value b from matrix B
    return b

#Function to compute A=1/X.
def function3(parameters,inputs):

    A = np.reciprocal(inputs.astype(float))

    return A

#Function to compute C=X+b.
def function4(parameters,inputs):

    b = function2(parameters,inputs)

    #Scalars cannot be added to arrays as the dimensions don't match, therefore, calulated value b is
    #multiplied by an identity matrix of size input array.
    C = inputs + (np.identity(len(inputs))*b)

    return C
