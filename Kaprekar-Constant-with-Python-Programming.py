#Kaprekar Constant with Python Programming

def kaprekar(num): # We define the Kaprekar function

    if num == 6174: # If the number is 6174, the operation is finished and the result is printed
        print("Result: 6174")
        return

    while num != 6174: # A loop is started which continues until the number is 6174
        digits = [int(d) for d in str(num)] # Separate the digits of the number and assign them to an array

        while len(digits) < 4: # Add a leading zero until the array has 4 digits
            digits.insert(0, 0)

        # New numbers are obtained by ordering the numbers from small to large and from large to small
        ascending = int(''.join(map(str, sorted(digits))))
        descending = int(''.join(map(str, sorted(digits, reverse=True))))
        
        # The difference between the new numbers is calculated and assigned to the variable num for the next iteration
        num = descending - ascending

        # Operation steps and result are printed on the screen
        print(f"{descending:04d} - {ascending:04d} = {num:04d}")

kaprekar(1000) # Enter your randomly selected 4-digit number and start the function, for this code I chose the number 1000.