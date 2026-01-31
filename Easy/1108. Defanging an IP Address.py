# 1108. Defanging an IP Address
# Easy
# Topics
# premium lock icon
# Companies
# Given a valid (IPv4) IP address, return a defanged version of that IP address.

# A defanged IP address replaces every period "." with "[.]".

 

# Example 1:

# Input: address = "1.1.1.1"
# Output: "1[.]1[.]1[.]1"
# Example 2:

# Input: address = "255.100.50.0"
# Output: "255[.]100[.]50[.]0"
 

# Constraints:

# The given address is a valid IPv4 address.

class Solution:
    def defangIPaddr(self, address: str):
        return address.replace(".","[.]")
    

"""
learn from few previous problems that using built in functions is always better as they are optimized
and runs faster than custom implementations.
yet this not best solution as its taking 37ms, it is too much for such an easy problem.

"""