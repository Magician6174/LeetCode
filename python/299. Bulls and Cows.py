class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        
        
        d = {}
        nbi = []
        for i in range(len(guess)):
            if secret[i] == guess[i]:
                nbi.append(i)
            else:
                if secret[i] not in d.keys():
                    d[secret[i]] = 1
                else:
                    d[secret[i]] += 1
        nc = 0
        for i in range(len(guess)):
            if i not in nbi:
                if guess[i] in d.keys():
                    if d[guess[i]] > 0:
                        d[guess[i]] -= 1
                        nc += 1
        return str(len(nbi))+"A"+str(nc)+"B"
        
        """
        A = sum(a==b for a,b in zip(secret, guess))
        B = collections.Counter(secret) & collections.Counter(guess)
        return "%dA%dB" % (A, sum(B.values()) - A)
        """
