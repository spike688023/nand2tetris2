# 我這個程 式的目的， 是要測試 ，function call一直往下，
# 如果變數，在目前的scope沒有，那它會往上一層，查它的symbol table嗎
# 看來是沒有， 如果有的話， 就不必用parameter 去傳了

# 應該 是這麼想，它不會看上一層的symbol table，但，會看最上層的，
# 因為那裡才會有  static or object variable.

# 另一個問題 ，如果class是 nested的話 ， 好像也是能往上查，上層class的變數

def func2():
    main_x = 0
    func3()

def func3():
    print main_x

if  __name__ =='__main__':

    func2()
