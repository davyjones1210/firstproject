#Have a 3x3 Matrix, one position want to select at which
#want to hide my money under one of the elements
list1 = [1,1,1]
list2=[1,1,1]
list3=[1,1,1]
final_list=[list1,list2,list3]
#replace element 3x2 of matrix with x
position=input("Where do you want to hide money, separated by x?: ")
hide_in= position.split("x")
#print(hide_in)
#final_list[2][1] = 'x'
final_list[int(hide_in[0])-1][int(hide_in[1])-1] = 'x'
print(f"{final_list[0]}\n{final_list[1]}\n{final_list[2]}")