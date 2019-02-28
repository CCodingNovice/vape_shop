import pandas as pd

def create_database(my_data):
    df = pd.DataFrame({
        "id": my_data[0],
        "name": my_data[1],
        "price": my_data[2],
        "amount": my_data[3]
    })
    df.to_csv("vapeshop.csv")


def insert_to_database(my_data):
    db_data = pd.read_csv("vapeshop.csv")
    for d in my_data:
        db_data.loc[db_data.__len__()] = d


def get_data_from_db():
    data = pd.read_csv("vapeshop.csv")
    output = [[], [], [], []]
    output = data.to_list()
    return output
