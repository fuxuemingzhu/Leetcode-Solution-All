
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/unique-binary-search-trees/description/


## 题目描述

Given ``n``, how many structurally unique BST's (binary search trees) that store values ``1...n``?

For example,
 
    Given n = 3, there are a total of 5 unique BST's.
    
       1         3     3      2      1
        \       /     /      / \      \
         3     2     1      1   3      2
        /     /       \                 \
       2     1         2                 3

## 题目大意

给了一个数字n，问n个节点的二叉树有多少种？

## 解题方法

### 记忆化递归

思路：从``1...n``中找出一个``i``作为根节点，比``i``小的数``1...i-1``作为左子树，比``i``大的数``i+1...n``作为右子树，左子树的排列和右子树的排列的乘积是此时的数目。

因为直接递归会超时，所以加上了记忆化搜索的方法，这样就快的多了。

```python
class Solution(object):
    def __init__(self):
        self.dp = dict()
    
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n in self.dp:
            return self.dp[n]
        if n == 0 or n == 1:
            return 1
        ans = 0
        for i in range(1, n + 1):
            ans += self.numTrees(i - 1) * self.numTrees(n - i)
        self.dp[n] = ans
        return ans
```

使用C++代码和上面类似，同样使用记忆化搜索能够完成。只不过，这里需要注意的一点是，左边的孩子数目是i的时候，右边的孩子数目因该是n - 1 - i，因为要去掉根节点。

代码如下：

```cpp
class Solution {
public:
    int numTrees(int n) {
        if (n == 0) return 1;
        if (m_.count(n)) return m_[n];
        int res = 0;
        for (int i = 0; i < n; i++) {
            int left = numTrees(i);
            int right = numTrees(n - 1 - i);
            res += left * right;
        }
        return m_[n] = res;
    }
private:
    unordered_map<int, int> m_;
};
```


### 动态规划

同样是上面的思路，如果使用动态规划去做，可以设dp[i]是i个节点的二叉树有多少种组合。那么，很明显和上面解法一样的，dp[i]等于左子树有0个节点，左子树有1个节点，左子树有2个节点……等等情况下的和。对于左右子树的组合方式是独立事件，所以总的组合数是左右子树相乘的关系。

完整的推导在下面，参照了：http://blog.csdn.net/u012501459/article/details/46622501

    给定一个数n，求1到n这些数可以构成多少棵二叉树。
    给定一个序列1.....n，为了构造所有二叉树，我们可以使用1......n中的每一个数i作为根节点，自然1......(i-1)必然位于树的左子树中，(i+1).....n位于树的右子树中。然后可以递归来构建左右子树，由于根节点是唯一的，所以可以保证构建的二叉树都是唯一的。
    
    使用两个状态来记录：
    
    G(n)：长度为n的序列的所有唯一的二叉树。
    
    F(i,n)，1<=i<=n：以i作为根节点的二叉树的数量。
    
    G(n)就是我们要求解的答案，G(n)可以由F(i,n)计算而来。
    
    G(n)=F(1,n)+F(2,n)+...+F(n,n)                           (1)
    
    G(0)=1,G(1)=1
    
    对于给定的一个序列1.....n，我们取i作为它的根节点，那么以i作为根节点的二叉树的数量F(i)可以由下面的公式计算而来：
    
    F(i,n)=G(i-1)*G(n-i) 1<=i<=n                            (2)
    
    综合公式（1）和公式（2），可以看出：
    
    G(n) = G(0) * G(n-1) + G(1) * G(n-2) + … + G(n-1) * G(0)
    
    这就是上面这个问题的答案。

答案：

```python
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [1, 1]
        for i in xrange(2, n + 1):
            count = 0
            for j in xrange(i):
                count += dp[j] * dp[i - j - 1]
            dp.append(count)
        return dp.pop()
```

上面的做法的C++代码如下：

```cpp
class Solution {
public:
    int numTrees(int n) {
        // how many trees if the total tree has dp[i] nodes.
        vector<int> dp(n + 1);
        dp[0] = dp[1] = 1;
        for (int i = 2; i < n + 1; i ++) {
            for (int j = 0; j < i; j++) {
                dp[i] += dp[j] * dp[i - 1 - j];
            }
        }
        return dp[n];
    }
};
```

### 卡特兰数

卡塔兰数的一般项公式为 

令``h(0)=1,h(1)=1``，卡塔兰数数满足递归式：

``h(n)= h(0)*h(n-1) + h(1)*h(n-2) + ... + h(n-1)h(0)`` (其中n>=2)这是n阶递归关系;

该递推关系的解为：

``h(n)=C(2n,n)/(n+1)=P(2n,n)/(n+1)!=(2n)!/(n!*(n+1)!) (n=1,2,3,...)``

代码如下：

```cpp
class Solution {
public:
    int numTrees(int n) {
        // how many trees if the total tree has dp[i] nodes.
        long long res = 1;
        for (int i = n + 1; i <= 2 * n; i++) {
            res = res * i / (i - n);
        }
        return res / (n + 1);
    }
};
```

卡特兰数的前20项是固定的，也就可以直接返回对应的数字即可。

```cpp
class Solution {
public:
    int numTrees(int n) {
        // how many trees if the total tree has dp[i] nodes.
        vector<int> dp = {1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862, 16796, 58786, 208012, 742900, 2674440, 9694845, 35357670, 129644790, 477638700, 1767263190};
        return dp[n];
    }
};
```


## 日期

2018 年 2 月 25 日 
2018 年 12 月 31 日 —— 2018年最后一天！
