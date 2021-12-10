标签（空格分隔）： LeetCode

作者： 		负雪明烛 
id：				fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/


[https://leetcode.com/problems/ugly-number-ii/](https://leetcode.com/problems/ugly-number-ii/)

Total Accepted: 12227 Total Submissions: 54870 Difficulty: Medium


## Question

> Write a program to find the n-th ugly number.


> Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.


## Examples

> For example, 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.


> Note that 1 is typically treated as an ugly number.



## Ways

### 方法一

最简单的方法就是遍历的方法，直接判断每个数是不是丑数，如果是就加入list中，这就是方法一。

但是这个方法效率太低，提交的时候连续三次都超出时间限制了。本地运行还是可以的。迫于无奈，必须提高效率。

### 方法二

所有的 ugly number 都是由 1 开始，乘以 2/3/5 生成的。

只要将这些生成的数排序即可获得，自动排序可以使用 set

这样每次取出的第一个元素就是最小元素，由此再继续生成新的ugly number.

可以分成如下三组：

> (1) 1×2, 2×2, 3×2, 4×2, 5×2, …
> 
> (2) 1×3, 2×3, 3×3, 4×3, 5×3, …
> 
> (3) 1×5, 2×5, 3×5, 4×5, 5×5, …

使每个组已经用过的数字删除掉，这样列表中只有一个元素，获取三个组的最小值之后就计算下一个丑数。

```java
public static int nthUglyNumber2(int n) {
	List<Integer> num2List = new ArrayList<Integer>();
	List<Integer> num3List = new ArrayList<Integer>();
	List<Integer> num5List = new ArrayList<Integer>();

	num2List.add(1);
	num3List.add(1);
	num5List.add(1);

	int test = 0;

	for (int j = 0; j < n; j++) {
		//最小元素
		test = Math.min(Math.min(num2List.get(0), num3List.get(0)), num5List.get(0));

		//让列表中一直只有一个元素
		if (num2List.get(0) == test) num2List.remove(0);
		if (num3List.get(0) == test) num3List.remove(0);
		if (num5List.get(0) == test) num5List.remove(0);

		num2List.add(2 * test);
		num3List.add(3 * test);
		num5List.add(5 * test);
	}


	return test;
}
```
----
二刷，python

```python
class Solution(object):
    def nthUglyNumber(self, n):
        if n < 0:
            return 0
        dp = [1] * n
        index2, index3, index5 = 0, 0, 0
        for i in range(1, n):
            dp[i] = min(2 * dp[index2], 3 * dp[index3], 5 * dp[index5])
            if dp[i] == 2 * dp[index2]: index2 += 1
            if dp[i] == 3 * dp[index3]: index3 += 1
            if dp[i] == 5 * dp[index5]: index5 += 1
        return dp[n - 1]
```

## Reference

[http://blog.csdn.net/guang09080908/article/details/47780619](http://blog.csdn.net/guang09080908/article/details/47780619)

[http://blog.csdn.net/xudli/article/details/47903959](http://blog.csdn.net/xudli/article/details/47903959)

## Date

2015/10/18 20:57:01  

2018 年 8 月 28 日 ———— 雾霾天
