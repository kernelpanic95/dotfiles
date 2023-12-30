#!/bin/bash

sleep 3
mpv --no-video ~/dotfiles/audio/startupsound/startup.mp3

files=(~/dotfiles/audio/voicesound/*)
sleep 2
mpv --no-video "${files[RANDOM % ${#files[@]}]}"

