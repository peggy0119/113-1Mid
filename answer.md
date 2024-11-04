# 期中考
>
>學號：112112105
><br />
>姓名：李佩琪
><br />
>作業撰寫時間：60 (mins，包含程式撰寫時間)
><br />
>最後撰寫文件日期：2024/11/04
>

本份文件包含以下主題：(至少需下面兩項，若是有多者可以自行新增)
- [x] 說明內容

## 說明程式與內容

開始寫說明，該說明需說明想法，
並於之後再對上述想法的每一部分將程式進一步進行展現，
若需引用程式區則使用下面方法，
若為.cs檔內程式除了於敘述中需註明檔案名稱外，
還需使用語法` ```語言種類 程式碼 ``` `，其中語言種類若是要用python則使用py，java則使用java，C/C++則使用cpp，
下段程式碼為語言種類選擇csharp使用後結果：

```csharp
public void mt_getResult(){
    ...
}
```

若要於內文中標示部分網頁檔，則使用以下標籤` ```html 程式碼 ``` `，
下段程式碼則為使用後結果：

```html
<%@ Page Language="C#" AutoEventWireup="true" ...>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
<meta http-equiv="Content-Type" ...>
    <title></title>
</head>
<body>
    <form id="form1" runat="server">
        <div>
        </div>
    </form>
</body>
</html>
```
更多markdown方法可參閱[https://ithelp.ithome.com.tw/articles/10203758](https://ithelp.ithome.com.tw/articles/10203758)
請在撰寫"說明程式與內容"該塊內容，請把原該塊內上述敘述刪除，該塊上述內容只是用來指引該怎麼撰寫內容。


a. 小題

Ans
```py
#生成一個整數2維陣列大小為10x10，名稱為map
map = np.zeros((10, 10), dtype=int)
```
b. 小題

Ans
```py
#生成一個整數1維陣列大小為10，名稱為rowMap
rowMap = np.zeros(10, dtype=int)
```
c. 小題

Ans
```py
#設定rowMap的值
rowMap = np.array([0, 7, 13, 28, 44, 62, 74, 75, 87, 90])
```
d. 小題

Ans
```py
#在map中對應rowMap裡面的值標記炸彈
for index in rowMap:
    row, col = divmod(index, 10)  # 將一維索引轉為二維索引
    map[row, col] = -1  # 使用-1來表示炸彈
```
e. 小題

Ans
```py
#統計炸彈周圍的數量
def count_bombs(map):
    rows, cols = map.shape
    bomb_map = np.zeros((rows, cols), dtype=int)
    
    for r in range(rows):
        for c in range(cols):
            if map[r, c] == -1:  # 如果是炸彈
                bomb_map[r, c] = -1  # 標記為炸彈
            else:
                # 統計周圍炸彈的數量
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if 0 <= r + i < rows and 0 <= c + j < cols:
                            if map[r + i, c + j] == -1:
                                bomb_map[r, c] += 1
    return bomb_map
```