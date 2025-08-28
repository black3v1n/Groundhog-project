def help():
    print("SYNOPSIS")
    print("    ./groundhog period")
    print()
    print("DESCRIPTION")
    print("    period        the number of days defining a period")
    exit(0)
    
def check_input(value):
    try:
        float(value)
        return True
    except: 
        return False
