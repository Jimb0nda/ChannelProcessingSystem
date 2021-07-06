import numpy as np
import VectorArithmetic

def main():

    inputs = channelData()
    parameters = parameterData()
    output = 'b'

    #While value b has not been added to the parameters dictionary, keep looping
    while(output not in parameters):

        # For each attribute of module VectorArithmetic, if its callable, call it
        for i in dir(VectorArithmetic):
            function = getattr(VectorArithmetic,i)
            if callable(function):
                function(parameters,inputs)

    print(parameters[output])

#Function to read in channel data from channels.txt file.
#Returns an array of float values
def channelData():

    #Read data from text files, casting vaues to float and creating an array
    data = np.genfromtxt("ChannelProcessingSystem/channels.txt", dtype=float,
                     encoding=None, delimiter=",")

    #Delete the first element in the array to remove the array name 'X'
    chanData = np.delete(data, 0)

    return chanData



#Function to read in parameter data from parameters.txt file.
#Returns an array of float values
def parameterData():

    #Extract key and value pair from text file and place into dictionary
    f = open("ChannelProcessingSystem/parameters.txt", 'r')
    paramData = {}
    for line in f:
        key, value = line.strip().split(',')
        paramData[key.strip()] = float(value.strip())

    f.close()

    return paramData



if __name__ == '__main__':
    main()
