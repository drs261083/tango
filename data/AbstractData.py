'''
/*
 *
 *  This class stores the data structure for a abstract class of DataField.
 *  Effort is made to make it as general as possible for different mesh types.
 *
 *  Author :
 *  Date   :
 *
 */
'''

#external imports

#internal imports



class AbstractData(object):
    ## The constructor
    #
    #  @param self            The object pointer.
    #  @param Name            string: Name of the mesh
    #  @param Dimension       int: Dimension of the datafield.
    def __init__(self, Name, Dimension):

        ## @var name
        #  string: name of the data field
        self.name = Name

        ## @var size
        # int: size of the data field data
        self.size = 0

        ## @var data
        # python list: container to store the data
        self.data = []

    ## Initialize function of the mesh
    #
    def Initialize(self):
        pass

    ## Gets the dimension of the datafield data
    #
    #  @param self            The object pointer.
    #  @return int : Dimension of the datafield.
    def SetSize(self, Size):
        self.size = Size
        self.data = [0.0]*self.size

    ## Gets the size of the datafield data
    #
    #  @param self            The object pointer.
    #  @return int : Siez of the datafield.
    def GetSize(self):
        return self.size
