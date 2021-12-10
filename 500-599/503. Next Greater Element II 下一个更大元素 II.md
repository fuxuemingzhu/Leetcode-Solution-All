
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/minesweeper/description/

## 题目描述

Given a circular array (the next element of the last element is the first element of the array), print the Next Greater Number for every element. The Next Greater Number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, output -1 for this number.

    Example 1:
    Input: [1,2,1]
    Output: [2,-1,2]
    Explanation: The first 1's next greater number is 2; 
    The number 2 can't find next greater number; 
    The second 1's next greater number needs to search circularly, which is also 2.

Note: The length of given array won't exceed 10000.
    
## 题目大意

找出一个数组中每个数字的下一个更大的数字，可以看做是循环数组。

## 解题方法

### 暴力解法

额，直接使用暴力解法的话。可以使用``%``符号来实现循环数组。可惜超时了。

代码：

```python
class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        _len = len(nums)
        res = [-1] * _len
        for i in xrange(_len):
            for j in xrange(i + 1, _len * 2):
                if nums[j % _len] > nums[i]:
                    res[i] = nums[j % _len]
                    break
        return res
```

### 单调递减栈

下面的引用自 http://blog.csdn.net/Cloudox_/article/details/62881181

在遍历数组的过程中，如果是往后遇到大的数，那就是第一个更大的数，如果一直遇到不断小的数，才会一直找不到，我们可以用一个栈来记录，遇到比栈顶小的数字就放入栈中，遇到比栈顶大的数字就说明这是栈顶数字的下一个更大的数，就将其放在结果数组的对应位置上，栈顶的元素出栈，继续比较新的栈顶的数，如果还是大，那么继续记录，出栈，直到栈顶的数比新数要小，那么就可以将新数入栈了。因为我们要将找到的更大的数放在对应位置上，所以栈中记录的应该是元素位置，而不是具体的数字，但比较的时候还是比较原来的数组中这个位置的数字，这一点要想清楚。此外，因为会出现循环寻找的情况，所以数组我们可能遍历两次。这个做法会快很多。

官方解读的ppt做的很好~也推荐看下：https://leetcode.com/problems/next-greater-element-ii/solution/

注意，栈里保存的是索引，一定不要忘记。

同样适用单调栈的题目有：[962. Maximum Width Ramp](https://blog.csdn.net/fuxuemingzhu/article/details/85223568)

代码：

```python
class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [-1] * len(nums)
        stack = []
        for i in range(len(nums)) * 2:
            while stack and (nums[stack[-1]] < nums[i]):
                res[stack.pop()] = nums[i]
            stack.append(i)
        return res
```

C++代码如下：

```cpp
class Solution {
public:
    vector<int> nextGreaterElements(vector<int>& nums) {
        const int N = nums.size();
        vector<int> res(N, -1);
        stack<int> stack;
        for (int i = 0; i < N * 2; i++) {
            while (!stack.empty() && nums[stack.top()] < nums[i % N]) {
                res[stack.top()] = nums[i % N];
                stack.pop();
            }
            if (i < N)
                stack.push(i);
        }
        return res;
    }
};
```

## 日期

2018 年 3 月 6 日 
2018 年 12 月 28 日 —— 元旦假期到了

  [1]: https://leetcode.com/static/images/problemset/minesweeper_example_1.png
  [2]: https://leetcode.com/static/images/problemset/minesweeper_example_2.png
