class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        # step 1 : create dict for first word


        d1 ={}
        d2 ={}
        output = []

        for char in words[0]:
            if char not in d1:
                d1[char] = 1
            else:
                d1[char]+=1


        #step 2: iterate over other two words
        for index in range(1, len(words)):
            #check if chars in word 2 are present in word1. Also condsider the pointer
            print(words[index])
            for char in words[index]:
                #print(char)
                if char in d1 and d1[char] > 0:
                    d1[char] = d1[char] - 1
                    if char not in d2:
                        d2[char] = 1
                    else:
                        d2[char]+=1
            d1 = d2
            d2 = {}

        for key, value in d1.items():
            for i in range(0,value):
                output.append(key)
        return output