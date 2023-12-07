#!/usr/bin/python3

if __name__ == "__main__":

    import hidden_4

    arr = dir(hidden_4)
    for arr in arr:
        if arr[0:2] != "__":
            print(arr)
