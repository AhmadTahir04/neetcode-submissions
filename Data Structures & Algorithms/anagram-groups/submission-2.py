class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for word in strs:
            count = [0] * 26

            for char in word:
                # update correct position in count
                index = ord(char) - ord('a')
                count[index] += 1
            # use count as a key somehow
            key = tuple(count)
            # add word to that group
            if key not in groups:
                groups[key] = []
            groups[key].append(word)
        return list(groups.values())