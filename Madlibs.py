def mad_lib():


    # This is Madlibs.py for CS 415 Quiz #1 (Programming)
    # By Kyle Stewart

    #These print statements output and promet the user to input 2 nouns and 2 adjectives
    print("Enter an adjective:")
    Adj1 = str(input())
    print("Enter a noun:")
    No1 = str(input())
    print("Enter a noun:")
    No2 = str(input())
    print("Enter an adjective:")
    Adj2 = str(input())


    # The next major part prints out the statement with the users noun and adjective inputs
    # are inputed into the print statements that are f strings. Finishing the prints.
    print(f"Roses are {Adj1}")
    print(f"{No1} are blue")
    print(f"{No2} is {Adj2}")
    print("And so are you!")

# Running this function is at the end is running the whole process above to run.
mad_lib()
