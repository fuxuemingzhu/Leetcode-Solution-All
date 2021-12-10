
作者： 负雪明烛
id：	fuxuemingzhu
个人博客：	http://fuxuemingzhu.cn/

---
@[TOC](目录)

题目地址：https://leetcode.com/problems/encode-and-decode-tinyurl/description/


## 题目描述

TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl and it returns a short URL such as http://tinyurl.com/4e9iAk.

Design the encode and decode methods for the TinyURL service. There is no restriction on how your encode/decode algorithm should work. You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.

## 解题方法

### 方法一：数组

这个题是个佛性题。不给任何要求，只要能编码、解码出来就行。用了大神的思路，直接用数组进行保存，然后把每个网址所在数组中的编号作为短网址进行编码和解码。

```python
class Codec:

    def __init__(self):
        self.urls = []

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        self.urls.append(longUrl)
        return "http://tinyurl.com/" + str(len(self.urls) - 1)
        
        

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        return self.urls[int(shortUrl.split('/')[-1])]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
```

### 方法二：字典

道理是一样的，其实字典更简单一点。

```python
class Codec:
    def __init__(self):
        self.count = 0
        self.d = dict()
    
    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        self.count += 1
        self.d[self.count] = longUrl
        return str(self.count)

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        return self.d[int(shortUrl)]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
```

C++版本的代码如下：

```cpp
class Solution {
public:

    // Encodes a URL to a shortened URL.
    string encode(string longUrl) {
        count++;
        d[count] = longUrl;
        return to_string(count);
    }

    // Decodes a shortened URL to its original URL.
    string decode(string shortUrl) {
        return d[stoi(shortUrl)];
    }
private:
    int count = 0;
    map<int, string> d;
};

// Your Solution object will be instantiated and called as such:
// Solution solution;
// solution.decode(solution.encode(url));
```

## 日期

2018 年 2 月 5 日 
2018 年 12 月 2 日 —— 又到了周日
