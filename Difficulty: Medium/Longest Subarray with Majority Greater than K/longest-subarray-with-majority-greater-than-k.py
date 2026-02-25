class Solution:
    def longestSubarray(self, arr, k):
        # Code Here
        prefix = 0
        mp = {}
        ans = 0
        
        for i in range(len(arr)):
            
            # Convert to +1 / -1
            if arr[i] > k:
                prefix += 1
            else:
                prefix -= 1
            
            # Case 1: whole subarray valid
            if prefix > 0:
                ans = i + 1
            
            # Store first occurrence
            if prefix not in mp:
                mp[prefix] = i
            
            # Case 2: find smaller prefix
            if (prefix - 1) in mp:
                ans = max(ans, i - mp[prefix - 1])
        
        return ans