phone_no = {'Ram': 1234,
            'Shyam': 3456,
            'Mohan': 8976
}
#phone_no2 = {'Ram','Shyam','Mohan'}
#print(phone_no)
#print((phone_no['Mohan']))
#phone_no['Mohan']=9999
#print(phone_no)
#phone_no['Madhav']={1111,2222,3333}
#print(phone_no)
#phone_no['Shyam']={'Shyam_home':5555,'Shyam_work':4444}
print(phone_no)
# phone_no2 = phone_no.copy()
# print(phone_no2)
print(len(phone_no))

#del phone_no['Ram']
#print( phone_no.pop('Shyam'))
print(phone_no.values())

for k,v in phone_no.items():
    phone_no[k] = "7777"

print(phone_no)

#phone_no.clear()



#for i in phone_no.items():
    #print(i)
    #print(phone_no[i])

#print(phone_no)
#print(phone_no['Shyam']['Shyam_work'])
#print([phone_no.get('Ram')])

# data={
#     1:'jenny',
#     2:'Ram',
#     0:'Mohan'
# }
# print(data)
# print(data[0])