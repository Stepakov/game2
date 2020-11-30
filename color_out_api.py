
colors = {
    'red': "\033[031m",
    'yellow': "\033[033m",
    'blue': "\033[034m",
    'green': "\033[032m"
}

def out_colors( color, *args ):
    text = ''
    for t in args:
        text += str( t )
    print( "{}{}\033[0m".format( colors[ color ], text ) )

def color_text( color, text ):
    print( "{}{}\033[0m".format( colors[ color ], text ) )