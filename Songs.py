#Delaney’s Disco wants to provide training sessions for their DJs. They want a computer program to be developed to ensure each training session runs smoothly.

#The program will ask for the duration of a training session. The DJ enters the duration of each song they will play. The program will add up the duration of all songs until the total is greater than or equal to the duration of the training session. At this point, the program tells the DJ they have selected enough songs to complete the training session.

#Key points:
#- The duration of the training session will be entered in minutes but stored as seconds.
#- The duration of the training session will between 10 and 30 minutes.  Invalid inputs will display an appropriate message.
#- The duration of each song will be entered in seconds.
#- When the final song is played in full, the training session duration may be longer than the original session duration entered by the user.

#The program should display:
#"Enough songs have been entered" once the total duration exceeds the entered time.
#The number of each song and the duration of them in seconds.
#The total length of the training session.


songCount = 0 
arr = []
total = 0
Count = 0
length = 0
Training_session = int(input("Enter the duration of the session in minutes: "))
while Training_session < 10 or Training_session > 30:
    print("Session duration should be between 10 and 30 minutes.  Try again")
    Training_session = int(input("Enter the duration of the session in minutes: "))
Training_session = Training_session*60
while total < Training_session:
    songs = int(input("Enter the songs in seconds: "))
    arr.append(songs)
    total = total + songs
    if total >= Training_session:
        print("Enough songs have been entered")
length = len(arr)
for i in range(length):
    Count = Count + 1
    print("Song " +str(Count)+ ": " +str(arr[i]))
print("Total duration: "+str(total)+ " seconds")
