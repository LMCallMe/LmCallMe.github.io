---
title: Atom:创建自己的语法高亮
layout: post
categories: IDE
tag: [Atom]
---

原文链接: http://www.cnblogs.com/coding-my-life/p/4639649.html


atom linux 的配置目录在 ~/.atom 下，
里面有一个 packages 目录，所有安装的插件(或者叫做包)都在这里。
所有在这里的包在启动时都会自动加载。
因此，我们直接在这里创建一个包。

``` bash
cd .atom/packages
mkdir language-protobuf
cd language-protobuf
```

atom 的 packages 都是有特定的目录结构和文件的。 
首先，要有一个 package.json 来描述你的包，在 language-protobuf 目录下创建它。

``` json
{
  "name": "language-proto",
  "version": "0.2.0",
  "description": "Syntax highlighting for google protobuf",
  "repository": "https://github.com/changnet/language-protobuf",
  "license": "MIT",
  "engines": {
    "atom": "*",
    "node": "*"
  }
}
```

其中， name(包名) 、 version(版本) 、 description(描述) 这些都是要的。
如果你准备发布这个包 repository(源) 这些也是要的。
可以到github上参考别人的怎么写。

现在已经创建了一个空包。要实现语法高亮，就要有一些语法规则来指定如何高亮。
下面开始创建语法规则。

``` bash
mkdir grammars
cd grammars
```

然后在 grammars 目录下创建语法规则文件 protobuf.cson (atom的配置文件用cson来保存的)

``` json
'scopeName': 'source.protobuf'
'name': 'protobuf'
'fileTypes': ['proto']
'patterns': [
  {
    'match': '\\b[0-9]+\\b'
    'name': 'constant.numeric.protobuf'
  }
]
```

上面是一个简单的语法规则文件。

scopeName是指定本文件的范围，相当于C++中的namespace。
比如你写了一个C的语法高亮(source.c)，然后要写一个C++的语法高亮，
那么可以直接在C++的语法文件中'include': 'source.c'
即可把C的语法规则给包含进来。

name是语法的名字，C就是C，java就是java。
atom通常会把它显示在状态栏右下角。

fileTypes是文件后缀。atom打开时会根据文件后缀来判断采用哪一种语法高亮。
多个文件后缀按行分开即可。如

``` json
'fileTypes': [
'h'
'hpp'
'cpp'
]
```

patterns 是规则匹配的集合，它是一个数组，每个元素是一个对象{}。

在上面的例子中，对象的内容如下：

match 是正则表达式（在cson中转义字符要多加一个\，如\b变成\\b）
,指明如何要匹配到高亮的目标。
如\\b[0-9]+\\b用来匹配常数。比如"required int32 id = 1;"中的1

name 是高亮的名字，constant.numeric.protobuf 
表示用 constant(常量) 下的 numeric(数字) 规则（什么字体、颜色）来高亮匹配的字符。

