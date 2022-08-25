def min_pieces(original, desired):
    l = len(desired)
    output = []

    for i in range(0, l):
        temp = [original[x:x + l] for x in range(0, l, i + 1)]
        output.append(temp)
    
    return output

original = [1, 4, 3, 2]
desired = [1, 2, 4, 3]
print(min_pieces(original, desired))


'''
    response = 0
    lenght = len(original)
    
    for x, i in enumerate(original):
        counter = 0
        # if original[x] == desired[x]:
        #     counter += 1
        for n in range(0, lenght):
            if original[x] == desired[n]:
                counter += 1
            else:
                break
        if counter > 0:
            response += 1
            counter = 0

    return response
'''