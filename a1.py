# 1) Ask user to enter the donation amount (1 to 100 tk) of 4 persons : amount1, amount2, amount3, amount4
# while taking input, convert them into integer for mathematical operations

amount1 = int( input("Person 1 please enter some amount, 100: ") )
amount2 = int( input("Person 2 please enter some amount, 100: ") )
amount3 = int( input("Person 3 please enter some amount, 100: ") )
amount4 = int( input("Person 2 please enter some amount, 100: ") )
# 2) store the sum of all 4 amounts in a variable called 'total_amount'
total_amount =amount1+amount2+amount3+amount4
# 3) Print the 'total_amount' with a message "Total amount recieved  = "
print (total_amount,"Total amount recieved")


# 4) Calculate the average of the total amount and store the value in a variable 'average'
avg = total_amount/4
print("Average amount : ", avg)

# exm : average = total_amount / 4


# 5) Find how many 100 tk notes are there in total_amount. 
note_1 = total_amount//100

#    Divide `total_amount` by 100 (whole number division) and store the value in a variable 'note_1'

# 6) Find the remaining amount after taking out 100tk notes from total_amount and store the value in
#    a variable 'remaning_amount'
remaining_amount = total_amount % 100
#    remaining_amount = total_amount % 100
# 7) Find how many 50 tk notes are there in the 'remaining_amount'
note_2 = remaining_amount // 50
#    Divide `remaining_amount` by 50 (whole number division) and store the value in a variable 'note_2'

# 9) Print note_1 with a message
print("Count of 100tk note: ", note_1)

# 10) Print note_2 with a message
print("Count of 50tk note:", note_2)


# 11) Calculate the percentage of total donation recieved'
per = (total_amount/400)*100
#    - Divide total_amount by 400 ( maximum possible donation is 400 tk )
#    - Then multiply it by 100
#    - Store the result in a variable 'perc'

# 12) Print 'perc' with a message
print("The percentege of money left",per)



4