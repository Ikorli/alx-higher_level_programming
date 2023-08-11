#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    
    total = len(sys.argv) - 1
    
    if total == 0:
        print("0 arguments.")
    elif total == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(total))
    
    for i in range(1, total + 1):
        print("{:d}: {}".format(i, sys.argv[i]))