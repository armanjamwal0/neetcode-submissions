class Solution:
    def hasDuplicate(self, arr: List[int]) -> bool:
        hash_map = {}
        for i in range(len(arr)):
            if arr[i] not in hash_map:
                hash_map[arr[i]] = 1
            elif arr[i] in hash_map:
                hash_map[arr[i]]+=1

        for i in hash_map:
            if hash_map[i] > 1:
                return True
        return False