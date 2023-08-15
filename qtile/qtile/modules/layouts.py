from libqtile import layout
from libqtile.config import Match

layouts = [
    layout.MonadTall(margin=10, border_focus='#FBD69B',
                     border_normal='#366276'),
    #layout.Columns(border_focus_stack='#FBD69B'),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
   # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    layout.Matrix(margin=3, border_focus='#FBD69B', border_normal='#366276'),
   # layout.MonadTall(margin=10, border_focus='#FBD69B',
     #                border_normal='#366276'),
    layout.MonadWide(margin=10, border_focus='#FBD69B',
                     border_normal='#366276'),
    # layout.RatioTile(),
    # layout.Tile(),
   # layout.TreeTab(margin=10, border_focus='#FBD69B',
      #               border_normal='#366276'),
    layout.VerticalTile(margin=3, border_focus='#FBD69B', border_normal='#366276'),
    #layout.Zoomy(margin=10, border_focus='#FBD69B',
       #              border_normal='#366276'),
]

floating_layout = layout.Floating(border_focus='#FBD69B', border_normal='#366276', float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])
