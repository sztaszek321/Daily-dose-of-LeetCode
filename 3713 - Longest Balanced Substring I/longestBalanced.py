from collections import Counter

class Solution:
    def longestBalanced(self, s: str) -> int:
        l = len(s)
        if l > 1000 or l < 1 or not s.isalpha() or not s.islower():
            return 0

        result = 0

        f = [0] * 26

        for i in range(l):

            f = [0] * 26 #empty list of occurrences a-z 1

            for j in range(i+1, l+1):

                f[ord(s[j-1]) - 97] += 1

                t = 0 #number of occurrences
                b = True #flag

                for k in f:
                    if k == 0:
                        continue
                    if t == 0:
                        t = k
                    elif k != t:
                        b = False
                        break

                if b:
                    result = max(result, j - i)
                    best = s[i:j]

        print(result)
        return result

txt1 = "abbac" #4
txt2 = "zzabccy" #4
txt3 = "aba" #2
txt4 = "gigfjjfijfhiihhgfijhgghiiighifijhhgfijhhggijhiggjghjfifhiiiffhfjhigigjggfgiijhfijghihgjgjigijfhifhgifgiihhijifigfihfjfjgjhgghhjhjifffgfghfhjhiighhjhifgfififfhiiifhffjjgijiifjghijgifghgiiggfjfjfjijiifhfiggigfihhhgggfhijijhghjfgfjhfgigfjjfhjjfijihhjiihffgggfghifjfggifjhfhgfihjhifgfihfffiijiggjfjiifjifigjjhigiiihjfghgigjihggjigijhhfigjgiggigjfgjhgjfggjffiiifhggiffifhgffiifgghhhifjfffjhjiihghfgihifgggjiihfjjfhfgjifigifihhfigjhhijjgfffggfjiighhhfgjgijihifjijjgjjjjggigjigfiiijijjhihjfijgggiffhhfgihijhijjjhhfgigifigfjhigiijigiifijiihgijhhjfiijiiihfhghjfgfigjfjjjfghfghiifhjgggihffjfhhhiffjjhfgjigjjhhggffjffifghgjgjhffhigghfiffjhgffjifhijjgihfgjjfhjjghihhfhifghfiijgjigfihfififjfhjhjhiggfjhhgigighiggjijiffiffjggjjjhjjjgjjfhjghigjjjhfhjgfifgjfgghjihjjffghhiifjfjffijfighgiffhifhffihffighjggijfjggfjfijhjjiffjiiighfgighihfgijigjigjjgjfjiiiiijfghihfhhjhjfjjggffhjjgjfjgihffjfhjhgjjhiijjhhgfhffgjjhfijhijhghijfjjfffgggi"
txt5 = "dedbecdceaccceedeacccacaeaeabadddaabdeaaccecaddcacdddbddeededecdcbecdcdcaeccaedeeadcbabaaabbdcdbbbdbbbddececdabddaedaeabdaaeedbdbdedaedbeaaecadadccadbacedceecdbaecaacceccacabbeadcdacaeecedccbbdaaedebbaabceecddccccbddacaecbedbddeaceacebcbbcabebceceadbbdbdddaaabcbeebaaaabbeeebdbdaababedcbcbbaccabecacebeaecebedeacdeabcbebcacbadbdaaebbcdaddedcebaeabeaedebebddcadebaddbdbbdbebaceaaecaccabacdcedbcabdacaadeabebbdbbbbcebdbaaccabdbebacadcaacbeedabddcbaadbecbcbcacbdaacadeddcedbbadcabebcacdbedbaaddcdeabbadbbcdaaeacabcbaaaddbbeccdbcdaabbecddaeaccabdeacaabbedabbdedadaccbbdebdbeacddbaeeeabbccbbabdccaeaeebdcdebeddbbcceabcabacdcebacddddadabeccbddcbdabbeceeecacaacedadaadabddcaceccdbbecaebbeeadacaddddaadcbebbdcbededdbaabadedbadcccbdcdbbeccceeedabbaaebdecaebedbcccbdddbcdcbadcdcabbcbaeaeabccbbaaadbbdceeccbbaaebeeceeadcdcccebeecdaddebaedeeaddebddeccbeabeccadacbcadeebedbeebbedaaedbbeddccaaabeabbcdababddcaebbecdebdcd"
sol = Solution()
sol.longestBalanced(txt4)
