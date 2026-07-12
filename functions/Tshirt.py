def make_shirt(size, text):
    print(f"Your new Tshirt has a size of {size}, and it says {text}" )

make_shirt("S", "Hello World!") #Positional Arguments, Python will read them in order and assign them to the parameters in the order provided.
make_shirt(text = "Hello Python!", size = "M") #Keyword Arguments, by providing the name of the argument, python knows to which parameter it belongs each piece of data.


