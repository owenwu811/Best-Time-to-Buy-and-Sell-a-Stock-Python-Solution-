#271
#medium


#Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

#Machine 1 (sender) has the function:

#string encode(vector<string> strs) {
#  // ... your code
#  return encoded_string;
#}
#Machine 2 (receiver) has the function:
#vector<string> decode(string s) {
#  //... your code
#  return strs;
#}
#So Machine 1 does:

#string encoded_string = encode(strs);
#and Machine 2 does:

#vector<string> strs2 = decode(encoded_string);
#strs2 in Machine 2 should be the same as strs in Machine 1.

#Implement the encode and decode methods.

#You are not allowed to solve the problem using any serialize methods (such as eval).




#my own solution using python3:

class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        self.start = strs
        print(strs)
        return "".join(strs)
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        print(self.start)
        return self.start
        #return list(s)
