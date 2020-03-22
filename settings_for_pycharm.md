1. open project using pycharm from commandline
1) click "tools"-> "create desktop entry" -> the short cut for pycharm bin with be in /usr/local/bin/charm
2) export charm to path
 ```
 export PATH=/usr/local/bin/charm:$PATH
 ```
3) go to directory of your project, and open it in pycharm
```
charm .
```


2. start pycharm or other program in background
add & in the end of the command
```
charm . &
```
