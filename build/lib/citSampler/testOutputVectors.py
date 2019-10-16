def testOutputVectors(fname,theConstraint): #Test all vectors in the output file
    """
    fname: str
    theConstraint: instance from Constraint()
    """
    with open(fname, "r") as f:
        lines = f.readlines()
    print('lines[0] is: ',lines[0])
    # Get a list of vectors
    vectorArrays = [[float(x) for x in line.split(" ")] for line in lines]
    for vector in vectorArrays:
        if not theConstraint.apply(vector):
            return False
    return True
