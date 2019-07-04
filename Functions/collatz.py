# Solution to the practise problem from the page
# https://automatetheboringstuff.com/chapter3/

def collatz (number):
    if isinstance(number, int) == False:
        raise ValueError
    
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    else:
        print(3 * number + 1)
        return 3 * number + 1
if __name__ == "__main__":
    try:
        userNumber = int(input("Enter a number:\n"))
        
        while True:
            userNumber = collatz(userNumber)
            if userNumber == 1:
                break
        
    except ValueError:
        print("That is not a number")