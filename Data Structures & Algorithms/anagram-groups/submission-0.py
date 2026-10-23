class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        for word in strs:
            flag = False
            for i in res:
                if sorted(word) == sorted(i[0]):
                    i.append(word)
                    flag = True
                    break
            if not flag:
                res.append([word])
        return res