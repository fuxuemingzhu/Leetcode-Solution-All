作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

[LeetCode]

题目地址：[https://leetcode.com/problems/count-primes/](https://leetcode.com/problems/count-primes/)

Total Accepted: 36655 Total Submissions: 172606 Difficulty: Easy


## 题目描述

Count the number of prime numbers less than a non-negative number, n.

Example:

	Input: 10
	Output: 4
	Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

## 题目大意

计算小于n的素数有多少个。

## 解题方法


### 素数筛法

[http://blog.csdn.net/blitzskies/article/details/45442923](http://blog.csdn.net/blitzskies/article/details/45442923)  提示用[Sieve of Eratosthenes](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes)的方法。

素数筛法就是把这个数的所有倍数都删除掉，因为这些数一定不是素数。最后统计一下数字剩余的没有被删除的个数就好。

![在这里插入图片描述](https://upload.wikimedia.org/wikipedia/commons/b/b9/Sieve_of_Eratosthenes_animation.gif)

也是学习了。

Java解法。

重点是优化效率，每一步的效率都要优化。

用List都会效率低，最后用数组好了。


```java
/**
 * 统计质数的数目。使用数组，用列表效率低。
 *
 * @param n
 * @return
 */
public static int countPrimes3(int n) {

	//n个元素的数组，其实只用到了n-2个。多见了2个防止输入0的时候崩溃。
	int[] nums = new int[n];
	//把所有的小于n的大于2的数字加入数组里
	for (int i = 2; i < n; i++) {
		//注意计算质数从2开始的，而数组从0开始
		nums[i - 2] = i;
	}
	//统一的长度，优化计算
	int size = nums.length;
	//各种优化效率，只计算到sqrt(n)
	for (int i = 0; i * i < size; i++) {
		//获取数组中的数字
		int temp = nums[i];
		//如果不是0，则进行计算，否则直接跳过，因为这个数已经是之前的某数字的倍数
		if (temp != 0) {
			//把该数字的倍数都删去，因为他们都不是质数
			//int i1 = temp - 1  优化效率，是因为比如用5来删除数字的时候15=3*5已经被删除过了，所以从20=5*4开始删除
			for (int i1 = temp - 1; i + temp * i1 < size; i1++) {
				//如果这个数不是素数则被置0，置成其他的负数也一样，只是为了区分和统计
				//i + temp * i1,i是因为从当前数字开始，比如10是从5的位置开始计算位置
				nums[i + temp * i1] = 0;
			}
		}
	}
	return countNums(nums);
}

/**
 * 计算数组中的0出现了多少次
 *
 * @param nums
 * @return
 */
public static int countNums(int[] nums) {
	int size = nums.length;
	int zeros = 0;
	for (int num : nums) {
		if (num == 0) {
			zeros++;
		}
	}

	return size - zeros;
}
```

没必要把所有的数字都保存到一个数组里面，可以直接记录和数字对应的位置的数字是不是质数。如果不是质数，则在对应位置保存true.最后统计不是true的，即质数的个数即可。

这个方法可以通用下去。类似的统计的题目只记录对应的位置是否满足条件，最后统计符合条件的个数。

```java
/**
 * 统计质数的数目。使用数组，用列表效率低。
 *
 * @param n
 * @return
 */
public static int countPrimes4(int n) {

	//n个元素的数组，其实只用到了n-2个。多见了2个防止输入0的时候崩溃。
	boolean[] nums = new boolean[n];
	//各种优化效率，只计算到sqrt(n)
	for (int i = 2; i * i < n; i++) {
		//获取数组中的数字是不是为0
		//不是质数则为true
		boolean temp = nums[i];
		//如果不是true，说明不是质数，则进行计算，否则直接跳过，因为这个数已经是之前的某数字的倍数
		if (!temp) {
			//把该数字的倍数都删去，因为他们都不是质数
			//int i1 = temp - 1  优化效率，是因为比如用5来删除数字的时候15=3*5已经被删除过了，所以从20=5*4开始删除
			for (int j = i; i * j < n; j++) {
				//如果这个数不是素数则被置true
				//i + temp * i1,i是因为从当前数字开始，比如10是从5的位置开始计算位置
				nums[i * j] = true;
			}
		}
	}
	return countNums2(nums);
}

/**
 * 计算数组中的不是素数的false出现了出现了多少次
 *
 * @param nums
 * @return
 */
public static int countNums2(boolean[] nums) {
	int notZeros = 0;
	for (int i = 2; i < nums.length; i++) {
		if (!nums[i]) {
			notZeros++;
		}
	}

	return notZeros;
}
```

二刷，使用Python解法，速度很慢，勉强通过了。

```python
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums = [True] * n
        for i in xrange(2, n):
            j = 2
            while i * j < n:
                nums[i * j] = False
                j += 1
        res = 0
        for i in xrange(2, n):
            if nums[i]:
                res += 1
        return res
```

C++版本如下：

```cpp
class Solution {
public:
    int countPrimes(int n) {
        vector<bool> nums(n, true);
        for (int i = 2; i < n; i++) {
            int j = 2;
            while (i * j < n) {
                nums[i * j] = false;
                j ++;
            }
        }
        int res = 0;
        for (int i = 2; i < n; i++) {
            if (nums[i]){
                res ++;
            }
        }
        return res;
    }
};
```

C++数组初始化需要使用memset，而且数组的大小n不能是0，数组解法如下。

```cpp
class Solution {
public:
    int countPrimes(int n) {
        if (n <= 0) return false;
        bool nums[n];
        memset(nums, true, sizeof(nums));
        for (int i = 2; i < n; i++) {
            int j = 2;
            while (i * j < n) {
                nums[i * j] = false;
                j ++;
            }
        }
        int res = 0;
        for (int i = 2; i < n; i++) {
            if (nums[i]){
                res ++;
            }
        }
        return res;
    }
};
```

## 参考资料

[http://blog.csdn.net/blitzskies/article/details/45442923](http://blog.csdn.net/blitzskies/article/details/45442923)

[https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes#cite_note-horsley-1](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes#cite_note-horsley-1)

[http://blog.csdn.net/xudli/article/details/45361471](http://blog.csdn.net/xudli/article/details/45361471)

## 日期

2015/10/19 23:38:24   
2018 年 11 月 29 日 —— 时不我待
