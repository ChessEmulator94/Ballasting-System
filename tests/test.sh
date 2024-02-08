#!/bin/bash

# Define the user inputs
input1="1"
input2="valves008,valves024" # Valves to close
input3="3"
input4="pipes001" # Source node
input5="pipes016" # Destination node
input6="5"



# Run the Python program and pass the inputs
echo -e "$input1\n$input2\n$input3\n$input4\n$input5\n$input6" | python3 driver.py
