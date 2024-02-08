"""
Acts as the backbone of the progam

- Handles parsing of settings file
- Deconstructs vessel.yml lines and creates ballistPart objects with connections
- Creates a ballistSystem object filled with ballistPart objects


"""

from ballistSystem import ballistSystem
from grapher import grapher
from typing import List


"""
Returns a list containing parts (including valves) and their 
connected valves with format: 
[part(1), connections(1), part(2), connections(2), ... , part(n), connections(n)]
"""


def importFile(fileName: str):

    # Open the file as specFile
    specFile = open(fileName, "r")
    # Store all the lines in this array
    fileLines = specFile.readlines()
    # Flag indicating which part of file the parser is in
    withinValves: bool = False
    # Current part type that is being read
    currentPart: str = ""

    # List of different parts in ballasting system
    allPartTypes = ["pipes", "tanks", "sea", "pumps"]

    # To store part type & connected valves every 2 indexes
    allFoundParts = []

    # Parse through the file
    for individualLine in fileLines:

        # Remove newline character
        individualLine = individualLine.strip()

        # Determine if in new section of connections
        temp = individualLine.split(":")

        if temp[0] in allPartTypes:  # New section found
            currentPart = temp[0]
            withinValves = True

        elif withinValves is True:  # Valve connections found
            allFoundParts.append(currentPart)  # Appends the type of part
            allFoundParts.append(individualLine)  # Appends the connected valves

    return allFoundParts


# CLI  menu for the program
def printMenu():

    print("\nMenu:\n")
    print("1. Close Valves")
    print("2. Open Valves")
    print("3. Check if parts are connected")
    print("4. View all parts & status")
    print("5. Exit")
    print()


def main():

    # Create new system
    fullBallistade = ballistSystem()

    # Open the specifications file and parse it
    allParts = importFile("vessel.yml")

    # Call ballistSystem.addParts()
    fullBallistade.addParts(allParts)

    # Create valve objects
    fullBallistade.generateValveList()

    # Merge Valves and Parts to create main graph for traversal
    fullBallistade.generateEntireSystem()

    # Load main menu
    while True:

        menuSelection: str
        
        printMenu()
        menuSelection = input("Enter your choice: ")

        print()

        if menuSelection == "1":
            userInput: str = input(
                'Enter the IDs of the valves you want to close (seperated by ","): '
            )
            userInputSeperated: List[str] = userInput.split(",")
            fullBallistade.closeValves(userInputSeperated)

        elif menuSelection == "2":
            userInput = input(
                'Enter the IDs of the valves you want to open (seperated by ","): '
            )
            userInputSeperated = userInput.split(",")
            fullBallistade.openValves(userInputSeperated)

        elif menuSelection == "3":
            sourceNode = input("Enter first ballisting part ID\n")
            destinationNode = input("Enter second ballisting part ID\n")

            # Run graphing algorithm
            connected: bool = grapher.twoPointTraversal(
                fullBallistade.entireSystem,
                fullBallistade.entireSystemID,
                sourceNode,
                destinationNode,
            )

            if connected:
                print("\nThe two parts selected are currently connected")
            else:
                print("\nThe two parts selected are currently disconnected")

        elif menuSelection == "4":
            print("All parts and status:")
            for part in fullBallistade.entireSystem:
                openStatus = "Open"
                if not part.open:
                    openStatus = "Closed"
                print("Part ID: " + part.getUniqueID() + " - " + openStatus)

        elif menuSelection == "5":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter a valid option.")


"""
Calls main method
        Parameters  : 
        Returns     :  void 
"""
if __name__ == "__main__":
    main()
