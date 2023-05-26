

def give_change(change, coins):
    # change is the amount
    # coins is an unsorted array containing all the possible coin types

    def _give_recursive(remaining_change, sorted_coins):
        # remaining_change: is the remaining value to get the change
        # sorted_coins: the available coins sorted in increasing order

        min_branch_count = float("inf")
        min_branch_coins = []

        for coin in reversed(sorted_coins):

            # 1) Can't use the coin - cuts the branch     
            if remaining_change < coin:
                continue
            
            # 2) When the coin is the exact remaining value
            if remaining_change == coin:
                return [coin]
            
            # 3) Finds the branch with the min coins count
            branch_coins = _give_recursive(remaining_change - coin, sorted_coins)

            if len(branch_coins) < min_branch_count:
                min_branch_count = len(branch_coins)

                # Concatenate the current coin with the branch
                min_branch_coins = [coin] + branch_coins

        return min_branch_coins

    return _give_recursive(change, sorted(coins))


def maximize_bag_weight(max_weight, cans_weight: list):
    # Maximizes the weight, trying to minimize the amount of cans. That's why sorting is used
    # Note that the max_weight isn't necessarily reached

    def _bag_recursive(remaining_weight, remaining_cans):
        
        max_weight_reached = -1
        max_weight_cans = []

        for can_weight in reversed(remaining_cans):
            
            # 1) Can't add to the bag - cuts branch
            if can_weight > remaining_weight:
                continue
            
            # 2) Exact required weight
            if can_weight == remaining_weight:
                return [can_weight]

            # 3) Tests with the cans left

            # Removes the can from the list
            cans_copy = remaining_cans.copy()
            cans_copy.remove(can_weight)            

            branch_cans = [can_weight] + _bag_recursive(remaining_weight - can_weight, cans_copy)

            # If the weight is greater
            branch_weight = sum(branch_cans)
            if branch_weight > max_weight_reached:
                max_weight_reached = branch_weight
                max_weight_cans = branch_cans

        return max_weight_cans
    
    return _bag_recursive(max_weight, sorted(cans_weight))


def longest_sub_sequence(numbers: list):
    # Done with brute force - seems like it should be done with dynamic programming

    def _longest_recursive(current_index, numbers):

        max_count = -1
        max_branch = []
        for i in range(current_index + 1, len(numbers)):

            if numbers[i] < numbers[current_index]:
                continue

            # Greater or equal passes
            branch = _longest_recursive(i, numbers)
            if len(branch) > max_count:
                max_count = len(branch)
                max_branch = [numbers[i]] + branch

        return max_branch
    

    longest = []
    for i in range(len(numbers)):
        
        sub_seq = [numbers[i]] + _longest_recursive(i, numbers)
        if len(sub_seq) > len(longest):
            longest = sub_seq

    return longest


def sum_subset(target, numbers):

    for number in numbers:

        # Cuts the branch
        if number > target:
            continue
        
        # Found - base case
        if number == target:
            return True

        remaining_copy = numbers.copy()
        remaining_copy.remove(number)
        if sum_subset(target - number, remaining_copy):
            return True

    return False
