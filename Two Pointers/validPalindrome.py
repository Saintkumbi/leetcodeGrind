class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Step 1: Preprocess the string using a list for efficient accumulation
        processed = []  # Initialize an empty list to collect alphanumeric characters

        for char in s:
            if char.isalnum():       # Check if the character is alphanumeric
                processed.append(char.lower())  # Convert to lowercase and append to the list

        # Convert the list of characters back to a single string
        pro = ''.join(processed)

        # Step 2: Initialize two pointers for comparison
        start = 0
        end = len(pro) - 1

        # Step 3: Use a while loop to compare characters from both ends
        while start < end:
            if pro[start] != pro[end]:
                return False       # Characters do not match; not a palindrome
            start += 1             # Move the start pointer forward
            end -= 1               # Move the end pointer backward

        return True                # All characters matched; it's a palindrome
