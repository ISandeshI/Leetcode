# 860. Lemonade Change
# Easy
# Topics
# premium lock icon
# Companies
# At a lemonade stand, each lemonade costs $5. Customers are standing in a queue to buy from you and order one at a time (in the order specified by bills). Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill. You must provide the correct change to each customer so that the net transaction is that the customer pays $5.

# Note that you do not have any change in hand at first.

# Given an integer array bills where bills[i] is the bill the ith customer pays, return true if you can provide every customer with the correct change, or false otherwise.

 

# Example 1:

# Input: bills = [5,5,5,10,20]
# Output: true
# Explanation: 
# From the first 3 customers, we collect three $5 bills in order.
# From the fourth customer, we collect a $10 bill and give back a $5.
# From the fifth customer, we give a $10 bill and a $5 bill.
# Since all customers got correct change, we output true.
# Example 2:

# Input: bills = [5,5,10,10,20]
# Output: false
# Explanation: 
# From the first two customers in order, we collect two $5 bills.
# For the next two customers in order, we collect a $10 bill and give back a $5 bill.
# For the last customer, we can not give the change of $15 back because we only have two $10 bills.
# Since not every customer received the correct change, the answer is false.
 

# Constraints:

# 1 <= bills.length <= 105
# bills[i] is either 5, 10, or 20.

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        cashArray = [0, 0, 0]

        for bill in bills:
            if bill == 5:
                cashArray[0] += 1

            elif bill == 10:
                if cashArray[0] == 0:
                    return False
                else:
                    cashArray[1] += 1
                    cashArray[0] -= 1

            elif bill == 20:
                if cashArray[1] > 0 and cashArray[0] > 0:
                    cashArray[2] += 1
                    cashArray[0] -= 1
                    cashArray[1] -= 1

                elif cashArray[0] > 2:
                    cashArray[2] += 1
                    cashArray[0] -= 3

                else:
                    return False
                
        return True
    

"""
This turn out to be worst solution with runtime 3ms beating only 76% + solutions and in memory beating 
only 66% + solutions.
Initialy at line 47 and 54 i wrote if statement. this gave runtime 7ms, because every condition was 
getting checked. We know for sure each bill is from distinct denomination, hence no need to check other
bill's conditions and we can save time.


we can improve runtime to 1ms by editing after line 54. there's no need to keep track of 20's bill,
we just have to check if we do have change or not.so following is code:

            else:
                if cashArray[1] > 0 and cashArray[0] > 0:
                    cashArray[0] -= 1
                    cashArray[1] -= 1

                elif cashArray[0] > 2:
                    cashArray[0] -= 3

                else:
                    return False
"""