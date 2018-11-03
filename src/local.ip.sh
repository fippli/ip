#!/bin/bash

# Print the local IP address of you device
echo $( ifconfig | grep "inet " | grep -v 127.0.0.1 | cut -d\  -f2 )
