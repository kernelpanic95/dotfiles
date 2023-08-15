#!/bin/sh
xrandr --output eDP1 --off --output HDMI1 --primary --mode 1920x1080 --pos 0x0 --rotate normal --output VIRTUAL1 --off

dunst &
nitrogen --restore &
picom & disown # --experimental-backends --vsync should prevent screen tearing on most setups if needed

nm-applet &
cbatticon &
kdeconnect-indicator &

# Low battery notifier
~/.config/qtile/scripts/check_battery.sh & disown

# Start welcome
eos-welcome & disown

/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 & disown # start polkit agent from GNOME
