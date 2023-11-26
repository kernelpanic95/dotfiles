#!/bin/bash
#  _   _       _             
# | \ | | ___ | |_ ___  ___  
# |  \| |/ _ \| __/ _ \/ __| 
# | |\  | (_) | ||  __/\__ \ 
# |_| \_|\___/ \__\___||___/ 
#                            
#  
# by kernelpanic.sh (2023) 
# this is a script for managing my notes
# ----------------------------------------------------- 

echo ""
echo "#  _   _       _             "
echo "# | \ | | ___ | |_ ___  ___  "
echo "# |  \| |/ _ \| __/ _ \/ __| "
echo "# | |\  | (_) | ||  __/\__ \ "
echo "# |_| \_|\___/ \__\___||___/ "
echo "#                            "
echo "#  "
echo "# by kernelpanic.sh (2023) "
echo "# ------------------------------------------"
echo ""
echo "Hello friend."

read -p "Do you want to open notes dir or start a new note? (d/n) " choice;

case $choice in 
    d|D)
        vim ~/notes;;
    n|N)
        read -p "Enter note filename adding the .txt extension: " notefile
        if test -f ~/notes/$notefile; then
            echo "file already exists, opening vim.."
            sleep 2
            command vim ~/notes/
        else
            echo "file doesn't exists, creating new file..."
            sleep 2
            vim ~/notes/$notefile
        fi;;
    *)
        exit;;

esac