一个简单的包就解释完了。但是
constant.numeric.protobuf
是如何指定高亮规则的。
这得从atom的主题说起。atom的主题分为ui和语法。
ui是界面(像标签、状态栏...)相关的，与语法无关。
语法主题则是控制代码高亮的，在设置中指定。
我使用的是Monokai主题，分析这个主题可以发现它里面有一个index.less文件(https://github.com/burntime/atom-monokai/blob/master/index.less)。里面指定了大部分结构的高亮规则。比如：

``` bash
.comment {
  color: #75715E;
}

.string {
  color: #E6DB74;
}

.constant.numeric {
  color: #AE81FF;
}
```

来龙去脉了解了，下面我们来添加更多的规则。

这分别指定了comment(注释)、string(字符串)、constant.number(常量分类下的数字)的颜色。
而在constant.numeric.protobuf这个命名中，从上而下找。
先找到constant，再到numberic，发现protobuf没找到，于是就使用constant.numeric的颜色。
所以，如果你要先了解主题中有哪些颜色分类可以用。

来龙去脉了解了，下面我们来添加更多的规则。

``` josn
{
    'match': '\\b(message|enum|service)\\b'
    'name': 'storage.type.custom.protobuf'
  }
  {
    'match': '\\b(rpc|returns)\\b'
    'name': 'keyword.protobuf'
  }
  {
    'match': '\\b[0-9]+\\b'
    'name': 'constant.numeric.protobuf'
  }
  {
    'match': '\\b(required|optional|repeated)\\b'
    'name': 'storage.modifier.protobuf'
  }
  {
    'captures':
      '1':
        'name': 'storage.modifier.protobuf'
      '2':
        'name': 'entity.name.instance.protobuf'
    'match': '\\b(required|optional|repeated)(\\s+\\w+)\\b'
    'name': 'entity.name.instance.protobuf'
  }
```

仔细看上面最后一条规则，与其他不一样。

captures 表示要匹配的多个规则。
第一个是 storage.modifier.protobuf ，另一个是 entity.name.instance.protobuf 。 
但是只有一个正则表达式啊，如何匹配多个呢？
仔细看正则表达式，你会发现有两个括号。
(required|optional|repeated)匹配第一个，
(\\s+\\w+)匹配第二个。
这样，"required Info info = 1;"中的required按第一个规则高亮，Info按第二个规则高亮。
而它本身的名字entity.name.instance.protobuf则不指定语法高亮了，随意写都可以。
（PS:这个规则是我推导测试出来的，未找到官方文档的说明）

接着继承添加其他规则:

``` josn
{
    'begin': '"'
    'beginCaptures':
      '0':
        'name': 'punctuation.definition.string.begin.protobuf'
    'end': '"'
    'endCaptures':
      '0':
        'name': 'punctuation.definition.string.end.protobuf'
    'name': 'string.quoted.double.protobuf'
    'patterns': [
      {
        'include': 'punctuation.definition.string.begin.protobuf'
      }
      {
        'include': 'punctuation.definition.string.end.protobuf'
      }
      {
        'match': '\\\\.'
        'name': 'constant.character.escape.protobuf'
      }
    ]
  }
```

这是一个很复杂的规则，连我看得也不是很明白。这是一个匹配字符串的规则。begin表示字符串以"开始，beginCaptures表示开始字符串要匹配多个规则(万一这个开始字符串很复杂)，其中的name也表示高亮规则。end表示字符串以"结束，endCaptures对应。string.quoted...表示以字符串规则进行高亮，注意，如果这个整个规则中某个部分(比如开始部分的名字)未找到对应高亮规则，则使用这个规则。patterns表示字符串中包含多个匹配规则，还要在字符串内部进一行匹配。比如'\\\\.'表示正则匹配一个\和一个\r\n以外的字符(即正则中的点号)，即匹配字符串中\t之类的。include表示字符串内部包含其他现成高亮规则，遗憾的是我并没有测试成功。只有写完整的match才OK。

　　一此为止，所有的匹配规则都已介绍完了。如果还有你想高亮而不能高亮的地方，哪就在正则表达式上多下点功夫。另一个好办法是去看一下其他现在的语言的高亮是怎么做的。

　　写完了，当然还要调试。下面说几个调试要点：

语法文件是在打开atom的时候加载的，你改了后，要看看效果。一种办法是重启atom;另一种办法是ctrl+shift+p，输入widown:Reload重新加载，对应快捷键是ctrl+alt+r

把鼠标放在高亮的字符尾，然后ctrl+shift+p，输入Editor:log curso scope，atom会在右上角显示当前的高亮信息。

atom本身是基于webkit内核的一个web编辑器。在View-->devloper-->toggle developer tools即可打开web调试界面。对应做web的来说，这个应该很容易。

调试完了，该说一下发布。
atom是github开发的，它的包要在github上
(也可能不需要，但我发布时确实要用到github的密码)。
因此当前开始的包要在github上创建一个源，测试好，把最新的代码提交。
然后从cmd进入到包的根目录，利用atom自带的apm进行发布。

``` bash
apm publish minor
```

第一次的时候，要注册atom开发帐号(可以直接用github帐号关联)，
然后拿到帐号中的开发key进行绑定

然后重新发布：

如果没有什么问题，发布成功后就可以在atom的设置界面搜索并进行安装。

proto的语法高亮最终效果如下：

在atom中搜索language-proto可以搜索到这个包。