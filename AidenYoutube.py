#Aidan has a YouTube channel and wants to calculate how many watch-hours he requires to gain monetisation.

#"Monetisation" is a status that can be earned when a channel gains 4000 watch hours.

#Assuming that each subscriber will give the same average watch time, calculate the required number of subscribers to hit 4000 hours based on the current subscriber count and the current watch hours.

#For example, if there are 100 subscribers and a current watch hours of 400, that means an average of 4 hours per subscriber, and therefore it would take 1000 subscribers to hit 4000 hours.


Sub = float(input("Enter the number of Subscribers"))
Watch  = float(input("Enter the watch hours per sub"))
hours = Watch/Sub
watch_hours = 4000/hours
watch_hours = str(watch_hours)
print("You need "+ watch_hours+ " subscribers to hit 4000 watch hours.")
