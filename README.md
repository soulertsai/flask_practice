# flask_practice

## 快速實作作品
[link](https://dashboard.heroku.com/apps/powerful-coast-62530)

## virtualenv
用virtualenv可以讓不同版本的flask不會因為global的東西被改變後，舊的東西因此死機。
在flask的資料夾裡：
`virtualenv -p C:\Python34\python.exe venv` 可以選擇python的版本。
`pip install flask` 可以安裝flask相應的版本。

## flask的架構
把像`home.html`、`about.html`等文件放在templates這個資料夾下，然後用`layout.html`做為主模版，如果有和`layout.html`不一樣的話，可以取代，這就是template的概念。
如果是css、js、image的靜態的文件的話，可以放在static之下。

### Jinja2的語法
`{% for post in posts %}` 一些statement用`{%%}`，可以傳進html版後，進行排版
`{{ title }}` 變數名雙大括號

## deploy to Heroku
參考自[Deploying-Flask-To-Heroku](https://github.com/twtrubiks/Deploying-Flask-To-Heroku)

## Reference
1. https://www.youtube.com/watch?v=QnDWIZuWYW0&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH&index=3&t=0s