
def radix_sort(numbers):

    def get_digit_at(n, digit_index):
        # Given a number, returns the digit at the given position
        # digit_index starts in 0
        return (n // 10**digit_index) % 10

    # List in wich the numbers are placed. It's a list of lists
    place_list = [[] for _ in range(10)]

    current_digit = 0
    
    # With this flag, the loop will stop if all the digit for 
    # all the numbers is 0 at the current digit_index
    non_zero_max_digit = True

    while non_zero_max_digit:

        non_zero_max_digit = False

        # 1) Places the numbers in the list
        for number in numbers:
            digit = get_digit_at(number, current_digit)
            non_zero_max_digit |= digit != 0 
            place_list[digit].append(number)

        # Increases the digit index for next iteration
        current_digit += 1

        # 2) Then adds back the numbers to the numbers list, ready for the next step
        i = 0
        while i < len(numbers):
            
            for list_index in range(len(place_list)):
                for number in place_list[list_index]:
                    numbers[i] = number
                    i += 1
                
                # Clears the list for the next iteration
                place_list[list_index] = []

if __name__ == "__main__":
    l = [45, 3, 3, 5, 3,5 ,76, 7,4, 2, 4,5 , 6]
    radix_sort(l)
    print(l)


    