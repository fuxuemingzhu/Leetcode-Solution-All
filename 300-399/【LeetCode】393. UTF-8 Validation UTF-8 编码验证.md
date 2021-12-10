作者： 		负雪明烛 
id：				fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---

题目地址: https://leetcode.com/problems/utf-8-validation/description/

## 题目描述：

A character in UTF8 can be from 1 to 4 bytes long, subjected to the following rules:

For 1-byte character, the first bit is a 0, followed by its unicode code.
For n-bytes character, the first n-bits are all one's, the n+1 bit is 0, followed by n-1 bytes with most significant 2 bits being 10.
This is how the UTF-8 encoding would work:

       Char. number range  |        UTF-8 octet sequence
          (hexadecimal)    |              (binary)
       --------------------+---------------------------------------------
       0000 0000-0000 007F | 0xxxxxxx
       0000 0080-0000 07FF | 110xxxxx 10xxxxxx
       0000 0800-0000 FFFF | 1110xxxx 10xxxxxx 10xxxxxx
       0001 0000-0010 FFFF | 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx

Given an array of integers representing the data, return whether it is a valid utf-8 encoding.

Note:

The input is an array of integers. Only the ``least significant 8 bits`` of each integer is used to store the data. This means each integer represents only 1 byte of data.

Example 1:

    data = [197, 130, 1], which represents the octet sequence: 11000101 10000010 00000001.
    
    Return true.
    It is a valid utf-8 encoding for a 2-bytes character followed by a 1-byte character.

Example 2:

    data = [235, 140, 4], which represented the octet sequence: 11101011 10001100 00000100.
    
    Return false.
    The first 3 bits are all one's and the 4th bit is 0 means it is a 3-bytes character.
    The next byte is a continuation byte which starts with 10 and that's correct.
    But the second continuation byte does not start with 10, so it is invalid.

## 题目大意

判断一个字符的编码（不是一组）是不是有效的UTF-8编码。规则是：

> 对于UTF-8编码中的任意字节B，如果B的第一位为0，则B独立的表示一个字符(ASCII码)；
> 如果B的第一位为1，第二位为0，则B为一个多字节字符中的一个字节(非ASCII字符)；
> 如果B的前两位为1，第三位为0，则B为两个字节表示的字符中的第一个字节；
> 如果B的前三位为1，第四位为0，则B为三个字节表示的字符中的第一个字节； 如果B的前四位为1，第五位为0，则B为四个字节表示的字符中的第一个字节；


## 解题方法

注意题目让判断的是一个字符，这样就简单了很多。方法是使用位运算，首先判断首字符中的起始位置是什么，来知道后面跟着几个字符或者整个字符是个单独的字符，然后判断后面跟着的字符是不是都是以01开头的，个数是不是和第一个字符指示我们的相等。

时间复杂度是O(N)，空间复杂度是O(1)。N是给出的数据的长度。

```python
class Solution(object):
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        cnt = 0
        for d in data:
            if cnt == 0:
                if (d >> 5) == 0b110:
                    cnt = 1
                elif (d >> 4) == 0b1110:
                    cnt = 2
                elif (d >> 3) == 0b11110:
                    cnt = 3
                elif (d >> 7):
                    return False
            else:
                if (d >> 6) != 0b10:
                    return False
                cnt -= 1
        return cnt == 0
```


参考资料：

http://www.cnblogs.com/grandyang/p/5847597.html

## 日期

2018 年 10 月 8 日 —— 终于开学了。


  [1]: https://blog.csdn.net/fuxuemingzhu/article/details/82960833
