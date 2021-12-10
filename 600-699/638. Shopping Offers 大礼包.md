
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/shopping-offers/description/

## 题目描述

In LeetCode Store, there are some kinds of items to sell. Each item has a price.

However, there are some special offers, and a special offer consists of one or more different kinds of items with a sale price.

You are given the each item's price, a set of special offers, and the number we need to buy for each item. The job is to output the lowest price you have to pay for exactly certain items as given, where you could make optimal use of the special offers.

Each special offer is represented in the form of an array, the last number represents the price you need to pay for this special offer, other numbers represents how many specific items you could get if you buy this offer.

You could use any of special offers as many times as you want.

Example 1:

    Input: [2,5], [[3,0,5],[1,2,10]], [3,2]
    Output: 14
    Explanation: 
    There are two kinds of items, A and B. Their prices are $2 and $5 respectively. 
    In special offer 1, you can pay $5 for 3A and 0B
    In special offer 2, you can pay $10 for 1A and 2B. 
    You need to buy 3A and 2B, so you may pay $10 for 1A and 2B (special offer #2), and $4 for 2A.

Example 2:

    Input: [2,3,4], [[1,1,0,4],[2,2,1,9]], [1,2,1]
    Output: 11
    Explanation: 
    The price of A is $2, and $3 for B, $4 for C. 
    You may pay $4 for 1A and 1B, and $9 for 2A ,2B and 1C. 
    You need to buy 1A ,2B and 1C, so you may pay $4 for 1A and 1B (special offer #1), and $3 for 1B, $4 for 1C. 
    You cannot add more items, though only $9 for 2A ,2B and 1C.

Note:

1. There are at most 6 kinds of items, 100 special offers.
1. For each item, you need to buy at most 6 of them.
1. You are not allowed to buy more items than you want, even if that would lower the overall price.


## 题目大意

可以直接按照原价price购买商品，也可以用一些套餐。套餐的价格用special给出，用户的需求用needs给出。求问怎么组合才能最便宜。

## 解题方法

### DFS

明显是DP的题目，但DFS没超时的话可以使用DFS解。

我们定义DFS返回的是对于当前的needs需要付出的最小价格。

因为这个题允许多次使用同一个套餐，所以这次dfs不需要像permutation一样记录位置，只需要保留我们如果直接购买或者套餐之后，剩余的商品数目即可。

dfs的做法是这样：求出直接购买这些商品的价格，然后遍历所有的套餐，看能不能使用这个套餐（判断的方式是使用套餐之后仍然还有剩余物品），保存所有情况下的最小值返回即可。

这种做法在remains全部是0的情况下，也会做一次遍历。但是注意不能改成min(remains) > 0的情况下才去继续遍历，因为有一个needs已经为0了的情况下，我们还要确保其他的needs都是0才可以。

我在写下面这个代码的时候，犯了一个大错：计算local_min的时候写成了``local_min = min(local_min, spec[-1]) + self.dfs(price, special, remains)``，这个错误不可饶恕啊！！

代码如下：

```python
class Solution(object):
    def shoppingOffers(self, price, special, needs):
        """
        :type price: List[int]
        :type special: List[List[int]]
        :type needs: List[int]
        :rtype: int
        """
        return self.dfs(price, special, needs)
    
    def dfs(self, price, special, needs):
        local_min = self.directPurchase(price, needs)
        for spec in special:
            remains = [needs[j] - spec[j] for j in range(len(needs))]
            if min(remains) >= 0:
                local_min = min(local_min, spec[-1] + self.dfs(price, special, remains))
        return local_min
        
    def directPurchase(self, price, needs):
        total = 0
        for i, need in enumerate(needs):
            total += price[i] * need
        return total
```

使用记忆化搜索可以加速计算，代码如下：

```python
class Solution(object):
    def shoppingOffers(self, price, special, needs):
        """
        :type price: List[int]
        :type special: List[List[int]]
        :type needs: List[int]
        :rtype: int
        """
        return self.dfs(price, special, needs, {})
    
    def dfs(self, price, special, needs, d):
        val = sum(price[i] * needs[i] for i in range(len(needs)))
        for spec in special:
            remains = [needs[j] - spec[j] for j in range(len(needs))]
            if min(remains) >= 0:
                val = min(val, d.get(tuple(needs), spec[-1] + self.dfs(price, special, remains, d)))
        d[tuple(needs)] = val
        return val
```

其实不用定义一个新的函数dfs()，因为我们可以看出dfs的参数和原函数一样的，所以直接用原函数进行递归更方便。

```python
class Solution(object):
    def shoppingOffers(self, price, special, needs):
        """
        :type price: List[int]
        :type special: List[List[int]]
        :type needs: List[int]
        :rtype: int
        """
        N = len(needs)
        res = sum(p * n for p, n in zip(price, needs))
        for sp in special:
            if all(sp[i] <= needs[i] for i in range(N)):
                remain = [needs[i] - sp[i] for i in range(N)]
                if min(remain) >= 0:
                    res = min(res, sp[-1] + self.shoppingOffers(price, special, remain))
        return res
```

### 回溯法

使用回溯法也能解决这个问题，使用了一个套餐之后，再进行回溯，看求得的结果是不是能更便宜。定义的helper函数就是用来计算在还有剩余needs的情况下的最小值。

```cpp
class Solution {
public:
    int shoppingOffers(vector<int>& price, vector<vector<int>>& special, vector<int>& needs) {
        return helper(price, special, needs, 0);
    }
    int helper(vector<int>& price, vector<vector<int>>& special, vector<int>& needs, int start) {
        const int N = price.size();
        int ans = 0;
        for (int i = 0; i < N; i++) {
            ans += price[i] * needs[i];
        }
        for (int i = start; i < special.size(); i++) {
            auto offer = special[i];
            int total = offer.back();
            for (int j = 0; j < N; j ++) {
                needs[j] -= offer[j];
            }
            if (*min_element(needs.begin(), needs.end()) >= 0) {
                total += helper(price, special, needs, i);
                ans = min(total, ans);
            }
            for (int j = 0; j < N; j++) {
                needs[j] += offer[j];
            }
        }
        return ans;
    }
};
```


参考资料：

https://leetcode.com/problems/shopping-offers/discuss/105212/Very-Easy-to-understand-JAVA-Solution-beats-95-with-explanation
https://leetcode.com/problems/shopping-offers/discuss/105204/Python-dfs-with-memorization.

## 日期

2018 年 9 月 7 日 —— 中午不睡，下午崩溃
2019 年 3 月 23 日 —— 今天也是元气满满的一天！
