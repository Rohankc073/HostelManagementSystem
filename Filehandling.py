# f=open('student.txt',mode='w')
# print('File name :',f.name)
# print('File mode: ',f.mode)
# print('File Readable :',f.readable())
# print('File writeable',f.writable())
# print('File closed:',f.closed)
# f.close()
# print('File closed:',f.closed)

# import os
# print(os.path.isfile('student.txt'))

# import os
# if os.path.isfile('student.txt'):
#     f=open('student.txt')
#     print('File opened ')
#     f.close()
# else:
#     print('File not found')

# import os
# os.remove('student.txt')

# f=open('student.txt','w')
# f.write('Rohan')
# f.close()
#
# f=open('student.txt','w')
# n=f.write('Hello')
# print(n)

# f.close()

# f=open('student.txt','a')
# lst=['ram\n','rohan\n','shyam\n','giri\n']
# f.writelines(lst)
# f.close()
# print('Success')

# f=open('student.txt','r')
# data=f.read()
# print(data)
# f.close()
# print('Completed')

# f=open('student.txt','r')
# data=f.read(10)
# print(data)
# f.close()
# print('complete')

# f=open('student.txt','r')
# data=f.readline()
# print(data,end='')
# f.close()
#
# f=open('student.txt','r')
# data=f.readlines()
# print(data,end='')
# f.close()
#
# f=open('student.txt','r')
# data=f.readlines()
# for i in data:
#     print(i, end='')
# f.close()
# print('complete')
#
# f=open('student.txt','w+')
# f.write('hello')
# f.seek(0)
# b=f.read()
# print(b)
# f.close()

#rb wb

#=============================================PICKLE==========================================
#to pickle dump and dumps
#to unpickle loads and load
import pickle
# f=open('student.txt','wb')
# dct={'1':'Ram','2':'Hari'}
# pickle.dump(dct,f)
# f.close()

# #Load 'Unpickle '
# f=open('student.txt','rb')
# d=pickle.load(f)
# print(d)
# f.close()

#USing DUMPS AND LOADS
# dict1={1:'abc',2:'hari'}
# pickle_dict1=pickle.dumps(dict1)
# print(pickle_dict1)

# #USING LOADS
# dict1={1:'abc',2:'hari'}
# pickle_dict1=pickle.dumps(dict1)
# print(pickle_dict1)
# dict2=pickle.loads(pickle_dict1)
# print(dict2)


#===========================================CSV FILE ===============================
import csv
with open('abc,csv','w',newline='') as f:
    csv_reader=csv.writer(f)
    for i in range(2):
        n=input('Enter Name')
        a=input('Enter Address')
        csv_reader.writerows([n,a])
    print('Store Successfully ')








