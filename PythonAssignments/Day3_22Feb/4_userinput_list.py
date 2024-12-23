# 4.Accept scores of a student for 5 topics from keyboard and then print the total score and % score.

score = [int(x) for x in input("Enter the score of 5 topics : ").split(":")]

print(score)

total_score = sum(score)
percentage = (total_score / 500) * 100
print("Total Score : ", total_score)
print("Percentage : ", percentage)

# OUTPUT
# Enter the score of 5 topics : 78:55:88:91:69
# [78, 55, 88, 91, 69]
# Total Score :  381
# Percentage :  76.2
