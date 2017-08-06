users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }


def studentsInstructorsFunc():#nested loop
     for key,value in users.items():
         print key
         counter=0
         for data in value:
             counter+=1
             first_name = data['first_name'].upper()#build-in method .upper()
             last_name = data['last_name'].upper()#build-in method .upper()
             length_total = len(first_name)+len(last_name)#build-in function len()
             print "{}-{} {}-{}".format(counter,first_name,last_name,length_total)


studentsInstructorsFunc()
