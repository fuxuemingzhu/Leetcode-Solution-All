作者： 		负雪明烛 
id：				fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---

题目地址: https://leetcode.com/problems/super-pow/description/

## 题目描述：

Your task is to calculate ``a^b`` mod 1337 where a is a positive integer and b is an extremely large positive integer given in the form of an array.

Example 1:

    Input: a = 2, b = [3]
    Output: 8

Example 2:

    Input: a = 2, b = [1,0]
    Output: 1024

## 题目大意

实现a的b次方的函数。但是给出的b是超级巨大的，而且是用数组保存着每一位的。

## 解题方法

这个题是[50. Pow(x, n)][1]的拓展题，都是求幂的问题，但是这个题由于数值大，需要模1337，对于模什么数一般都是瞎选的，不用考虑这个题为什么模这个数。

我觉得这个题的难点在于，如何求数组表示的超级大的数字b次幂。原来是求幂也可以做展开，比如求2^23，相当于求(2^2)^10 * (2^3).也就是说把前面以求的结果求一次10次幂，然后再去求后面的幂。

注意这里每次计算的结果都要%1337，保留后面的部分。前面被模掉的部分对结果不影响的，所以不用顾虑太多，直接求模。

时间复杂度是O(N)，空间复杂度是O(1)。N是b的长度。

```python
class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        res = 1
        for x in b:
            res = self.pow(res, 10) * self.pow(a, x) % 1337
        return res
        
    def pow(self, a, b):
        if b == 0 or a == 1: return 1
        if b % 2:
            return a * self.pow(a, b - 1) % 1337
        return self.pow((a * a) % 1337, b / 2) % 1337
```


参考资料：

http://www.cnblogs.com/grandyang/p/5651982.html

## 日期

2018 年 10 月 7 日 —— 假期最后一天！！


  [1]: https://blog.csdn.net/fuxuemingzhu/article/details/82960833
