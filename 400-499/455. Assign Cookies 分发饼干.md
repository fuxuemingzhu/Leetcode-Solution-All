
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

[LeetCode]

题目地址：[https://leetcode.com/problems/assign-cookies/][1]

 - Difficulty: Easy

## 题目描述

Assume you are an awesome parent and want to give your children some cookies. But, you should give each child at most one cookie. Each child ``i`` has a greed factor ``gi``, which is the minimum size of a cookie that the child will be content with; and each cookie ``j`` has a size ``sj``. If ``sj >= gi``, we can assign the cookie ``j``to the child ``i``, and the child ``i`` will be content. Your goal is to maximize the number of your content children and output the maximum number.

Note:

1. You may assume the greed factor is always positive. 
1. You cannot assign more than one cookie to one child.

Example 1:

	Input: [1,2,3], [1,1]
	
	Output: 1
	
	Explanation: You have 3 children and 2 cookies. The greed factors of 3 children are 1, 2, 3. 
	And even though you have 2 cookies, since their size is both 1, you could only make the child whose greed factor is 1 content.
	You need to output 1.

Example 2:

	Input: [1,2], [1,2,3]
	
	Output: 2
	
	Explanation: You have 2 children and 3 cookies. The greed factors of 2 children are 1, 2. 
	You have 3 cookies and their sizes are big enough to gratify all of the children, 
	You need to output 2.


## 题目大意

我们需要把饼干分给一群小孩，每个小孩最多只有一个饼干。每个小孩有自己的欲望，每个饼干有自己的大小，给小孩分饼干的时候最少也要给他欲望大小的饼干。求能让多少个小孩满意。

## 解题方法

明显的贪心算法，尽可能给小孩满足他欲望的最小饼干。

### Java解法

这个题目简单的思路就是：

1、首先把两个数组排序
2、如果当前满足感小于等于饼干，两个指针都后移，否则，只有满足感后移，然后再和当期前的满足感比较
3、最后返回指向孩子满足感指针的指针位置

```java
public class Solution {
    public int findContentChildren(int[] g, int[] s) {
        Arrays.sort(g);
        Arrays.sort(s);
        int i=0, j=0;
        while(i<g.length && j<s.length){
            if(g[i]<=s[j])
                i++;
            j++;
        }
        return i;
    }
}
```

AC:17ms

### Python解法

二刷，Python解法。


```python
class Solution:
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        sp = 0
        res = 0
        for gi in g:
            while sp < len(s) and s[sp] < gi:
                sp += 1
            if sp < len(s) and s[sp] >= gi:
                res += 1
                sp += 1
        return res
```

## 日期

2017 年 1 月 7 日 
2018 年 11 月 16 日 —— 又到周五了！

  [1]: https://leetcode.com/problems/assign-cookies/
