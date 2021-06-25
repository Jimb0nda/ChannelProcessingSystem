import numpy as np

#Function to compute Y=mX+c. m & c being paramter variables and X being input channel data array
def function1(parameters,inputs):

    try:
        #Scalars cannot be added to arrays as the dimensions don't match, therefore, parameter c is
        #multiplied by an identity matrix of size input array.
        Y = (parameters["m"]*inputs) + (np.identity(len(inputs))*parameters["c"])

        #Adds new key value pair to dictionary
        parameters["Y"] = Y

        #Returns updated parameter dictionary
        return parameters
    except:
        return 0

#Function to compute B=A+Y & the mean of the result.
def function2(parameters,inputs):

    try:
        B = parameters["A"] + parameters["Y"]

        b = np.mean(B)

        #Adds new key value pair to dictionary
        parameters["b"] = b

        #Returns float value b from matrix B
        return parameters
    except:
        return 0

#Function to compute A=1/X.
def function3(parameters,inputs):

    if(inputs.size > 0):
        A = np.reciprocal(inputs.astype(float))

        #Adds new key value pair to dictionary
        parameters["A"] = A

        #Returns updated parameter dictionary
        return parameters
    else:
        return 0

#Function to compute C=X+b.
def function4(parameters,inputs):

    try:
        #Scalars cannot be added to arrays as the dimensions don't match, therefore, calulated value b is
        #multiplied by an identity matrix of size input array.
        C = inputs + (np.identity(len(inputs))*parameters["b"])

        #Adds new key value pair to dictionary
        parameters["C"] = C

        #Returns updated parameter dictionary
        return parameters

    except:
        return 0
