import fade

def logger(data, option):
    if option=="":
        print(fade.purpleblue("[ VEXUS ] > " + data))
    elif option=="load":
        print(fade.greenblue("[ LOAD ] > " + data))
    elif option=="error":
        print(fade.pinkred("[ ERROR ] > " + data))
