作頁很有趣，

最後二個是要 編多個檔案，

但是以os的角度，有一個跟OS 有關的VM ，會先執行 ，

裡面會用到其它的FUNC， 基本上，這裡面用到的FUNC，

其細節定義都不會寫在 Sys.vm裡面，

就是要分散各個Service，所以，只要先掃Sys.vm，把它有call的func，

通常格式都是  ClassName.FuncName ，所以只要掃有call 的那行 ，

再把 ClassName抓出來，去把 ClassName.vm 放到 Sys.vm中，就可以了。

接下來就 是接著之前的 translator.


https://github.com/spike688023/The-Python-Workbook-Solve-100-Exercises/blob/master/all_exercises/92_spike.py

我就記得，以前有處理過 這種類似的問題。
list1 = [ i for i in os.listdir("files") if ".py" in i]
print(len(list1))
