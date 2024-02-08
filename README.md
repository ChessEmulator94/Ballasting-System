# Ballasting System Checker

This program is designed to determine whether two parts are connected in a ballasting system. 

## Features

- Parses settings file (`vessel.yml`) to create ballastPart objects with connections.
- Manages opening and closing valves.
- Checks if two parts in the ballasting system are connected.
- Displays all parts and their status.

## Installation

1. Ensure you have Python 3.11 and Poetry installed on your system.
2. Navigate to the project directory and install dependencies by running `poetry install`.

3. (optional) An automated test that shows user inputs has been created using `expect`. This
    is a Unix tool, and thus needs to be installed separately by running:
    `brew install expect` (macOS)

## Usage

1. Ensure your ballasting system specifications file `vessel.yml` is in the same directory as `driver.py`
2. In terminal avigate to the directory containing `driver.py`
3. Run the program by executing `poetry run python driver.py`
4. Follow the on-screen menu to perform various actions:
   - Close valves
   - Open valves
   - Check if two parts are connected
   - View all parts and their status
   - Exit the program

## Notes

There is no validation/verification on data entry (apart from when in the main menu), if data is input
incorrectly, the program will stop running. For this reason, please make sure data is entered as follows:

To view all parts (ballisting parts and valves) in the system and their respective identifiers, select `4` from the main menu

[When selecting valves to close/open]
- use their IDs. These are made using the word `valves` and their respective number e.g `valves001`
- Enter valves as a list seperated by `,`, without spaces e.g `valves001,valves002`

[When checking if two parts are connected]
- Enter the ID of the part e.g `pipes001` 


## Testing

Some automated tests have been created to demonstrate functionality. These can be used as is or altered.
`test.sh` & `BasicTest.sh` will run normal bash scripts. `TestShowingUser.exp` will run the same tests but show user input on screen.

To use the tests as is:
1. Copy the files from within the `tests` directory to within the `ballistingsystem` directory
2. Navigate to the `ballistingsystem` directory in terminal 
3. run: chmod +x test_script_here.sh (replace `test_script_here.sh` with the file name)
4. run: ./test_script_here.sh (replace `test_script_here.sh` with the file name)

If you wish to change the parameters of the tests, such as selecting different valves to close:
- To change the valves to close, alter line 5 of `test.sh` or `TestShowingUser.exp`, make sure to follow the correct convention
- To change the parts having their connection status tested, change line 7 & 8 of `test.sh` or `TestShowingUser.exp`
- If you run a test with `.exp`, allow for some time to complete the test as it is considerably slower than `.sh` tests


## File Structure

- `driver.py`: Main script orchestrating the functionality of the program.
- `ballistPart.py`: Defines the `ballistPart` class representing individual parts in the ballasting system.
- `ballistSystem.py`: Defines the `ballistSystem` class managing the collection of `ballistPart` objects and their interactions.
- `grapher.py`: Contains algorithms for traversing the ballasting system graph.
