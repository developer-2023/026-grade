score = int(input("Score: "))
if 90 <= score <= 100: # score >= 90 and score <= 100
    print("A grade")
elif score >= 80:
    print("B grade")
elif score >= 70:
    print("C grade")
elif score >= 60:
    print("D grade")
else:
    print("F score")