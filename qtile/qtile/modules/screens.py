from libqtile import bar
from .widgets import *
from libqtile.config import Screen
from modules.keys import terminal
import os

screens = [
    Screen(
        
        top = bar.Bar(
            
            [   
                
                widget.Sep(padding=3, linewidth=0, background="#1E1F29"),
                widget.Image(filename='~/.config/qtile/eos-c.png', margin=3, background="#1E1F29", mouse_callbacks={'Button1': lambda: qtile.cmd_spawn("rofi -show combi")}),
                widget.Sep(padding=10, linewidth=0, background="#1E1F29"), 
                widget.GroupBox(
                                highlight_method='line',
                                this_screen_border="#FBD69B",
                                this_current_screen_border="#FBD69B",
                                active="#FBD69B",
                                inactive="#366276",
                                background="#1E1F29",
                                font = 'Victor Mono Bold',
                                ),
                widget.TextBox(
                    #   text = '',
                       padding = 0,
                       fontsize = 28,
                       foreground='#1E1F29'
                       ),    
                widget.Prompt(),
                widget.Spacer(length=5),
                widget.WindowName(foreground='#FBD69B',fmt='{}'),
                widget.Chord(
                    chords_colors={
                        'launch': ("#ff0000", "#FBD69B"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.CurrentLayoutIcon(
                    scale=0.5,
                    color ='#FBD69B'
                    ),
                widget.TextBox(
                     #  text = '',
                       padding = 0,
                       fontsize = 28,
                       foreground='#1E1F29'
                       ), 
                widget.CheckUpdates(
                    update_interval=1800,
                    distro="Arch_checkupdates",
                    display_format=" ",
                    fontsize = 15,
                    foreground="#FBD69B",
                    mouse_callbacks={
                        'Button1':
                        lambda: qtile.cmd_spawn(terminal)
                    },
                    background="#1E1F29"),
                widget.TextBox(                                                                    
                     #  text = '',
                       padding = 0,
                       fontsize = 28,
                       foreground ='#1E1F29',
                       ),   
                
                widget.Systray(
                    icon_size = 15               
                    ),
                widget.TextBox(
                    #   text = '',
                       padding = 0,
                       fontsize = 20,
                       foreground='#1E1F29'
                       ), 
                volume,
                widget.TextBox(                                                                    
                     #  text = '',
                       padding = 0,
                       fontsize = 20,
                       foreground='#1E1F29',
                       ),   
                widget.TextBox(
                    #   text = '',
                       padding = 0,
                       fontsize = 20,
                       foreground='#1E1F29'
                       ),    
                widget.Clock(format='  %A %d-%m-%Y %I:%M %p',
                             background="#1E1F29",
                             foreground='#ffffff',
                            mouse_callbacks={
                                    'Button1':
                                    lambda: qtile.cmd_spawn("coretime")
                                    },
                             ),

                widget.TextBox(                                                
                    #   text = '',
                       padding = 0,
                       fontsize = 28,
                       foreground='#1E1F29',
                       ),   
                widget.TextBox(
                    text=' ',
                    fontsize = 15,
                    mouse_callbacks= {
                        'Button1':
                        lambda: qtile.cmd_spawn(os.path.expanduser('~/.config/rofi/powermenu.sh'))
                    },
                    foreground='#FBD69B'
                )                
            ],
            30,  # height in px
            background="#1E1F29"  # background color
        ),),
]
