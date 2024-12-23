
import re
s="Welcome to aPSLb. *PSL&, Pune psl"
patt1 =r"PSL";
m = re.findall(patt1,s)
print ("m = ", m)                         #m =  ['PSL', 'PSL']   list will be returned
if m!=None:
    print ("Match Found = ",m)            #Match Found =  ['PSL', 'PSL']
else:
    print ("Match Not found!!!")

print ("---------------------------------")
print (re.findall('car', 'car'))          #['car']
print (re.findall('car', 'scary'))        #['car']
print (len(re.findall('car', 'carry the tarcardi to the car')))  #['car', 'car', 'car']

#find all occurance of PSL
print ("---------------------------------")

#print count of "car" in original string
