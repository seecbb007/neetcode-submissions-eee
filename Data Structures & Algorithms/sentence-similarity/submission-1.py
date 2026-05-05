class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1)!= len(sentence2):
            return False

        setsentences = set()
        for u,v in similarPairs :
            setsentences.add((u,v))
            setsentences.add((v,u))

        for s1,s2 in zip(sentence1,sentence2):
            if s1 != s2 and (s1,s2) not in setsentences:
                return False
        return True