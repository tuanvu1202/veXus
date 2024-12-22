import fade
def logger(data, option):
    if option=="":
        print(fade.purpleblue("[ VEXUS ] > " + data))
    elif option=="load":
        print(fade.greenblue("[ VEXUS ] > " + data))
    elif option=="error":
        print("\033[91m[ VEXUS ] > " + data)
    elif option=="database":
        print(fade.greenblue("[ VEXUS ] > " + data))
