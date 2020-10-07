name=input("Enter your name:")
#Get Credit Score from a user
credit_score=int(input("Enter your credit score:"))
while credit_score<0 or credit_score>850:
	print("Error your credit score cannot be negative")
	print("or be greater than 850")
	credit_score=int(input("Enter your credit score:"))
if 0<=credit_score< 579:
    print(name, "You're in the credit score range of poor, with a credit score of.",credit_score)
elif 580>= credit_score <= 669:
	print(name, "You're in the credit score range of fair with a credit score of:", credit_score)
elif 670>=credit_score <= 739:
    print(name, "You're in the credit score range of good, with a credit score of:", credit_score)
elif 740>=credit_score <= 799:
	print(name, "You're in the credit score range of very good, with a credit score of :", credit_score)
elif 800>= credit_score <= 850:
	print(name, "You're in the credit score range of excellent,with the credit score of: ", credit_score)
