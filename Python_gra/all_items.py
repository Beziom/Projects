import pandas

def all_items_game():

    file_name = r"D:\Repozytorium\Projekty\Python_gra\all_items_game.csv"
    data = pandas.read_csv(file_name, header=None, index_col=0, squeeze=True)
    dict = data.to_dict()
    for key,values in dict.items():
        print({key:values})
        
all_items_game()