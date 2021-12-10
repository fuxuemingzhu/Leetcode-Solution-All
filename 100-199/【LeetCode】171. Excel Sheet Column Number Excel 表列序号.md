作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

[LeetCode]

题目地址：[https://leetcode.com/problems/excel-sheet-column-number/](https://leetcode.com/problems/excel-sheet-column-number/)

Total Accepted: 77115 Total Submissions: 185238 Difficulty: Easy


## 题目大意

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
    ...

Example 1:

	Input: "A"
	Output: 1

Example 2:
	
	Input: "AB"
	Output: 28

Example 3:

	Input: "ZY"
	Output: 701

## 解题方法

典型的26进制题目啊！没啥难度。

重点是26进制中每一位对应的26的多少次幂。不要搞错。另外，为了防止计算时间过
长，而且避免数据转化，没有采用Math.exp的方法。直接手撸26的次幂。

### Java解法

算法如下：

```java
public class Solution {
    public int titleToNumber(String s) {
        int answer=0;
        char[] nums=s.toCharArray();
        for(int i=0; i<nums.length; i++){
            int temp=nums[i]-'A'+1;//字幕代表的数字是多少
            for(int j=0; j<nums.length-i-1; j++){//注意循环的次数
                temp*=26;
            }
            answer+=temp;
        }
        return answer;
    }
}
```

AC:2ms

### Python解法

python的代码总是那么短。

```python
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        for c in s:
            res = 26 * res + ord(c) - ord("A") + 1
        return res
```

## 日期

2016/4/30 14:42:55 
2018 年 11 月 11 日 —— 剁手节快乐
