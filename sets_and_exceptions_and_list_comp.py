#sets: its an unordered collection and duplicates are not allowed
cats ={'Leopard','Tiger','Catello'}
dogs =() #empty set
dogs.add('Husky')
dogs.add('German Shepherd')
print(dogs)
dogs.add('Husky')#wont be added
#prints out of order, sets are unordered, this way it prevents duplicates








list_test = [2,4,6]
new_list_test = [members+1 for members in list_test]
print(new_list_test)

list = [0,3,4,0,21,1]
non_zero_list = [n for n in list if n!=0]
print(non_zero_list)

classes = ['ITEC 2544', 'ITEC 1111', 'ENGL 1232','MATH 3333']
itec_classes = [course for course in classes if course.startswith('ITEC')]
print(itec_classes)

num = [0,10,4,3,0,32]
doubled = [n *2 for n in num if n!=0]
print(doubled)