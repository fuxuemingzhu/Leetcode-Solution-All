作者： 		负雪明烛 
id：				fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---

题目地址: https://leetcode.com/problems/3sum-with-multiplicity/description/

## 题目描述：

Given an integer array A, and an integer target, return the number of tuples ``i, j, k``  such that ``i < j < k`` and ``A[i] + A[j] + A[k] == target``.

As the answer can be very large, return it modulo ``10^9 + 7``.

 

Example 1:

    Input: A = [1,1,2,2,3,3,4,4,5,5], target = 8
    Output: 20
    Explanation: 
    Enumerating by the values (A[i], A[j], A[k]):
    (1, 2, 5) occurs 8 times;
    (1, 3, 4) occurs 8 times;
    (2, 2, 4) occurs 2 times;
    (2, 3, 3) occurs 2 times.

Example 2:

    Input: A = [1,1,2,2,2,2], target = 5
    Output: 12
    Explanation: 
    A[i] = 1, A[j] = A[k] = 2 occurs 12 times:
    We choose one 1 from [1,1] in 2 ways,
    and two 2s from [2,2,2,2] in 6 ways.
 

Note:

- 3 <= A.length <= 3000
- 0 <= A[i] <= 100
- 0 <= target <= 300

## 题目大意

在一个数组中找出有多少组合的和是target。


## 解题方法

看到3sum直接就3sum走起啊！因为需要统计总共出现的次数，那么直接暴力肯定是不行的，需要我们先统计每个数字出现了多少次，过会进行一个查找和组合。使用了set和list来保存去重的数字。

两重循环i, j，分别对应了第一二个数字，需要注意的是第二个数字和第一个数字相同，所以j从i开始向后遍历。第三个数字等于target减去前两个数字，比较重要的一步是需要判断第三个数字要不比第二个数字小，而且第三个数字必须在set中，因为第三个数字不能向前找，得向后找，而且可以等于第二个数字！

如果把上面的a, b, c全都找到了，那么底下的方法就很简单了，求一个组合数字！从counter里面知道每个数字出现了多少次，判断一下，这三个数字是不是都不相等、有两个相等、三个全相等，这三种情况，然后就知道了总的数字组合会出现多少次。

最后最后，需要模一个数，就是因为忘了求模，导致又浪费了一次提交。。

时间复杂度是O(N^2)，空间复杂度是O(N)。

```python
class Solution(object):
    def threeSumMulti(self, A, target):
        """
        :type A: List[int]
        :type target: int
        :rtype: int
        """
        count = collections.Counter(A)
        Aset = set(A)
        Alist = list(Aset)
        Alist.sort()
        _lenA = len(Alist)
        res = 0
        for i in range(_lenA):
            for j in range(i, _lenA):
                c = target - Alist[i] - Alist[j]
                if c >= Alist[j] and c in Aset:
                    if Alist[i] != Alist[j] != c:
                        res += count[Alist[i]] * count[Alist[j]] * count[c]
                    elif Alist[i] == Alist[j] and Alist[j] != c:
                        res += count[c] * self.caculate(count[Alist[i]], 2)
                    elif Alist[j] == c and Alist[i] != Alist[j]:
                        res += count[Alist[i]] * self.caculate(count[Alist[j]], 2)
                    elif Alist[i] == c and Alist[j] != c:
                        res += count[Alist[j]] * self.caculate(count[c], 2)
                    else:
                        res += self.caculate(count[Alist[i]], 3)
        return res % (10 ** 9 + 7)
    
    def caculate(self, x, i):
        if i == 2:
            return x * (x - 1) / 2
        elif i == 3:
            return x * (x - 1) * (x - 2) / 6
```


参考资料：


## 日期

2018 年 10 月 14 日 —— 周赛做出来3个题，开心
