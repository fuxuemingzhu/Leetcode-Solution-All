
- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)

---
@[TOC](目录)


题目地址：https://leetcode-cn.com/problems/read-n-characters-given-read4/

## 题目描述

Given a file and assume that you can only read the file using a given method `read4`, implement a method to read n characters.

Method `read4`:

The API `read4` reads 4 consecutive characters from the file, then writes those characters into the buffer array buf.

The return value is the number of actual characters read.

Note that read4() has its own file pointer, much like FILE *fp in C.

Definition of read4:

    Parameter:  char[] buf
    Returns:    int

Note: buf[] is destination not source, the results from read4 will be copied to buf[]
Below is a high level example of how read4 works:

    File file("abcdefghijk"); // File is "abcdefghijk", initially file pointer (fp) points to 'a'
    char[] buf = new char[4]; // Create buffer with enough space to store characters
    read4(buf); // read4 returns 4. Now buf = "abcd", fp points to 'e'
    read4(buf); // read4 returns 4. Now buf = "efgh", fp points to 'i'
    read4(buf); // read4 returns 3. Now buf = "ijk", fp points to end of file
 

Method `read`:

By using the `read4` method, implement the method read that reads n characters from the file and store it in the buffer array buf. Consider that you cannot manipulate the file directly.

The return value is the number of actual characters read.

Definition of read:

    Parameters:	char[] buf, int n
    Returns:	int

Note: buf[] is destination not source, you will need to write the results to buf[]
 

Example 1:

    Input: file = "abc", n = 4
    Output: 3
    Explanation: After calling your read method, buf should contain "abc". We read a total of 3 characters from the file, so return 3. Note that "abc" is the file's content, not buf. buf is the destination buffer that you will have to write the results to.

Example 2:

    Input: file = "abcde", n = 5
    Output: 5
    Explanation: After calling your read method, buf should contain "abcde". We read a total of 5 characters from the file, so return 5.

Example 3:

    Input: file = "abcdABCD1234", n = 12
    Output: 12
    Explanation: After calling your read method, buf should contain "abcdABCD1234". We read a total of 12 characters from the file, so return 12.

Example 4:

    Input: file = "leetcode", n = 5
    Output: 5
    Explanation: After calling your read method, buf should contain "leetc". We read a total of 5 characters from the file, so return 5.
     

Note:

1. Consider that you cannot manipulate the file directly, the file is only accesible for read4 but not for read.
1. The read function will only be called once for each test case.
1. You may assume the destination buffer array, buf, is guaranteed to have enough space for storing n characters.

## 题目大意

用read4函数读取n个字符。

## 解题方法

### 直接调用

题目比较绕，总之`read4`一次最多能读取4个字符，读取结果放到第一个参数里，真正读取了的长度是其返回值。现在要用`read4`读取n个字符。

做法是如果读取的字符串不够n，那么就一直循环读取，读取到了n个或者文件中已经没有内容了就停止，最后返回读取了多少个。

C++代码如下：

```cpp
// Forward declaration of the read4 API.
int read4(char *buf);

class Solution {
public:
    /**
     * @param buf Destination buffer
     * @param n   Number of characters to read
     * @return    The number of actual characters read
     */
    int read(char *buf, int n) {
        int count = 0;
        while (n) {
            char file[4];
            int m = read4(file);
            for (int i = 0; i < m && count < n; ++i) {
                buf[count] = file[i];
                count ++;
            }
            if (m < 4)
                break;
        }
        return count;
    }
};
```

## 日期

2019 年 9 月 19 日 —— 举杯邀明月，对影成三人


  [1]: https://blog.csdn.net/fuxuemingzhu/article/details/72465759
