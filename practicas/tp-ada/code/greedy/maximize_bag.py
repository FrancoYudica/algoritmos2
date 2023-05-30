"""
We have a bag that can handle certain weight, called "max_weight".
    - There are k cans of weight C1, C2, C3, ..., CK
    - Each can has a "benefit" value B1, B2, B3, ..., BK

We wish to maximize the total "benefit", without exceeding the "max_weight"
"""

class Can:
    def __init__(self, tag, weight, benefit) -> None:
        self.tag = tag
        self.weight = weight
        self.benefit = benefit

# cans: list of Can
# max_weight: float
# returns: list of cans that maximize the bag
# The algorithm complexity is determined by the sorting, therefore O(n log(n))
def maximize_bag(cans, max_weight):

    # Sorts the can by benefit
    sorted_cans = sorted(cans, key=lambda can: can.benefit)

    accumulated_weight = 0
    selected_cans = []
    while accumulated_weight < max_weight and len(sorted_cans):
        can = sorted_cans.pop()

        #  Exceeds the weight limits
        if can.weight + accumulated_weight > max_weight:
            continue
        
        accumulated_weight += can.weight
        selected_cans.append(can.tag)

    return selected_cans