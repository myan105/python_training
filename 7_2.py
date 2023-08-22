#Write a function called eval_loop that iteratively prompts the user, takes the resulting input and evaluates it using eval, 
#and prints the result.
#It should continue until the user enters 'done', and then return the value of the last 
#expression it evaluated.


def eval_loop():
    result = None
    while True:
        user_input = input("Enter a Python expression (or 'done' to exit): ")
        if user_input == 'done':
            break
        try:
            result = eval(user_input)
            print(result)
        except Exception as e:
            print("Error:", e)
    return result

last_result = eval_loop()
print("Last result:", last_result)
#output: Enter a Python expression (or 'done' to exit): 1+2+3
# 6