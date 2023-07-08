# Task 1
# Write a function called oops that explicitly raises an IndexError exception when called. Then write another function that calls oops inside a try/except state­ment to catch the error. What happens if you change oops to raise KeyError instead of IndexError?

def oops():   
    raise IndexError  # якщо тут буде KeyError, то KeyError небуде спіймано, бо except очікує IndexError

def catch_oops():
    try:
        oops()
    except IndexError as e:
        print("catch IndexError") 

catch_oops()        
     


def oops():
     raise KeyError
     
def catch_key():
    try:
        oops()
    except KeyError as e:
        print("catch KeyError ")

catch_key()

    

