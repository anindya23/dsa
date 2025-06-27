class Anagram:
    # Anagram with sorting where time complexity is O(1)
    def anagramWithSorting(self, s, t) -> bool:
        return sorted(s) == sorted(t)
    # Time Complexity O(n) but space complexity O(S + T) because of two extra hashmap
    def isAnagram(self, s, t) -> bool:
        mapS, mapT = {}, {}

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            mapS[s[i]] = 1 + mapS.get(s[i], 0)
            mapT[t[i]] = 1 + mapT.get(t[i], 0)

        for j in mapS:
            if mapS[j] != mapT.get(j, 0):
                return False
        return True


if __name__ == '__main__':
    obj = Anagram()
    print(obj.anagramWithSorting('Anindya', 'aydninA'))