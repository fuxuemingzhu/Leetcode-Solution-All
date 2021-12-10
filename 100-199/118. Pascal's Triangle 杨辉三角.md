作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

[LeetCode]

题目地址：[https://leetcode.com/problems/pascals-triangle/][1]

Total Accepted: 83023 Total Submissions: 247907 Difficulty: Easy


## 题目描述

Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.

![在这里插入图片描述](https://upload.wikimedia.org/wikipedia/commons/0/0d/PascalTriangleAnimated2.gif)

In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

	Input: 5
	Output:
	[
	     [1],
	    [1,1],
	   [1,2,1],
	  [1,3,3,1],
	 [1,4,6,4,1]
	]


## 题目大意

杨辉三角。

## 解题方法

### Java解法

智商呀！智商！大一的题竟然纠结的有一个小时！

最后找到错误的根源在于第10行的temp=new ArrayList();之前写的是temp.clear()；
这样的问题是clear()之后那个temp还在用，就是说如果下次修改temp的话会把原来已经放进去的给改了。

所以java基础很重要！

```java
public class Solution {
    public List<List<Integer>> generate(int numRows) {
        if(numRows<=0)  return new ArrayList();
		List<List<Integer>> answer=new ArrayList();
		List<Integer> temp=new ArrayList();
		temp.add(1);
		answer.add(temp);
		if(numRows==1)  return answer;
		for(int i=2;i<=numRows;i++){
			temp=new ArrayList();
			for(int j=0;j<i;j++){
				if(j==0 || j==i-1){
					temp.add(1);
				}else{
					temp.add(answer.get(i-2).get(j-1) + answer.get(i-2).get(j));
				}
			}
			answer.add(temp);
		}
		return answer;
    }
}
```
AC:2ms


### Python解法

二刷的时候采用的Python解法，而且我一遍就AC了，看到了两年前的答案还是觉得自己进步了的。

使用的方法是提前构造好三角形，然后再遍历每行的中间位置是上面两行的和即可。

```python
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = [[1 for j in range(i)] for i in range(1, numRows + 1)]
        for i in range(2, numRows):
            for j in range(1, i):
                res[i][j] = res[i - 1][j - 1] + res[i - 1][j]
        return res
```

## 日期

2016 年 05月 8日 
2018 年 11 月 19 日 —— 周一又开始了

  [1]: https://leetcode.com/problems/pascals-triangle/
