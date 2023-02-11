# Tip Calculator

# set up our loop!
# first, we must make an assumption.  our assumption is that we want to
# compute the tip on a restaurant bill.  we can express this assumption
# by creating a variable that is holding a specific value (in this case
# the value is the String "yes")
# this variable is sometimes referred to as a "control variable"
compute_tips = 'yes'

# next we can ask Python to start a loop. this loop will execute as long
# as our "compute_tips" varialbe is holding the value "yes"
# note that the first time we encounter this loop the value of "compute_tips"
# will be "yes" because we set up this variable on the previous line
while compute_tips == 'yes':
    # get bill amount
    bill = float(input("Enter bill amount: "))
    rate = float(input("Enter tip rate (i.e. 0.15): "))

    # calculate tip
    print("Your tip: ", bill * rate)

    # ask the user if they want to continue
    compute_tips = input('Do you want to continue? Type yes or no ')

    # note that we are overwriting the "compute_tips" variable on the previous line
    # once we reach the end of the loop Python will jump back up to the beginning of
    # the "while" loop and re-evaluate the condition.  if the user typed the word
    # "yes" then the condition evalutes to True (compute_tips == 'yes') -- but if they
    # type "no" (or anything else) the condition will evaluate to False and the loop
    # will not execute again.

print("thanks for using our program")
