"""
Used to turn the ballasting system architecture into a graph for traversal
"""

from ballistPart import ballistPart
from typing import List


class grapher:

    @staticmethod
    def twoPointTraversal(
        entireSystem: List[ballistPart],
        entireSystemID: List[str],
        sourceNode: str,
        destinationNode: str,
    ):

        # Create two sets of nodes:  toDoSet and doneSet
        nodesToCheck = []
        nodesChecked = []

        # Add the source node to the toDoSet
        nodesToCheck.append(sourceNode)

        # While (nodesToCheck is not empty)
        while not len(nodesToCheck) == 0:

            # Remove the first element from nodesToCheck
            tempNode = nodesToCheck.pop(0)

            # Add it to nodesChecked
            nodesChecked.append(tempNode)

            targetIndex = entireSystemID.index(tempNode)

            # Foreach (node reachable from the removed node)
            for connectedNode in entireSystem[targetIndex].valveConnections:

                # If the node is actually on -> continue
                tempIndex = entireSystemID.index(connectedNode)
                if entireSystem[tempIndex].open:

                    # If node equals the destination node
                    if connectedNode == destinationNode:
                        # Connection found
                        return True

                    # If node is not in checkedNodes
                    if connectedNode not in nodesChecked:
                        nodesToCheck.append(connectedNode)  # Add to nodes to check

        # No connection found
        return False
