作者： 		负雪明烛 
id：				fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---

题目地址: https://leetcode.com/problems/accounts-merge/description/

## 题目描述：

Given a list ``accounts``, each element ``accounts[i]`` is a list of strings, where the first element ``accounts[i][0]`` is a name, and the rest of the elements are emails representing emails of the account.

Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some email that is common to both accounts. Note that even if two accounts have the same name, they may belong to different people as people could have the same name. A person can have any number of accounts initially, but all of their accounts definitely have the same name.

After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.

Example 1:

    Input: 
    accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
    Output: [["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'],  ["John", "johnnybravo@mail.com"], ["Mary", "mary@mail.com"]]
    Explanation: 
    The first and third John's are the same person as they have the common email "johnsmith@mail.com".
    The second John and Mary are different people as none of their email addresses are used by other accounts.
    We could return these lists in any order, for example the answer [['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com'], 
    ['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] would still be accepted.

Note:

1. The length of accounts will be in the range [1, 1000].
1. The length of accounts[i] will be in the range [1, 10].
1. The length of accounts[i][j] will be in the range [1, 30].


## 题目大意

给出一个账户列表，其中每一个账户由多个字符串组成，第一个字符串为姓名，其余的字符串为在该姓名下注册的邮箱地址。由于同一个人可能有两个不同的账户，判别是否是同一个人所拥有的账户方法就是在不同的账户中发现是否有相同的邮箱地址，如果有相同的邮箱地址，则可判定两个账户为同一人所拥有。现在要做的就是，对给定账户列表中同一个人所拥有的账户进行合并，合并结果为一个人只拥有一个账户，并且该账户包含其所有的邮箱并且不重复。 
Note：同一人的账户可能有多个重名邮箱地址，输出的时候要对这部分进行处理去掉冗余部分，并且进行字典序排列。

## 解题方法

这个题的解法是并查集，[LeetCode 721. Accounts Merge][1]对这个题有非常详细的讲解，包括并查集的知识，我就不班门弄斧了。另外，我把这个c++代码用python实现了一遍，时间复杂度应该比c++还要低一点，可是通过不了啊……尴尬。

> 这个问题本质上是对不同的集合进行处理，因此暴力求解法在这里几乎不可能成功。求解这个问题的方法最经典的思路就是并查集。
> 
> 那么在本题所涉及的条件下，我们应该满足两个要求。
> 
> 
> 去除重复元素，并且有序排序
> 
> 
> 对于这个条件，很容易想到set集合（结合中没有重复元素，而且元素在插入的时候保持字典序），因此在实现的过程中，必要的一步就是将原有的邮箱列表装载到一个set集合中，然后进行如下的操作。
> 
> 
> 对含有相同元素的集合，进行合并。
> 
> 
> 这个步骤中，就要我们的刚学的并查集登场了。 
> 1. 首先初始化并查集，使并查集和中的元素（i = 0,1,2…n）与account中的元素(account[0], account[1]…account[n]）一一对应。 
> 2. 在对应结束后，我们便可以将所有的集合元素遍历一遍，判断哪些集合会有相同的元素。凡是有相同邮箱的账户均合并（此操作在并查集中实现）。 
> 3. 进行完上面的步骤之后，哪些account是属于同一人的，这些关系均会在并查集上体现出来。最后，我们按照并查集的操作，来将元素进行合并即可。

代码如下，并没有通过OJ.

```python
class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        n = len(accounts)
        self.par = [x for x in range(n)]
        nameMap = collections.defaultdict(list)
        for i, account in enumerate(accounts):
            nameMap[account[0]].append(i)
        for i in range(n):
            for j in nameMap[accounts[i][0]]:
                if (not self.same(i, j)) and (set(accounts[i][1:]) & set(accounts[j][1:])):
                    self.union(i, j)
        res = [set() for _ in range(n)]
        for i in range(n):
            self.par[i] = self.find(i)
            res[self.par[i]] |= set(accounts[i][1:])
        ans = []
        for i in range(n):
            if self.par[i] == i:
                person = list()
                person.append(accounts[i][0])
                person.extend(sorted(res[i]))
                ans.append(person)
        return ans
        
        
    def find(self, x):
        if x == self.par[x]:
            return self.par[x]
        parent = self.find(self.par[x])
        self.par[x] = parent
        return parent
    
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        self.par[x] = y
    
    def same(self, x, y):
        return self.find(x) == self.find(y)
```

使用原文的c++代码能通过，时间是1204ms，这个对于c++来说已经很慢了。

```c++
const int N = 1000 + 5;
int n, par[N];
int find(int x) {
    return par[x] == x ? x : (par[x] = find(par[x]));
}
void unit(int x, int y) {
    x = find(x); y = find(y);
    if (x == y) return;
    par[x] = y;
}
bool same(int x, int y) {
    return find(x) == find(y);
}
class Solution {
public:
    vector<vector<string>> accountsMerge(vector<vector<string>>& accounts) {
        n = accounts.size();
        for (int i = 0; i < n; i++) par[i] = i;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < i; j++) if (!same(i, j)) {
                for (int k = 1; k < accounts[i].size(); k++) for (int t = 1; t < accounts[j].size(); t++) {
                    if (accounts[i][k] == accounts[j][t]) unit(i, j);
                }
            }
        }
        vector<set<string> > res; res.resize(n);
        for (int i = 0; i < n; i++) {
            par[i] = find(i);
            for (int j = 1; j < accounts[i].size(); j++) res[par[i]].insert(accounts[i][j]);
        }
        vector<vector<string> > ret;
        for (int i = 0; i < n; i++) if (par[i] == i) {
            vector<string> cur;
            cur.push_back(accounts[i][0]);
            for (auto str : res[i]) cur.push_back(str);
            ret.push_back(cur);
        }
        return ret;
    }
};
```

使用官方解答的并查集代码也能通过，说明在优化不够好的情况下，c++速度确实比python快了很多。

```python
class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        dsu = DSU()
        em_to_name = dict()
        em_to_id = dict()
        i = 0
        for acc in accounts:
            name = acc[0]
            for email in acc[1:]:
                em_to_name[email] = name
                if email not in em_to_id:
                    em_to_id[email] = i
                    i += 1
                dsu.union(em_to_id[acc[1]], em_to_id[email])
                
        ans = collections.defaultdict(list)
        for email in em_to_name:
            ans[dsu.find(em_to_id[email])].append(email)
        
        return [[em_to_name[v[0]]] + sorted(v) for v in ans.values()]
        
class DSU:
    def __init__(self):
        self.par = range(10001)

    def find(self, x):
        if x != self.par[x]:
            self.par[x] = self.find(self.par[x])
        return self.par[x]
    
    def union(self, x, y):
        self.par[self.find(x)] = self.find(y)
    
    def same(self, x, y):
        return self.find(x) == self.find(y)
    
```


参考资料：

https://blog.csdn.net/likewind1993/article/details/78473302
https://leetcode.com/articles/accounts-merge/

## 日期

2018 年 9 月 30 日 —— 9月最后一天啦！


  [1]: https://blog.csdn.net/likewind1993/article/details/78473302
