# ToolKit
​:smile: some tools I developed to provide convenience

# [qrsSpellLink](https://github.com/BitterPotato/ToolKit/issues/1)
**qrsSpellLink** is used to generate the link of the file which you have uploaded to the [Qiniu Cloud](https://www.qiniu.com) by using [qrsbox](https://developer.qiniu.com/kodo/tools/qrsbox).

And here's why you might want to use it:
* You produced and uploaded a picture to `Qiniu Cloud` by by using `qrsbox` for your new blog written by [Markdown](https://zh.wikipedia.org/zh-cn/Markdown), and just wanted to get the link of the picture quickly.

[see more](https://github.com/BitterPotato/ToolKit/issues/1)

# mdMathRender

[Jianshu](http://www.jianshu.com) doesn't support `Mathjax`.

When we have written blogs by using `Mathjax` in markdown, if we want to publish them in *Jianshu*. Then we need to [do this transformation](http://www.jianshu.com/p/e8a14ec1c614)

```
$$x_1 + x_2$$
```

to

```
![](http://latex.codecogs.com/svg.latex?x_1 + x_2)
```



## Getting Started

1. drop your `xxx.md` file to `ToJianshu.bat`
2. you will get a `xxx_js.md` in your current directory

