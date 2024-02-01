

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t): return ""
        tdict, matched, l, start, windowlenS = Counter(t), 0, 0, 0, len(s) + 1
        for r, sch in enumerate(s):
            if sch in tdict:
                tdict[sch] -= 1
                if tdict[sch] == 0:
                    matched += 1
            while matched == len(tdict):
                if windowlenS > r - l + 1:
                    start = l
                    windowlenS = r - l + 1
                removedchar = s[l]
                l += 1
                if removedchar in tdict:
                    if tdict[removedchar] == 0:
                        matched -= 1
                    tdict[removedchar] += 1
        if windowlenS < len(s):
            return s[start:start + windowlenS]
        elif windowlenS == len(s):
            return s
        else:
            return ""



#explanation: ORIGINALLY, our tdict represents what we need from s to satisfy t: 'a': 1, 'b': 1, 'c': 1. as we find t's characters from s, we now say we need ONE LESS FROM S. if we shrink the window, we take the character - a - we kicked out of the left side of the window and saw we now still need one MORE OF THAT CHARACTER FROM S by incrementing the dictionary value - a: 0 becomes a: 1 - to say we still need one more A from s to satisfy t. 
#explanation 2: ONLY WHAT IS IN OUR WINDOW CURRENTLY can count towards our allowance from s to satisfy t. We only shrink the window once by kicking the character out from the leftmost side of our window, and if the character - a - we kicked out counted towards the allowance towards satisfying t, we must take this allowance away once since we only shrink by a character ONCE and increment the count in the dictinoary to say we still need one more a - 'a': 0 becomes 'a': 1 to say we still need one more a to satisfy t



#my solution - python3:

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t): return ""
        startsaver = 0
        endsaver = len(s) + 1
        ws = 0
        matched = 0
        tdict = Counter(t)
        for we, schar in enumerate(s):
            if schar in tdict:
                tdict[schar] -= 1
                #only matched when we satisfy all occurences of a character 
                if tdict[schar] == 0:
                    matched += 1
            while matched == len(tdict):
                if endsaver > we - ws + 1:
                    startsaver = ws
                    endsaver = we - ws + 1
                kickout = s[ws]
                ws += 1
                if kickout in tdict:
                    #only if we completely satisfied the character in t do we rollback our progress on matched  
                    if tdict[kickout] == 0:
                        matched -= 1
                    #we need one more
                    tdict[kickout] += 1
        if len(s) > endsaver:
            return s[startsaver:startsaver + endsaver]
        elif len(s) == endsaver:
            return s
        else:
            return ""

#important: matched variable tracks the frequency of characters from s that have fully satisified t. so means how many letters in the dictionary have values of 0 - a:0, b: 0, c: 1 - matched would be 2 because 2 letters - a and b - from s have FULLY SATISFIED t




#another practice run - my own solution in python3:

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #note that, even if we comment out the 1st line, the algorithm still works 
        if len(s) < len(t): return ""
        startsaver = 0
        endsaver = len(s) + 1
        tdict = Counter(t)
        fullysatisfied = 0
        ws = 0
        for we, schar in enumerate(s):
            if schar in tdict:
                tdict[schar] -= 1
                if tdict[schar] == 0:
                    fullysatisfied += 1
            while fullysatisfied == len(tdict):
                #since we've now found a solution, we're after the goal of finding the minimum window that satisfies t from s
                #we - ws + 1 is the new smaller but valid window
                if endsaver > we - ws + 1:
                    startsaver = ws
                    endsaver = we - ws + 1
                #whether we found a smaller window or not, we need to shrink the window
                kickoutchar = s[ws]
                ws += 1
                if kickoutchar in tdict:
                    if tdict[kickoutchar] == 0:
                        fullysatisfied -= 1
                    #as long as the left char we are kicking out is in tdict as a key, we need to reflect the fact that we need one more of that character now since we shrunk the window - this is independant of if we fully satisfied that character from s in t or not
                    tdict[kickoutchar] += 1
        #we finished looping through s, and endsaver represents the end of the smallest window that satisfies t
        if len(s) > endsaver:
            return s[startsaver: startsaver + endsaver]
        elif len(s) == endsaver:
            return s
        else:
            return ""



#super important: if you put "tdict[kickoutchar] += 1" before "if tdict[kickoutchar] == 0:" rather than after, then fullysatisfied -= 1 would never execute: to illustrate here, let's say it was supposed to be 'a': 0, which would decrement fully satisfied, but now that you've incremented it before, you would get 'a': 1, which wouldn't decrement fully satisfied now, messing up the result, causing the "while fullysatisfied == len(tdict)" to be true instead of false because you shrunk the window, so now s isn't fully satisfying t since the a from the beginning of s = ADOBECODEBANC is now gone from the window DOBEC, but this was never reflected in fully satisfied, leading to complete wrong results
                      

#2/1/24 practice:

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        tdict = Counter(t)
        startsaver = 0
        ws = 0
        matched = 0
        endsaver = len(s) + 1
        for we, schar in enumerate(s):
            #if schar exists in tdict as a key
            if schar in tdict:
                tdict[schar] -= 1
                #only when we fully satisfied that character from s in t do we increment matched by 1 because we want matched to equal the length of tdict aka the number of unique keys in tdict counting by the left column
                if tdict[schar] == 0:
                    matched += 1
            while matched == len(tdict):
                if endsaver > we - ws + 1:
                    #we found a new smallest window, so save those indicies and begin shrinking
                    startsaver = ws
                    endsaver = we - ws + 1
                kickout = s[ws]
                ws += 1
                #there's a possibility that the character we are kicking out from the left of the window is not a character in tdict
                if kickout in tdict:
                    #fully satisfied - if we made this <= 0, it would be incorrect because if a: 0, c: 0, b: -1, we have one more than enough Bs to satisfy t, so that dosen't mean we still need one more
                    if tdict[kickout] == 0:
                        matched -= 1
                    #we need one more allowance of that character
                    tdict[kickout] += 1
        if len(s) > endsaver:
            return s[startsaver: startsaver + endsaver]
        elif len(s) == endsaver:
            return s
        else:
            return ""
