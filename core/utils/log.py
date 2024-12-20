import fade

def logger(data, option):
    if option=="load":
        print("\u001b[32;1m"+"[ veXus ] > " + data)
    if option=="error":
        print("\u001b[31;1m"+"[ veXus ] > " + data)
