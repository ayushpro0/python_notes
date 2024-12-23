'''1.	Read given XML file movies.xml. Print the total count of movie details stored in it. Also display all Movie details '''

import xml.etree.ElementTree as ET
''''
tree = ET.parse('movies.xml')
root = tree.getroot()

#give the children of the tree
for child in root:
    print(child.tag, child.attrib)


ele = [elem.tag for elem in root.iter()]
elems = [elem for elem in root.iter()]
print(ele)

for movie in root.iter('movie'):
    print(movie.attrib)'''

tree = ET.parse('movies.xml')
root = tree.getroot()

tree.write("movies.xml")

tree = ET.parse('movies.xml')
root = tree.getroot()
c = 0
movie_list = []

for movie in root.iter('movie'):
    print(movie.attrib)
    movie_list.append(movie.attrib['title'])
    c+=1

print("total count of movie : ", c)
print()
print("Movie List:\n",movie_list)
print()

#only description:
#for description in root.iter('description'):
    #print(description.text)

i=0
for ele in root.iter():
    #print(movie_list[i])
    if i == 2:
        print("Movie: ",movie_list[0])
    elif i == 9:
        print("Movie: ",movie_list[1])
    elif i == 16:
        print("Movie: ",movie_list[2])
    elif i == 23:
        print("Movie: ",movie_list[3])

    print(ele.tag+' : '+ele.text)
    i+=1
    
    





