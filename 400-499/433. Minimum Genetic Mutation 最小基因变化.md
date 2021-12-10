
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址: https://leetcode.com/problems/minimum-genetic-mutation/description/

## 题目描述

A gene string can be represented by an 8-character long string, with choices from ``"A", "C", "G", "T"``.

Suppose we need to investigate about a mutation (mutation from "start" to "end"), where ONE mutation is defined as ONE single character changed in the gene string.

For example, ``"AACCGGTT"`` -> ``"AACCGGTA"`` is 1 mutation.

Also, there is a given gene "bank", which records all the valid gene mutations. A gene must be in the bank to make it a valid gene string.

Now, given 3 things - start, end, bank, your task is to determine what is the minimum number of mutations needed to mutate from "start" to "end". If there is no such a mutation, return -1.

Note:

1. Starting point is assumed to be valid, so it might not be included in the bank.
1. If multiple mutations are needed, all mutations during in the sequence must be valid.
1. You may assume start and end string is not the same.
 
    
Example 1:
    
    start: "AACCGGTT"
    end:   "AACCGGTA"
    bank: ["AACCGGTA"]
    
    return: 1
    
Example 2:
    
    start: "AACCGGTT"
    end:   "AAACGGTA"
    bank: ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
    
    return: 2
 
Example 3:
    
    start: "AAAAACCC"
    end:   "AACCCCCC"
    bank: ["AAAACCCC", "AAACCCCC", "AACCCCCC"]
    
    return: 3

## 题目大意

给出了一个起始基因，一个结束基因，问能不能通过变换，每次变化当前基因的一位，并且变化后的这个基因在基因库中的为有效基因，最后变换成为end。如果不可以的话，返回-1.

题目没有给出变换的过程，如果有问题的话，看[127. Word Ladder][1]这个类似题目。

## 解题方法

基本和[127. Word Ladder][1]一模一样的，只不过把26个搜索换成了4个搜索，所以代码只用改变搜索的范围，以及最后的返回值就行了。

很显然这个问题是BFS的问题，同样是走迷宫问题的4个方向，代码总体思路很简单，就是利用队列保存每个遍历的有效的字符串，然后对队列中的每个字符串再次遍历，保存每次遍历的长度即可。每个元素进队列的时候，保存了到达这个元素需要的步数，这样能省下遍历和记录当前bfs长度部分代码。

时间复杂度是O(NL)，空间复杂度是O(N).其中N是Bank中的单词个数，L是基因的长度。

```python
class Solution(object):
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
        bfs = collections.deque()
        bfs.append((start, 0))
        bankset = set(bank)
        while bfs:
            gene, step = bfs.popleft()
            if gene == end:
                return step
            for i in range(len(gene)):
                for x in "ACGT":
                    newGene = gene[:i] + x + gene[i+1:]
                    if newGene in bank and newGene != gene:
                        bfs.append((newGene, step + 1))
                        bank.remove(newGene)
        return -1
```

C++代码如下：

```cpp
class Solution {
public:
    int minMutation(string start, string end, vector<string>& bank) {
        queue<string> q;
        const int N = start.size();
        q.push(start);
        int step = 0;
        while (!q.empty()) {
            int size = q.size();
            for (int s = 0; s < size; s++) {
                auto cur = q.front(); q.pop();
                if (cur == end) {
                    return step;
                }
                for (int i = 0; i < N; i++) {
                    for (char n : {'A', 'C', 'G', 'T'}) {
                        string next = cur.substr(0, i) + n + cur.substr(i + 1);
                        if (next == cur) continue;
                        for (auto it = bank.begin(); it < bank.end(); ++it) {
                            if (*it == next) {
                                q.push(next);
                                bank.erase(it);
                                break;
                            }
                        }
                    }
                }
            }
            step += 1;
        }
        return -1;
    }
};
```

参考资料：

http://www.cnblogs.com/grandyang/p/7653006.html
http://www.cnblogs.com/grandyang/p/4539768.html

## 日期

2018 年 9 月 29 日 —— 国庆9天长假第一天！
2018 年 12 月 28 日 —— 即将元旦假期

  [1]: https://blog.csdn.net/fuxuemingzhu/article/details/82903681
