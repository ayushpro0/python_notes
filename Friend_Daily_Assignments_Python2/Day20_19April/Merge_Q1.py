'''Q1. Merge and Sort List
The list of 'n' numbers is given to the student of 3rd class by the Maths teacher. And another 'n' numbers are given to another student.  Now they both have to merge the given numbers which were given by the Maths teacher. After merging the two set of list elements, then they have to write those merge elements in the sorted order.
Help the students to write a program.
So, in this program enter the two lists of length 3, and print them in the sorted order.

Input Format:
The first line of input consists of an integer which corresponds to a size of both the lists.
The second line of input consists of an 'n' integer values which correspond to elements of the list1.

Output Format:
The first line of output consists of merge list which is having elements from both the lists.
The second line of output consists of sorting order of merge list.
Refer the Sample Input Output.

Note:
[All the bold text corresponds to input and rest corresponds to output]

Sample Input and Output:  
Enter the length of the list:
3
Enter the elements forfirst list:
57 2 12
Enter the elements forsecond list:
11 14 1
Merging of two lists:
[57, 2, 12, 11, 14, 1]
Sorted list:
[1, 2, 11, 12, 14, 57]
'''

n = int(input("Enter the length of the list: \n"))
lis1 = list(map(int, input("Enter the elements forfirst list:\n").split()))
lis2 = list(map(int, input("Enter the elements forsecond list:\n").split()))

for i in lis2:
    lis1.append(i)

print("Merging of two lists:\n", lis1)
print("Sorted list:\n",sorted(lis1))
