from collections import defaultdict
from typing import List

class GroupAnagram:
    def groupAnagram(self, items: List[str]) -> List[List[str]]:
        hashMap = defaultdict(list)

        for item in items:
            groupKey = [0] * 26

            for s in item:
                groupKey[ord(s) - ord('a')] += 1

            hashMap[tuple(groupKey)].append(item)

        return hashMap

