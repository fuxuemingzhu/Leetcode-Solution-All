- 作者：    负雪明烛
- id：      fuxuemingzhu
- 个人博客：[http://fuxuemingzhu.cn/](http://fuxuemingzhu.cn/)

---
@[TOC](目录)


题目地址：https://leetcode-cn.com/contest/weekly-contest-185/problems/reformat-the-string/

# 题目描述


给你一个数组 `orders`，表示客户在餐厅中完成的订单，确切地说， `orders[i]=[customerNamei,tableNumberi,foodItemi]` ，其中 `customerNamei` 是客户的姓名，`tableNumberi` 是客户所在餐桌的桌号，而 `foodItemi` 是客户点的餐品名称。

请你返回该餐厅的 点菜展示表 。在这张表中，表中第一行为标题，其第一列为餐桌桌号 `“Table”` ，后面每一列都是按字母顺序排列的餐品名称。接下来每一行中的项则表示每张餐桌订购的相应餐品数量，第一列应当填对应的桌号，后面依次填写下单的餐品数量。

注意：客户姓名不是点菜展示表的一部分。此外，表中的数据行应该按餐桌桌号升序排列。

 

示例 1：

    输入：orders = [["David","3","Ceviche"],["Corina","10","Beef Burrito"],["David","3","Fried Chicken"],["Carla","5","Water"],["Carla","5","Ceviche"],["Rous","3","Ceviche"]]
    输出：[["Table","Beef Burrito","Ceviche","Fried Chicken","Water"],["3","0","2","1","0"],["5","0","1","0","1"],["10","1","0","0","0"]] 
    解释：
    点菜展示表如下所示：
    Table,Beef Burrito,Ceviche,Fried Chicken,Water
    3    ,0           ,2      ,1            ,0
    5    ,0           ,1      ,0            ,1
    10   ,1           ,0      ,0            ,0
    对于餐桌 3：David 点了 "Ceviche" 和 "Fried Chicken"，而 Rous 点了 "Ceviche"
    而餐桌 5：Carla 点了 "Water" 和 "Ceviche"
    餐桌 10：Corina 点了 "Beef Burrito" 

示例 2：

    输入：orders = [["James","12","Fried Chicken"],["Ratesh","12","Fried Chicken"],["Amadeus","12","Fried Chicken"],["Adam","1","Canadian Waffles"],["Brianna","1","Canadian Waffles"]]
    输出：[["Table","Canadian Waffles","Fried Chicken"],["1","2","0"],["12","0","3"]] 
    解释：
    对于餐桌 1：Adam 和 Brianna 都点了 "Canadian Waffles"
    而餐桌 12：James, Ratesh 和 Amadeus 都点了 "Fried Chicken"

示例 3：
    
    输入：orders = [["Laura","2","Bean Burrito"],["Jhon","2","Beef Burrito"],["Melissa","2","Soda"]]
    输出：[["Table","Bean Burrito","Beef Burrito","Soda"],["2","1","1","1"]]
 

提示：

1. `1 <= orders.length <= 5 * 10^4`
1. `orders[i].length == 3`
1. `1 <= customerNamei.length, foodItemi.length <= 20`
1. `customerNamei` 和 `foodItemi` 由大小写英文字母及空格字符 `' '` 组成。
1. `tableNumberi` 是 1 到 500 范围内的整数。


# 题目大意

给出了 Table 和 food 的一些匹配关系，求每条边出现的次数，以形成一张表格。

# 解题方法

## 字典统计边的次数

这个题本身不难，但是比较恶心，因为要返回的结果必须是指定格式的。所以我的代码写的贼麻烦。

1. 统计 foods 和 tables 分别为多少，并进行排序。
2. 统计每个桌的各个菜的次数
3. 把所有的桌的菜按照顺序拼接成列表

Python代码如下：

```python
class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        count = collections.defaultdict(dict)
        foods = set()
        tables = set()
        for order in orders:
            foods.add(order[2])
            tables.add(int(order[1]))
        foods = sorted(list(foods))
        cols = ["Table", ] + foods
        res = []
        res.append(cols)
        for order in orders:
            if order[2] not in count[order[1]]:
                count[order[1]][order[2]] = 0
            count[order[1]][order[2]] += 1
        for table in sorted(list(tables)):
            table = str(table)
            tc = count[table]
            line = [table,]
            for food in foods:
                if food not in tc:
                    line.append("0")
                else:
                    line.append(str(tc[food]))
            res.append(line)
        return res
```


**欢迎关注[负雪明烛的刷题博客](https://blog.csdn.net/fuxuemingzhu)，leetcode刷题800多，每道都讲解了详细写法！**

# 日期

2020 年 4 月 19 日 —— 近期比赛太多


  [1]: https://blog.csdn.net/fuxuemingzhu/article/details/79451733
