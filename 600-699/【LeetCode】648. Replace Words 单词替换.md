
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)


题目地址：https://leetcode.com/problems/replace-words/description/


## 题目描述

In English, we have a concept called ``root``, which can be followed by some other words to form another longer word - let's call this word successor. For example, the root an, followed by other, which can form another word another.

Now, given a dictionary consisting of many roots and a sentence. You need to replace all the successor in the sentence with the root forming it. If a successor has many roots can form it, replace it with the root with the shortest length.

You need to output the sentence after the replacement.

Example 1:

    Input: dict = ["cat", "bat", "rat"]
    sentence = "the cattle was rattled by the battery"
    Output: "the cat was rat by the bat"

Note:
1. The input will only have lower-case letters.
1. 1 <= dict words number <= 1000
1. 1 <= sentence words number <= 1000
1. 1 <= root length <= 100
1. 1 <= sentence words length <= 1000


## 题目大意

把句子中的每个单词用给的字典进行替换，替换时优先替换成最短的词。替换就是找出最短的头部匹配；如果字典中不存在，就保留原来的词。

## 解题方法

### set

看了下给出的Note，发现并没有特别长，普通的方法应该就能搞定，不会超时。

下面的方法叫做Prefix Hash，对于python而言就是用了set的意思。

```python
class Solution(object):
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        rootset = set(dict)
        def replace(word):
            for i in xrange(len(word)):
                if word[:i] in rootset:
                    return word[:i]
            return word
        return ' '.join(map(replace, sentence.split()))
```

### 字典

用数组保存dict中，每个小写字符开头的单词。然后对给出的句子进行遍历每个单词，判断这个单词能不能用更短的前缀替换。题目中要求用尽可能短的单词进行替换，所以需要排序，让短的单词在前面。

```cpp
class Solution {
public:
    string replaceWords(vector<string>& dict, string sentence) {
        vector<vector<string>> m(26);
        sort(dict.begin(), dict.end(), [](string a, string b) {
            return a.size() < b.size();});
        for (string s : dict)
            m[s[0] - 'a'].push_back(s);
        istringstream is(sentence);
        string cur;
        string res;
        while (is >> cur) {
            for (string word : m[cur[0] - 'a']) {
                if (word == cur.substr(0, word.size())) {
                    cur = word;
                    break;
                }
            }
            res += cur + ' ';
        }
        res.pop_back();
        return res;
    }
};
```

### 前缀树

前缀树，又称字典树Trie。具体实现可以看[208. Implement Trie (Prefix Tree)](https://blog.csdn.net/fuxuemingzhu/article/details/79388432)。

这个题里面，使用了Trie。做法比较简单，把所有的字典前缀放入Trie里面，然后再查句子每个单词是否在里面即可。

需要注意的是，我们的根节点没有存储字符，遍历Trie的时候，p的child数组是我们对应的当前字符。如果当前节点是单词，就直接返回了。如果当前节点不是单词，然后它的child又是空，说明不符合要查找的字符串。就返回掉原始字符串即可。

```cpp
class TrieNode {
public:
    vector<TrieNode*> child;
    bool isWord;
    TrieNode() : isWord(false), child(26, nullptr){};
    ~TrieNode() {
        for (auto& a : child)
            delete a;
    }
};
class Solution {
public:
    string replaceWords(vector<string>& dict, string sentence) {
        root = new TrieNode();
        for (string& d : dict) {
            insert(d);
        }
        istringstream is(sentence);
        string res;
        string cur;
        while (is >> cur) {
            res += getPrefix(cur) + ' ';
        }
        res.pop_back();
        return res;
    }
    string getPrefix(string word) {
        TrieNode* p = root;
        string path;
        for (char& c : word) {
            int i = c - 'a';
            if (p->isWord)
                return path;
            if (!p->child[i])
                return word;
            path += c;
            p = p->child[i];
        }
        return word;
    }
    void insert(string word) {
        TrieNode* p = root;
        for (char& c : word) {
            int i = c - 'a';
            if (!p->child[i])
                p->child[i] = new TrieNode();
            p = p->child[i];
        }
        p->isWord = true;
    }
private:
    TrieNode* root;
};
```

## 日期

2018 年 2 月 27 日 
2018 年 12 月 18 日 —— 改革开放40周年
