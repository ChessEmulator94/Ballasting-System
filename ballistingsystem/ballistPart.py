"""
Stores information about parts of the ballisting system

- Used for valves and other parts

"""

from typing import List


class ballistPart:

    # Stores a list of valves the part is connected to (as strings)
    valveConnections: List[str] = []
    # Stores type of part of the ballisting system
    partType: str
    # Unique identifier created using given partType & ID
    uPartID: str
    # Identifier within parts
    partID: str
    # Stores list of ballistPart objects this ballistPart is connected to
    ballistConnections = List[str]
    # Stores whether the valve is open or closed (for other parts, always == TRUE)
    open: bool = True

    # Getter for uniqueID
    def getUniqueID(self):
        return self.uPartID

    # Getter for connectedValves
    def getConnectedValves(self):
        return self.valveConnections

    """
    Constructor for ballistPart
        Parameters  : (partType: str, partID: str, valveConnetions: [str])
        Returns     : void                                           
    """

    def __init__(self, partType: str, partID: str, valveConnections):

        self.partType = partType
        self.valveConnections = valveConnections
        self.partID = partID
        self.uPartID = partType + partID
        self.open = True
