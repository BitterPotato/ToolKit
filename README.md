# ToolKit
​:smile: some tools I developed to provide convenience

# qrsSpellLink
[qrsSpellLink]() is used to generate the link of the file which you have uploaded to the [Qiniu Cloud](https://www.qiniu.com) by using [qrsbox](https://developer.qiniu.com/kodo/tools/qrsbox).

And here's why you might want to use it:
* You produced and uploaded a picture to `Qiniu Cloud` by by using `qrsbox` for your new blog written by [Markdown](https://zh.wikipedia.org/zh-cn/Markdown), and just wanted to get the link of the picture quickly.

## Getting Started
### Configuration
Clone the folder `qrsSpellLink`.
Modify the following two lines in `qrsSpellLink.py`.
	# synchronize folder
	src = ""
	# Domain Name
	name = ""
* The value of `synchronize folder` is the same as the coresponding key of `QRSBox window`.
  ![synchronize folder in qrsbox](http://oi0xi3dzx.bkt.clouddn.com/tools/qrs/qrsbox.png)
* You can find `Domain Name` in Your `Qiniu Cloud`, such as
  ![Domain Name](http://oi0xi3dzx.bkt.clouddn.com/tools/qrs/domain_name.png)

### Generate a link
Here's how you use `qrsSpellLink`.
1. Drag the file to `qrsSpellLink.cmd`.
2. Then you will see the link you want in the batch window.
   ![Usage](http://oi0xi3dzx.bkt.clouddn.com/tools/qrs/usage.gif)