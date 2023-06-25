#name = ['Jenny','Ram','Shyam']
#for i in name:
#    print(i)
#    if i =='Jenny':
#        print("Hey, it's me! ")

numbers = (2,3,4,-2,10)
square_list=[]
square_set=set()
square_tuple=tuple()

for i in numbers:
    square = i**2
    #square_list.append(square)
    #square_set.add(square)
    square_tuple = square_tuple + (square,)
print("The set of squares are: ", square_tuple)

    #square_list[1]=10
    #print(square_list)
    #square_list[j]=square

#    square_list[i] = square

#print("The list of squares are: ", square_list)

