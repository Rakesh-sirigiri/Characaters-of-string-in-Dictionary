inp_str = input("enter a string =")
out = {x : inp_str.count(x) for x in set(inp_str)}
print("Occurence of all characters in",inp_str,"is :\n " + str(out))
