# Length Of Last Word

def lengthOfLastWord(self, s):
        i = len(s) - 1
        s = s.lower()
        count = 0

        while i >= 0:
            if ord(s[i]) >= ord("a") and ord(s[i]) <= ord("z"):
                count += 1
            elif count > 0:
                break
            i -= 1
        
        return count
        
