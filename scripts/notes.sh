#!/bin/bash
#  _   _       _             
# | \ | | ___ | |_ ___  ___  
# |  \| |/ _ \| __/ _ \/ __| 
# | |\  | (_) | ||  __/\__ \ 
# |_| \_|\___/ \__\___||___/ 
#                            
#  
# by kernelpanic.sh (2023) 
# ----------------------------------------------------- 

read -p "Enter note filename adding the .txt extension: " notefile
if test -f ~/notes/$notefile; then
    echo "file already exists, opening vim.."
    sleep 2
    command vim ~/notes/
else
    echo "file doesn't exists, creating new file..."
    sleep 2
    vim ~/notes/$notefile
fi

