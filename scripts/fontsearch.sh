#!/bin/bash
#  _____           _                           _     
# |  ___|__  _ __ | |_ ___  ___  __ _ _ __ ___| |__  
# | |_ / _ \| '_ \| __/ __|/ _ \/ _` | '__/ __| '_ \ 
# |  _| (_) | | | | |_\__ \  __/ (_| | | | (__| | | |
# |_|  \___/|_| |_|\__|___/\___|\__,_|_|  \___|_| |_|
#                                                   
# by kernelpanic.sh (2023)
# -----------------------------------------------------
#
fc-list \
    | grep -ioE ": [^:]*$1[^:]+:" \
    | sed -E 's/(^: |:)//g' \
    | tr , \\n \
    | sort \
    | uniq
