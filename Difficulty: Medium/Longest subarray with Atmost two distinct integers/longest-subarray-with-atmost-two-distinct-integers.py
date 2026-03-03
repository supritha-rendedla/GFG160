class Solution:
    def totalElements(self, arr):
        # Code here
        left = 0
        max_len = 0
        freq = {}
        
        for right in range(len(arr)):
            # Add current element
            freq[arr[right]] = freq.get(arr[right], 0) + 1
            
            # If more than 2 distinct, shrink window
            while len(freq) > 2:
                freq[arr[left]] -= 1
                if freq[arr[left]] == 0:
                    del freq[arr[left]]
                left += 1
            
            # Update maximum length
            max_len = max(max_len, right - left + 1)
        
        return max_len