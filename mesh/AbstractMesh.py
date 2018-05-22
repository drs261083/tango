'''
/*
 *
 *  This class stores the data structure for a abstract class of Mesh.
 *  Effort is made to make it as general as possible for different mesh types.
 *
 *  Author :
 *  Date   :
 *
 */
'''

#external imports

#internal imports
import AbstractDataField



class AbstractMesh(object):

    ## The constructor
    #
    #  @param self            The object pointer.
    #  @param Name            string: Name of the mesh
    #  @param IsSubmesh       bool: if the mesh object is a submesh or not.
    #  @param Parent          MeshObject: if the mesh object is a submesh then this is the object of its parent.
    def __init__(self, Name, IsSubmesh=False, Parent=None):

        ## @var parent
        # python object: parent mesh
        self.parent = Parent

        ## @var name
        #  string: name of the data field
        self.name = Name

        ## @var data_fields_dict
        #  dictionary{string:python object} holds the data_fields_dict which live on this mesh
        self.data_fields_dict = dict()

        ## @var num_points
        # int: number of points
        self.num_points = 0

        ## @var points
        # python map of int(id) and list of doubles: stores points in this format : [x1,y1,z1,x2,y2,z2,...]
        self.points = {} # {id:[x,y,z]}

        ## @var sub_mesh_dict
        #  dictionary{string:python object} holds the submesh of the mesh
        self.sub_mesh_dict = dict()

        ## @var is_submesh
        #  bool to say if the object is a submesh
        self.is_submesh = IsSubmesh

    ## Initialize function of the mesh
    #
    def Initialize(self):
        pass

    ## Add a node to the mesh
    #
    #  @param self    The object pointer.
    #  @param PointId             int: node id
    #  @param PointCoordinates    list[double] : coordinates [x,y,z]
    def AddPoint(self, PointId, PointCoordinates):
        pass

    ## Adds a data field to the mesh
    #
    #  @param self    The object pointer.
    #  @param Name         string: name of the data field.
    #  @param Dimension    int: dimension of the data field.
    #  @paran OnElements   bool: if the datafield is defined on the elements
    def AddDataField(self, Name, Dimension, OnElements=False):
        pass

    ## Adds a submesh to the existing mesh.
    #
    #  @param self            The object pointer.
    #  @param NameOfSubmesh   string : The name of the submesh to be added.
    def AddSubmesh(self, NameOfSubmesh):
        pass

    ## Gets a data field from the mesh.
    #
    #  @param self    The object pointer.
    #  @param DataFieldName          string: name of the data field.
    #  @return DataField             python object: data field wrapper object
    def GetDataField(self, DataFieldName):
        pass

    ## Gets a submesh of the given name.
    #
    #  @param self            The object pointer.
    #  @param NameOfSubmesh   The name of the submesh to be obtained.
    def GetSubmesh(self, NameOfSubmesh):
        pass

    ## Deletes a data field of the mesh
    #
    #  @param self    The object pointer.
    #  @param DataFieldName    string: name of the data field to delete
    def DeleteDataField(self, DataFieldName):
        pass

    ## Delets a submesh of the given name.
    #
    #  @param self            The object pointer.
    #  @param NameOfSubmesh   The name of the submesh to be deleted.
    def DeleteSubmesh(self, NameOfSubmesh):
        pass

    ## Delets a submesh of the given name.
    #
    #  @param self            The object pointer.
    #  @param NodeId   Id of the node to be deleted.
    def DeleteNode(self, NodeId):
        pass