from tabulate import tabulate
 
# assign data
mydata = [
    ["a",
     '''a
aa
a a
2a
[a]'''], 
    ["B",
     '''B
BB
2B
[B]'''], 
    ["5", '''5
55
5 5
25
[5]''']
]
 
# create header
head = ["Entrada", "Resultado"]
 
# display table
print(tabulate(mydata, headers=head, tablefmt="grid"))
