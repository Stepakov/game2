from game_api import *
from color_out_api import out_colors, color_text
from termcolor import *

set_heap()

player = 1

while True:
    out_colors( "red", "The heap: ", get_heap() )
    out_colors( "yellow", "Remove stones from the row" )
    out_colors( "blue", "Player {} moves".format( player ) )
    pos = int( input( colored( "Which row: ", "green") ) )
    qua = int( input( colored( "How much: ", 'green' ) ) )
    res = get_from_heap( pos, qua )
    if not res:
        print( "wrong position" )
        continue
    if is_gameover():
        break
    player = 1 if player == 2 else 2

out_colors( "red", "THE WINNER IS PLAYER {}".format( player ) )