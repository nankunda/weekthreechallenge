def list_sort(lista):
    
    even = []
    odd = []
    character = []
    mydict = dict()
    if not isinstance(lista, list):
        return 'Invalid Input'

    if not lista:
        mydict['evens'] = even
        mydict['odds'] = odd
        mydict['chars'] = character
        return mydict

    for i in lista:

        if isinstance(i, int):
            if i % 2 == 0:
                even.append(i)

            else:
                odd.append(i)

        elif isinstance(i, str):
            character.append(i)

    mydict['evens'] = sorted(even)
    mydict['odds'] = sorted(odd)
    mydict['chars'] = sorted(character)
    return mydict


print(list_sort([1, 3, 5, 'a', 'b']))
