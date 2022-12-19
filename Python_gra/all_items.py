import pandas

def all_items_game():

    data = pandas.read_csv("Python_gra\\all_items_game.csv", header=None, index_col=0).squeeze(1)
    global all_items
    all_items = data.to_dict()
        
all_items_game()