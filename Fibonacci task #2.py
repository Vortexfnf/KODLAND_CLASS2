Numbers = [0, 1]

count = int(input("How many numbers do you want? "))

while len(Numbers) != count:
    Sum = Numbers[-2] + Numbers[-1]
    Numbers.append(Sum)

n_objective = int(input("Type an objective: "))

closest_number = Numbers[0] # Initializes the closest number to the first Fibonacci number in the list
min_difference = abs(n_objective - closest_number) # Calculates the starting difference between the objective and closest number

for i in range(len(Numbers)):
    difference = n_objective - Numbers[i]  # Calculate the difference between the objective and the current Fibonacci number
    if difference < min_difference: 
        min_difference = difference # changes min_difference to difference because difference is less than min_difference 
        closest_number = Numbers[i] # Update the closest number if the current number has a smaller difference

print("The closest number to", n_objective, "in the Fibonacci sequence is:", closest_number)