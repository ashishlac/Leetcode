class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        hashmap = {
            "0": "0",
            "1": "1",
            "00":"0",
            "01":"1",
            "10":"1",
            "11":"10",
            "110":"11",
            "111":"11"
        }
        self.stack = []
        l1 = len(a)
        l2 = len(b)
        if len(a) < len(b):
            a, b = b,a
            l1, l2 = l2, l1
        temp = ""
        carry = "0"
        i = 1
        while i  <= l1:
            if i <= l2:
                temp = hashmap[a[-(i)] + "" +b[-(i)]]
            else:
                temp = hashmap[a[-i]]
            if carry == "1":
                temp = hashmap [carry +"" + temp ]
                carry = "0"
            
            if temp == "10" or temp == "11":
                carry = "1"
                self.stack.append(temp[-1])
                
                if i == l1:
                    self.stack.append(temp[-2])
            else:
                self.stack.append(temp)
            i += 1
        return ''.join(self.stack[::-1])