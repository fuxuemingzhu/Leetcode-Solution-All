作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/remove-duplicate-letters/


## 题目描述

Given a string which contains only lowercase letters, remove duplicate letters so that every letter appear once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

Example 1:

    Input: "bcabc"
    Output: "abc"

Example 2:

    Input: "cbacdcbc"
    Output: "acdb"


## 题目大意

从一组字符串中取字符，使得生成结果中每个字符必须出现一次而且只出现一次，并且要求所得结果是字符串顺序最小的。

## 解题方法

这个题的难点在于使得结果是字符串顺序最小。解题思路也是围绕这个展开。

先顺一下思路，首先，每个字符都必须要出现一次，那么当这个字符只有一次机会的时候，必须添加到结果字符串结尾中去，反之，如果这个字符的次数没有降为0，即后面还有机会，那么可以先把优先级高的放进来，把这个字符放到后面再处理。所以，我们可以使用一个栈，有点类似单调递增栈的意思，但其实并不是单调栈。我们的思路就是把还可以放到后面的字符弹出栈，留着以后处理，字符序小的插入到对应的位置。

首先，为了知道每个字符出现了多少次，必须做一次次数统计，这个步骤大家都是知道的。

然后，需要借助一个栈来实现字符串构造的操作。具体操作如下：

从输入字符串中逐个读取字符c，并把c的字符统计减一。

1. 如果当前字符c已经在栈里面出现，那么跳过。
2. 如果当前字符c在栈里面，那么：
    1. 如果当前字符c小于栈顶，并且栈顶元素有剩余（后面还能再添加进来），则出栈栈顶，标记栈顶不在栈中。重复该操作直到栈顶元素不满足条件或者栈为空。
    2. 入栈字符c，并且标记c已经在栈中。




python代码如下：

```python
class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        count = collections.Counter(s)
        stack = []
        visited = collections.defaultdict(bool)
        for c in s:
            count[c] -= 1
            if visited[c]:
                continue
            while stack and count[stack[-1]] and stack[-1] > c:
                visited[stack[-1]] = False
                stack.pop()
            visited[c] = True
            stack.append(c)
        return "".join(stack)
```


C++代码如下：

```cpp
class Solution {
public:
    string removeDuplicateLetters(string s) {
        unordered_map<char, bool> visited;
        unordered_map<char, int> counter;
        string res = "";
        for (char c : s) ++counter[c];
        for (char c : s) {
            --counter[c];
            if (visited[c]) {
                continue;
            }
            while (!res.empty() && counter[res.back()] && c < res.back()) {
                visited[res.back()] = false;
                res.pop_back();
            }
            res += c;
            visited[c] = true;
        }
        return res;
    }
};
```

参考资料：

https://www.jiuzhang.com/solution/remove-duplicate-letters/
https://www.jianshu.com/p/8d75723657ad
https://blog.csdn.net/u012050154/article/details/51604942
http://www.cnblogs.com/grandyang/p/5085379.html

## 日期

2019 年 1 月 8 日 —— 别熬夜，我都开始有黑眼圈了。。


  [1]: https://assets.leetcode.com/uploads/2018/12/29/bst_cameras_01.png
  [2]: https://assets.leetcode.com/uploads/2018/12/29/bst_cameras_02.png
