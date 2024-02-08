"""
Contains the overall ballasting system architecture
"""

from ballistPart import ballistPart
from typing import List


class ballistSystem:

    # Holds non valve ballistPart objects
    allBallistParts: List[ballistPart] = []
    # Holds all ballistPart IDs
    allBallistPartsID: List[str] = []

    # Holds valve ballistPart objects
    allBallistValves: List[ballistPart] = []
    # Holds all valve ballistPart IDs
    allBallistValvesID: List[str] = []

    # Holds the full system (graph)
    entireSystem: List[ballistPart] = []
    # Holds the full system IDs
    entireSystemID: List[str] = []

    # Combines valves and other parts together (IDs list & Objects list)
    def generateEntireSystem(self):

        self.entireSystem = self.allBallistParts + self.allBallistValves
        self.entireSystemID = self.allBallistPartsID + self.allBallistValvesID

        return None

    # Deconstruct partType lines and find valve connections
    def getConnections(self, connectionsLine: str):

        connectedValves: List[str] = []

        # Seperate full part ID from it's connections
        splitLine: List[str] = connectionsLine.split(":")

        # Get raw part ID
        tempID: str = splitLine[0].strip('"')
        # Store raw part ID at index 0 of return list
        connectedValves.append(tempID)

        # Get raw connections as string
        tempString: str = splitLine[1].strip(" ")
        tempString = tempString.strip("[")
        tempString = tempString.strip("]")
        tempString = tempString.strip(" ")
        tempString = tempString.replace(", ", ",")

        # Create list of connections
        tempList: List[str] = tempString.split(",")

        # Add connected valves to return list
        for temp in tempList:

            tempString = temp.strip(" ")
            tempString = temp.strip('"')
            connectedValves.append(tempString)

        return (
            connectedValves  # First index contains partID, rest are actual connections
        )

    """
    - Add the created objects to self

        Parameters  :  (allPartsAsLines: list[str])
        Returns     :  void   
    """

    def addParts(self, allPartsAsLines: List[str]):

        currentPart: str
        currentConnections: str

        for i in range(len(allPartsAsLines)):

            if i % 2 == 0:
                currentPart = allPartsAsLines[i]
            else:
                currentConnections = allPartsAsLines[i]
                idConnectionsList = ballistSystem.getConnections(
                    self, currentConnections
                )
                actualID = idConnectionsList[0]
                actualConnections = idConnectionsList[1:]

                for i in range(len(actualConnections)):
                    actualConnections[i] = "valves" + actualConnections[i]

                tempBallistPart = ballistPart(currentPart, actualID, actualConnections)
                self.allBallistParts.append(tempBallistPart)
                self.allBallistPartsID.append(tempBallistPart.getUniqueID())

    # Generates a list of all valves in the system inferring them from vessel.yml
    def generateValveList(self):

        # Iterate over all created ballistPart objects
        for part in self.allBallistParts:

            # Iterate over all connected valves of ballistPart object
            for connectedValve in part.valveConnections:

                # Temp ID for the new valve
                tempValveID = "" + connectedValve

                # Check if the the valve has already been added to the parts list
                if tempValveID not in self.allBallistValvesID:
                    # Add the valve to the parts list
                    tempBallistPart = ballistPart(
                        "", connectedValve, [part.getUniqueID()]
                    )
                    self.allBallistValves.append(tempBallistPart)
                    self.allBallistValvesID.append(tempValveID)
                else:
                    index = self.allBallistValvesID.index(tempValveID)
                    # Check if the current part has already been added as a connection to the valve
                    if (
                        part.getUniqueID()
                        not in self.allBallistValves[index].valveConnections
                    ):
                        # Add the connection to the valve
                        self.allBallistValves[index].valveConnections.append(
                            part.getUniqueID()
                        )

        return None

    def closeValves(self, nodesToClose: List[str]):

        for node in nodesToClose:
            tempIndex = self.entireSystemID.index(node)
            self.entireSystem[tempIndex].open = False

        return None

    def openValves(self, nodesToOpen: List[str]):

        for node in nodesToOpen:
            tempIndex = self.entireSystemID.index(node)
            self.entireSystem[tempIndex].open = True

        return None

    def __init__(self):

        self.allBallistParts = []
        self.allBallistPartsID = []
        self.entireSystemID = []
        self.entireSystem = []
