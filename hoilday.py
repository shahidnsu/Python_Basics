# It is possible to name the days 0 through 6 where day 0 is Sunday and day 6 is Saturday. If you go on a wonderful holiday leaving on day number 3 (a Wednesday) and you return home after 10 nights you would return home on a Saturday (day 6) Write a general version of the program which asks for the starting day number, and the length of your stay, and it will tell you the number of day of the week you will return on.


staring_day = input("Please input starting day number ")

length_of_stay = input("Please enter length of your stay ")

staring_day = int(staring_day)
length_of_stay = int(length_of_stay)
return_day = (staring_day + length_of_stay ) % 7
print("You will return in ")
print(return_day) 