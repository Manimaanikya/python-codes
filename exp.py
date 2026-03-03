a=int(input('a : '))
b=int(input('b : '))

try:
    print(a/b)
except Exception as e:
    print('error banthu',e)
else:

    print('yenu error illa')
finally:
    print('i dont care about errors')
