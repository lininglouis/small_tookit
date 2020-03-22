### 1. open project using pycharm from commandline
 a) click "tools"-> "create desktop entry" -> the short cut for pycharm bin with be in /usr/local/bin/charm
 b) export charm to path
 ```
 export PATH=/usr/local/bin/charm:$PATH
 ```
 c) go to directory of your project, and open it in pycharm
```
charm .
```


### 2. start pycharm or other program in background
add & in the end of the command
```
charm . &
```
