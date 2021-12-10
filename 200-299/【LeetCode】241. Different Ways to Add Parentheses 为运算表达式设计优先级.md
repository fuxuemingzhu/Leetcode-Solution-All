
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/different-ways-to-add-parentheses/description/

## 题目描述

Given a string of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. The valid operators are +, - and *.

    Example 1
    Input: "2-1-1".
    
    ((2-1)-1) = 0
    (2-(1-1)) = 2
    Output: [0, 2]
    
    
    Example 2
    Input: "2*3-4*5"
    
    (2*(3-(4*5))) = -34
    ((2*3)-(4*5)) = -14
    ((2*(3-4))*5) = -10
    (2*((3-4)*5)) = -10
    (((2*3)-4)*5) = 10
    Output: [-34, -14, -10, -10, 10]



## 题目大意

给一个式子加上括号，看能够成的所有式子的值。

## 解题方法

### 方法一：递归构建所有表达式

这个题仍然可以使用回溯。通过dict保存有效的加括号方案，使用内置函数eval计算结果。

```python
class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        exprDict = dict()
        nums, ops = [], []
        input = re.split(r'(\D)', input)
        for x in input:
            if x.isdigit():
                nums.append(x)
            else:
                ops.append(x)
        self.dfs(nums, ops, exprDict)
        return exprDict.values()

    def dfs(self, nums, ops, exprDict):
        if ops:
            for x in range(len(ops)):
                self.dfs(nums[:x] + ['(' + nums[x] + ops[x] + nums[x + 1] + ')'] + nums[x+2:], ops[:x] + ops[x+1:], exprDict)
        elif nums[0] not in exprDict:
            exprDict[nums[0]] = eval(nums[0])
```

### 方法二：分而治之

如果仔细想一想，能发现这个题和[95. Unique Binary Search Trees II](https://blog.csdn.net/fuxuemingzhu/article/details/80778651)基本一模一样，都是分别求出左右的式子的值，然后再用循环拼接在一起。

方法是，循环遍历式子中的每个位置，如果这个位置是运算符，那么把左右的式子分别计算值，然后用运算符拼到一起。如果上面这个遍历中没有遇到运算符，那么res数组就是空的，这时input是个数字，所以结果把这个数字放进去，再返回即可。

Python代码如下：

```python
class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        res = list()
        N = len(input)
        for i in range(N):
            if input[i] == "+" or input[i] == "-" or input[i] == "*":
                lefts = self.diffWaysToCompute(input[:i])
                rights = self.diffWaysToCompute(input[i+1:])
                for left in lefts:
                    for right in rights:
                        if input[i] == "+":
                            res.append(left + right)
                        elif input[i] == "-":
                            res.append(left - right)
                        elif input[i] == "*":
                            res.append(left * right)
        if not res:
            res.append(int(input))
        return res
```

C++代码如下：

```cpp
class Solution {
public:
    vector<int> diffWaysToCompute(string input) {
        const int N = input.size();
        vector<int> res;
        for (int i = 0; i < N; ++i) {
            if (input[i] == '+' || input[i] == '-' || input[i] == '*') {
                vector<int> lefts = diffWaysToCompute(input.substr(0, i));
                vector<int> rights = diffWaysToCompute(input.substr(i + 1));
                for (int l : lefts) {
                    for (int r : rights) {
                        if (input[i] == '+')
                            res.push_back(l + r);
                        else if (input[i] == '-')
                            res.push_back(l - r);
                        else 
                            res.push_back(l * r);
                    }
                }
            }
        }
        if (res.empty())
            return {stoi(input)};
        return res;
    }
};
```

参考资料：

http://bookshadow.com/weblog/2015/07/27/leetcode-different-ways-add-parentheses/
http://www.cnblogs.com/grandyang/p/4682458.html

## 日期

2018 年 3 月 15 日 —— 雾霾消散，春光明媚
2018 年 11 月 15 日 —— 时间太快，不忍直视
2019 年 2 月 22 日 —— 这周结束了

  [1]: http://blog.csdn.net/fuxuemingzhu/article/details/79559645
