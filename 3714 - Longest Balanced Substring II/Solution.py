class Solution:
    def longestBalanced(self, s: str) -> int:
        l = len(s)
        ss = set(s)
        if l > 100000 or l < 1 or not s.isalpha() or not s.islower() or ss - set("abc") :
            return 0

        #only 1 letter in s
        if not ss - set("a") or not ss - set("b") or not ss - set("c") :
            return l

        result = 0

        for i in range(l):

            A = B = C = 0 #variables of occurrences a-c

            for j in range(i+1, l+1):

                if s[j-1] == "a":
                    A += 1
                if s[j-1] == "b":
                    B += 1
                if s[j-1] == "c":
                    C += 1

                if (A == B and C == 0) or (B == C and A == 0) or (A == C and B == 0) or (A == B == C) or (A == B == 0) or (A == C == 0) or (B == C == 0):
                    result = max(result, j - i)
                else:
                    continue

        print(result)
        return result

txt1 = "abbac" #4
txt2 = "zzabccy" #4
txt3 = "aba" #2
txt4 = "gigfjjfijfhiihhgfijhgghiiighifijhhgfijhhggijhiggjghjfifhiiiffhfjhigigjggfgiijhfijghihgjgjigijfhifhgifgiihhijifigfihfjfjgjhgghhjhjifffgfghfhjhiighhjhifgfififfhiiifhffjjgijiifjghijgifghgiiggfjfjfjijiifhfiggigfihhhgggfhijijhghjfgfjhfgigfjjfhjjfijihhjiihffgggfghifjfggifjhfhgfihjhifgfihfffiijiggjfjiifjifigjjhigiiihjfghgigjihggjigijhhfigjgiggigjfgjhgjfggjffiiifhggiffifhgffiifgghhhifjfffjhjiihghfgihifgggjiihfjjfhfgjifigifihhfigjhhijjgfffggfjiighhhfgjgijihifjijjgjjjjggigjigfiiijijjhihjfijgggiffhhfgihijhijjjhhfgigifigfjhigiijigiifijiihgijhhjfiijiiihfhghjfgfigjfjjjfghfghiifhjgggihffjfhhhiffjjhfgjigjjhhggffjffifghgjgjhffhigghfiffjhgffjifhijjgihfgjjfhjjghihhfhifghfiijgjigfihfififjfhjhjhiggfjhhgigighiggjijiffiffjggjjjhjjjgjjfhjghigjjjhfhjgfifgjfgghjihjjffghhiifjfjffijfighgiffhifhffihffighjggijfjggfjfijhjjiffjiiighfgighihfgijigjigjjgjfjiiiiijfghihfhhjhjfjjggffhjjgjfjgihffjfhjhgjjhiijjhhgfhffgjjhfijhijhghijfjjfffgggi"
txt5 = "dedbecdceaccceedeacccacaeaeabadddaabdeaaccecaddcacdddbddeededecdcbecdcdcaeccaedeeadcbabaaabbdcdbbbdbbbddececdabddaedaeabdaaeedbdbdedaedbeaaecadadccadbacedceecdbaecaacceccacabbeadcdacaeecedccbbdaaedebbaabceecddccccbddacaecbedbddeaceacebcbbcabebceceadbbdbdddaaabcbeebaaaabbeeebdbdaababedcbcbbaccabecacebeaecebedeacdeabcbebcacbadbdaaebbcdaddedcebaeabeaedebebddcadebaddbdbbdbebaceaaecaccabacdcedbcabdacaadeabebbdbbbbcebdbaaccabdbebacadcaacbeedabddcbaadbecbcbcacbdaacadeddcedbbadcabebcacdbedbaaddcdeabbadbbcdaaeacabcbaaaddbbeccdbcdaabbecddaeaccabdeacaabbedabbdedadaccbbdebdbeacddbaeeeabbccbbabdccaeaeebdcdebeddbbcceabcabacdcebacddddadabeccbddcbdabbeceeecacaacedadaadabddcaceccdbbecaebbeeadacaddddaadcbebbdcbededdbaabadedbadcccbdcdbbeccceeedabbaaebdecaebedbcccbdddbcdcbadcdcabbcbaeaeabccbbaaadbbdceeccbbaaebeeceeadcdcccebeecdaddebaedeeaddebddeccbeabeccadacbcadeebedbeebbedaaedbbeddccaaabeabbcdababddcaebbecdebdcd"
txt6 = "aabcc"
txt7 = "acababbcbaabacbcbbbbacaaaaccbbbbabcbccbcaaaccccabaabcacabbbbaccbaacabcbbbcaccbbccacabbcbcccaacccaaaaabcaabbbcccabcbbbabcaabaccaacabbccbbabacacaabacaabbcaccbacbccaaaaacccaacccaacabcbbccaabcbbbcabacacbabbcbbcaacbbbaaabaacabacbccbcabaccaabcabbaacabcababbccaccbacabcacbcccababaababcccbbbaacbbccbcbcabaacabaccbcbbcccbabcacbcccbcaccabbacaabcababbcabbcccbbbaaacbccabbbcaccccccbcccababaaaabaaabaabbbbabbacabbabaacbaabcbbbababcaacbaacaaacaacbcbbaaccbbbcbcbccaccbabbbabcccaacbccabbaacaccccccababccacbabccbcbbcbbbacacaabaacbbaaabaaabbcbbbcabbaabaabaabbabaaccababcbbabaacacaacbcccbbccacabbacbaaabccbcbacabcabcbbccbcbcaaacaacaaccaacacbccacbcaaccbacaacccbbbccacabaccbbaaccabbbaacbcaccbacbbcbaaabbaabcbbaccaabaaabccaabbccacbabcbabbcbccbcabbaccccbcccabccaababbaaacaabbacbabbbcbabbcbabccccbccbcbbccabbcaccbcbbbcccbbaacaaaccababcacbcabccbcacccbbacaccbacbacacbcabbbbccabcabcccbbbababbcaabbbcabcacccccbbbccaccbcaccabaaccbbbbcbaacaacbcacccaaabacaacccacacabcacacacbaaabaabbbbbbabacccbcbccbcbcbbcaacbcaacbacaabbbaaabacbbbbacbbaabccabaccaccacbbbbabbbbcbbaabbccbbbbccbccbbbabbacabcacbcabaabbacaaabaabcabacbaa"
txt8 = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
txt9 = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaac"
sol = Solution()
sol.longestBalanced(txt9)