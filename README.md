# CDP_Android

解决博客上提及的问题，通过CDP的方式正确连接微信上的webview页面。

# 注意

此code为解决博客上的问题的小demo。

此demo未对异常进行细致的处理，所以在运行代码前需各位朋友提前检查环境：
1. python版本>3.0
2. adb可正常连接android
3. 采用USB进行adb连接
4. adb shell 命令可正常工作
5. 连接微信上的webview前，确保其已开启webview调试模式
6. demo只支持在windows下运行, 不支持linux


# 开始

1. 检查完以上注意事项后, 在微信中访问百度首页[baidu.com]
2. 运行以下demo，即可连接微信的内置chromium，并与其上的webview[百度页面]通信
```
$ python ./example.py
```

# 补充

1. demo中的连接webview的原因适合所有hybridApp以及基于electron的桌面应用
2. 感兴趣的朋友欢迎fork后扩展，对于demo的健壮性也欢迎提升
3. 如有问题欢迎留言，但代码不做维护





