#Ask a student for the marks they got in the test out of 90.

#Calculate their percentage and if they get 70% or more, say "A Grade".  If they get 60% or more, say "B Grade".  If they get 50% or more, say "C Grade".  Otherwise, tell them "No grade".


mark = int(input("Enter your mark: "))
perc = mark/90*100
if perc >= 70:
    print("A Grade")
elif perc >= 60:
    print("B Grade")
elif perc >= 50:
    print("C Grade")
else:
    print("No grade")
