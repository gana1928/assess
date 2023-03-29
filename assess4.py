import csv
from csv import DictWriter
print("before adding the new employee record")
with open('new.csv') as f:
   for line in csv.DictReader(f, fieldnames=('val1', 'val2',)):
      print(line)
   f.close()
field_names = ['emp_id','emp_name','dob','doj']
dict={
    'emp_id':'35105','emp_name':'ganadakshaka','dob':'27-05-2000','doj':'12-01-2023'
}

with open('new.csv','a') as f:
    dictwriter_object = DictWriter(f, fieldnames=field_names)
    dictwriter_object.writerow(dict)
    f.close()
print("after adding the new employee record")
with open('new.csv') as f:
   for line in csv.DictReader(f, fieldnames=('val1', 'val2',)):
      print(line)
   f.close()
