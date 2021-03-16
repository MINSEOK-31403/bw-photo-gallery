def myfunc():
    print("Hello")

if __name__ == "__main__":
    myfunc()

import csv
f = open('write1.csv', 'r', encoding='utf-8')
rdr = csv.reader(f)
for line in rdr:
  print(line)
f.close()

def total1 (w1, w2, w3, w4, w5, w6, w7, w8, w9, w10, w11, w12, w13, w14, w15):

    def my_strings():
        print('a', 'b', 'c', 'd', 'e')

my_strings = ()  
my_numbers = ['<90','<80','<70', '<60','<50']

results = list(map(lambda x, y: (x, y), my_strings, my_numbers))

print(results)



if total1> 90:                     
     print('a')                
if 90>total1>= 80:
    print('b')
if 80>total1>= 70:
    print('c')
if 70>total1>= 60:
    print('d')
if 60>total1:
    print('e')
