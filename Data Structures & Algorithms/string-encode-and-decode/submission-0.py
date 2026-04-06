class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        sizes , result = [], ""
        for word in strs:
            sizes.append(len(word))#[]
        for lengths in sizes:
            result += str(lengths)
            result += "," 
        result += "#"  #   "4,4,4,3,#""
        for words in strs:
            result += words
        return result #   "4,4,4,3,#neetcodeloveyou"

    def decode(self, s: str) -> List[str]:
        if not s:#""
            return []
        sizes, result, i = [], [], 0
        while s[i] != "#" : #3
            hashcut = "" #""
            while s[i] != ",":
                hashcut += s[i] #"3"
                i += 1
            sizes.append(int(hashcut)) #[4,4,4,3]
            i += 1 #8
        i += 1 # 9
        for size in sizes: #4
            result.append(s[i:i+size])#s[13:13+4] code
            i += size #13
        return result
        
        


        
        
