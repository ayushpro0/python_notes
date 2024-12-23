'''4.Accept scores of a student for 5 topics from keyboard and then print the total score and % score.'''

score = []
for i in range(5):
    sc = int(input("Enter {} number: ".format(i+1)))
    score.append(sc)
print("Total score out of 500: ", sum(score))

percen = (sum(score)/500)*100
print("Percentage: ", percen)
