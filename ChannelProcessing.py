import numpy as np
import VectorArithmetic

def main():

    inputs = channelData()
    parameters = parameterData()

    z = VectorArithmetic.function2(parameters,inputs)

    print(z)

#Function to read in channel data from channels.txt file.
#Returns an array of float values
def channelData():

    #Read data from text files, casting vaues to float and creating an array
    data = np.genfromtxt("channels.txt", dtype=float,
                     encoding=None, delimiter=",")

    #Delete the first element in the array to remove the array name 'X'
    chanData = np.delete(data, 0)

    return chanData

#Function to read in parameter data from parameters.txt file.
#Returns an array of float values
def parameterData():

    #Read data from text files, using only the column at index 1 to ignore variable names
    #Casts vaues to float and creates an array
    paramData = np.genfromtxt("parameters.txt", dtype=float,
                     usecols=(1), encoding=None, delimiter=",")

    return paramData

if __name__ == '__main__':
    main()
