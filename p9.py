# wapp to track items in the trolly

items = ()

res = input("do u want to add something y/n ")
while res == "y":
	i = input(" enter item name ")
	items = items + (i,)
	res = input("do u want to add more y/n ")
print(items)

# to convert i into a tuple we have to add , ow it will show error