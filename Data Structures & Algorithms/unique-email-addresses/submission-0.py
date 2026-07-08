class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        email=""
        s1=""
        s2=""
        l1=[]
        char1="@"
        s0=""
        for mail in emails:

            email=mail.split("@")
            s1=email[0]
            s2=s1.split("+")
            for ch in s2[0]:
                if ch !=".":
                    s0+=ch 
            if s0+char1+email[1] not in l1:
                l1.append(s0+char1+email[1])
            s0=""
            s0=""
            email=""
            s1=""
            s2=""

        
        return len(l1)
         