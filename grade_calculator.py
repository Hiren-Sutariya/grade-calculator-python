score = int(input("Enter Your score: "))

if score >= 101:
    print("please Verify your Grade Again")
    exit()

if score >= 90:
    print("Gread A")
elif score >= 80:
    print("Gread B")
elif score >= 70:
    print("Gread C")
elif score >= 60:
    print("Gread D")
else :
    print("Gread F")