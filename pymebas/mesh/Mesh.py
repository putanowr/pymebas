# -*- coding: utf-8 -*-
"""Define mesh data structure.
"""
import numpy as np

class BasicConnections(object):
    """Basic connectivity lists"""
    def __init__(self):
        self.node = []
        """list of list of node to node adjacencies"""

        self.edge = []
        """list of list of node to edge incidencies"""

        self.element = []
        """List of list of node to element incidencies"""

        self.subdomain = []
        """list of subdomains the nodes belongs"""

    def reset(self):
        """Reset all connectivity list to empty ones"""
        self.node = []
        self.edge = []
        self.element = []
        self.subdomain = []

class SubdomainConnections(object):
    """Subdomain connectivity lists.
    """
    def __init__(self):
        self.subdomain = []
        """list of list of subdomain to subdomain adjacencies"""

        self.node = []
        """list of list of subdomain to node incidencies"""

        self.elem = []
        """list of list of subdomain to element incidencies"""

        self.interface_elem = []
        """list of list of subdomain to interface elements incidencies"""

        self.inteface_node = []
        """list of list of subdomain to interface nodes"""

class EdgeConnections(object):
    """Edge connectivity lists"""
    def __init__(self):
        self.node = []
        """list of edge to node incidencies"""

        self.subdomain = []
        """list of edge to subdomain incidencies"""

class FaceConnectios(object):
    """Face connectivity lists"""
    def __init__(self):
        self.node = []
        """list of list of face to node incidencies"""

class MeshCount(object):
    """Proxy class for holding cardinality of various mesh components.
    """
    def __init__(self):
        self.nodes = 0
        self.edges = 0
        self.faces = 0
        self.elems = 0
        self.sudomains = 0
        self.subdomain_elems = []
        self.subdomain_neighbours = []
        self.subdomain_parts = []
        self.subdomain_nodes = []
        self.subdomain_interface_nodes = []

    def reset(self):
        """Reset counts to zero"""
        self.nodes = 0
        self.edges = 0
        self.faces = 0
        self.elems = 0
        self.sudomains = 0
        self.subdomain_elems = []
        self.subdomain_neighbours = []
        self.subdomain_parts = []
        self.subdomain_nodes = []
        self.subdomain_interface_nodes = []

    def update(self, mesh):
        """Update counters from mesh connectivity
        """
        pass

class Mesh(object):
    """Data structure for unstructure finite element mesh.
    """
    def __init__(self):
        self.space_dim = -1

        self.coords = np.array([])

        self.node_to = BasicConnections()
        self.elem_to = BasicConnections()
        self.edge_to = EdgeConnections()
        self.face_to = FaceConnectios()
        self.subdomain_to = SubdomainConnections()

        self.count = MeshCount()

        # elements
        self.elem_type = []
        self.elem_weight = []
        self.elem_size = []
        """list of element size"""

        self.elem_barycenter = np.array([])
        """array of elements' barycenters"""

        self.subdomain_weight = []
        """list of subdomain weights"""

        self.subdomain_barycenter = np.array([])
        """array of subdomain barycenters"""

        # local to global numbering

        self.l2g_node = []
        """list of mapping from local node number to global node number"""

        self.l2g_elem = []
        """list of mapping from local element number to global element number"""

    @classmethod
    def fromfile(cls, file_name, file_format, file_type):
        """Create mesh reading its data from give file"""
        obj = cls()
        obj.read(file_name, file_format, file_type)
        return obj

    def read(self, file_name, file_format='', file_type='asci'):
        """Read mesh from file"""
        if file_name is '':
            pass
        if file_format is '':
            pass
        if file_type is '':
            pass
        self.count.nodes = 12
