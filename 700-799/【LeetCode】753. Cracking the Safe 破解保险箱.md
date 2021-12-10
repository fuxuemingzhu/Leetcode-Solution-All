作者： 		负雪明烛 
id：				fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---

题目地址: https://leetcode.com/problems/cracking-the-safe/description/

## 题目描述：

There is a box protected by a password. The password is ``n`` digits, where each letter can be one of the first ``k`` digits ``0, 1, ..., k-1``.

You can keep inputting the password, the password will automatically be matched against the last ``n`` digits entered.

For example, assuming the password is ``"345"``, I can open it when I type ``"012345"``, but I enter a total of 6 digits.

Please return any string of minimum length that is guaranteed to open the box after the entire string is inputted.

Example 1:

    Input: n = 1, k = 2
    Output: "01"
    Note: "10" will be accepted too.

Example 2:

    Input: n = 2, k = 2
    Output: "00110"
    Note: "01100", "10011", "11001" will be accepted too.

Note:

1. n will be in the range [1, 4].
1. k will be in the range [1, 10].
1. k^n will be at most 4096.

## 题目大意

题目描述是一个智能门锁，这个门锁只识别最近的n个字符，只要有连续的n个字符输入对了，前面无论输入什么都无所谓。那么，让我们求一个最短的万能钥匙串，能破解这个门锁的所有可能密码。

## 解题方法

显而易见，如果要这个万能钥匙串足够短，那么可以预料的是，每个密码都复用前面的密码，那么最优情况下就是，每个密码复用前面的n - 1位密码。额，这个数学问题叫做``De Bruijin sequence``，已经证明了每个可能的密码都可以在一个万能钥匙串中出现并且只出现一次。（Leetcode出这样的题也是让人没辙）

n位的密码锁，每个位置可以有k个数，所以总的可能性是k ^ n个。然后我们从前n位是0的状态开始，每次在后面添加一个新的字符，同时使用set保存这个出现过的新密码。当新密码的种类数等于 k ^ n时，搜索截止。

数学上已经郑明，这样的串是最短的串，而且，能解决所有可能的密码数。

python由于是值传递，可以通过给函数传list的方式，直接修改list内会导致外边的List也变化，但是传string不行。string是不可变的对象，函数内部修改string不会影响到外边。因此，如果需要动态生成字符串，可以把string变成list当做函数的参数。

时间复杂度是O(Nlog(N))，空间复杂度是O(N)。

```python
class Solution(object):
    def crackSafe(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        res = ["0"] * n
        size = k ** n
        visited = set()
        visited.add("".join(res))
        if self.dfs(res, visited, size, n, k):
            return "".join(res)
        return ""
        
    def dfs(self, res, visited, size, n, k):
        if len(visited) == size:
            return True
        node = "".join(res[len(res) - n + 1:])
        for i in range(k):
            node = node + str(i)
            if node not in visited:
                res.append(str(i))
                visited.add(node)
                if self.dfs(res, visited, size, n, k):
                    return True
                res.pop()
                visited.remove(node)
            node = node[:-1]
```

参考资料：

http://www.cnblogs.com/grandyang/p/8452361.html
https://www.youtube.com/watch?v=kRdlLahVZDc

## 日期

2018 年 10 月 5 日 —— 转眼假期要结束了！！
