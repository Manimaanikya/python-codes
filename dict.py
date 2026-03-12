dishes={
    'kannada':'netra',
    'english':'karan',
    'hindi':'padma',
    'acco':'sabiya',
    'eco':'harsya',
    'cs':'mani'
}
print(dishes)

#adding another one sub
dishes['bs']='sabiya'
print(dishes)

#update value
dishes['cs']='manikumar'
print(dishes)
#remove item
del dishes['eco']
print(dishes)

#printnig values
print(dishes.values())

#printnig keys
print(dishes.keys())
