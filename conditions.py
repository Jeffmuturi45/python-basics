marks = int(input("Enter your marks: "))

if marks >= 80:
    print(f"{marks} gives an A ")
elif marks >= 79:
    print(f"{marks} gives an B ")
elif marks >= 59:
    print(f"{marks} gives an C ")
elif marks >= 49:
    print(f"{marks} gives an D ")
elif marks >= 40:
    print(f"{marks} gives an E ")
else:
    print(f"{marks} gives an F ")