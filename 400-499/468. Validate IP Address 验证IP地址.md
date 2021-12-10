# 【LeetCode】468. Validate IP Address 解题报告（Python）

标签（空格分隔）： LeetCode

作者： 		负雪明烛 
id：				fuxuemingzhu
个人博客：	http://fuxuemingzhu.me/

---

题目地址：https://leetcode.com/problems/validate-ip-address/description/

## 题目描述：

Write a function to check whether an input string is a valid IPv4 address or IPv6 address or neither.

IPv4 addresses are canonically represented in dot-decimal notation, which consists of four decimal numbers, each ranging from 0 to 255, separated by dots ("."), e.g.,``172.16.254.1``;

Besides, leading zeros in the IPv4 is invalid. For example, the address ``172.16.254.01`` is invalid.

IPv6 addresses are represented as eight groups of four hexadecimal digits, each group representing 16 bits. The groups are separated by colons (":"). For example, the address ``2001:0db8:85a3:0000:0000:8a2e:0370:7334`` is a valid one. Also, we could omit some leading zeros among four hexadecimal digits and some low-case characters in the address to upper-case ones, so ``2001:db8:85a3:0:0:8A2E:0370:7334`` is also a valid IPv6 address(Omit leading zeros and using upper cases).

However, we don't replace a consecutive group of zero value with a single empty group using two consecutive colons (::) to pursue simplicity. For example, ``2001:0db8:85a3::8A2E:0370:7334`` is an invalid IPv6 address.

Besides, extra leading zeros in the IPv6 is also invalid. For example, the address ``02001:0db8:85a3:0000:0000:8a2e:0370:7334`` is invalid.

Note: You may assume there is no extra space or special characters in the input string.

Example 1:

    Input: "172.16.254.1"
    
    Output: "IPv4"

    Explanation: This is a valid IPv4 address, return "IPv4".

Example 2:

    Input: "2001:0db8:85a3:0:0:8A2E:0370:7334"
    
    Output: "IPv6"
    
    Explanation: This is a valid IPv6 address, return "IPv6".

Example 3:

    Input: "256.256.256.256"
    
    Output: "Neither"
    
    Explanation: This is neither a IPv4 address nor a IPv6 address.

## 题目大意

给出了IPv4和IPv6的地址规范，求一个字符串属于哪类地址，如果都不属于，那么返回"Neither"。

## 解题方法

其实这种题本身不难，更多的工作在于审题和测试吧。所以做这个题应该把题目中所有的IP都复制到Testcase中进行测试。

我趟了一个坑，题目说的"::"这种v6地址是不合法的。。好吧，谁让你是出题官。

另外一个坑，题目说不包含特殊符号，但是在v4地址中仍然出现了"1e5"这种测试用例。。


```python
class Solution(object):
    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        if '.' in IP and self.checkIPv4(IP):
            return "IPv4"
        elif ':' in IP and self.checkIPv6(IP):
            return "IPv6"
        else:
            return "Neither"
        
    def checkIPv4(self, IP):
        numbers = IP.split('.')
        if len(numbers) != 4: return False
        for num in numbers:
            if not num or (not num.isdecimal()) or (num[0] == '0' and len(num) != 1) or int(num) > 255:
                return False
        return True
        
    def checkIPv6(self, IP):
        IP = IP.lower()
        valid16 = "0123456789abcdef"
        if "::" in IP: return False
        numbers = IP.split(':')
        if len(numbers) > 8: return False
        for num in numbers:
            if not num: continue
            if len(num) >= 5: return False
            for n in num:
                if n not in valid16:
                    return False
        return True
```

## 日期

2018 年 6 月 13 日 ———— 腾讯赛圆满结束！两个月修得正果哈哈～～


  [1]: http://bookshadow.com/weblog/2017/09/17/leetcode-valid-parenthesis-string/