# Minecraft愚人节中文翻译包

*嗨，愚人节中文翻译包更新了，来测。*

![Crowdin Localization Badge](https://badges.crowdin.net/mcaf-resourcepack/localized.svg)

## 项目背景

从2024年愚人节快照起，愚人节快照的完成度已相当于一个小型模组。但历年愚人节快照所有字符串均不会通过Crowdin进行本地化，导致Wiki相关条目易出现共识问题。由此本人搭建这一项目以期望促进Wiki相关页面共识讨论工作，同时进行“与Wiki相一致的游戏内中文翻译包”的分发工作。

*人话：字符串太多，一个人啃不动。*

## 项目特色

- 尽可能快速、准确的愚人节快照的中文本地化支持。
- 尽可能修复愚人节快照中找到的缺失本地化键名及错别字问题（例如2024年马铃薯牧羊人的纹理文件`shepherd_potato.png`错误拼写为`shepard_potato.png`等）。

## 如何使用

在右侧最新Releases里下载需要的版本，然后安装到你的游戏。

如果不会安装资源包，请见[这篇条目](https://zh.minecraft.wiki/?curid=10215#%E4%BD%BF%E7%94%A8%E8%B5%84%E6%BA%90%E5%8C%85)。

## 参与翻译

Crowdin：[https://crowdin.com/project/mcaf-resourcepack](https://crowdin.com/project/mcaf-resourcepack)

## 反馈问题

若游玩过程中出现英文文本：

- 到Crowdin参与贡献（见[上一段](#参与翻译)）。
- 如果在Crowdin也没发现此文本，大概率硬编码所致，资源包无法修复此问题。

如游玩过程中出现本地化键名（类似`rule.food_restriction.air_block`的文本）：

- 一般是语言文件遗漏了，可在本仓库[Issues](https://github.com/Don-Trueno/mcaf-resourcepack/issues)反馈。

## 2019年<!--及以前的-->愚人节快照

繁体中文（香港）、文言自加入后，向前支持直至2019年8月22日发布的快照版本`19w34a`，晚于2019年愚人节快照`3D Shareware v1.34`的发布时间。对此：

- Crowdin项目和自动打包的资源包中仍会包含相关语言文件，方便Wiki编写时参考。
- 但2019年<!--及以前的-->愚人节快照中，这两种语言仍然不会出现在语言列表里。

如强烈需要，可自行修改`pack.mcmeta`为以下内容：

```json
{
    "pack": { 
        "pack_format": 4,
        "description": "适合3D Shareware v1.34的中文翻译包"
    },
    "language": {
        "zh_hk": {
            "name": "繁體中文",
            "region": "香港特別行政區"
        },
        "lzh": {
            "name": "文言",
            "region": "華夏"
        }
    }
}
```

*另外，这些版本里硬编码文本超多的。资源包能起到的作用十分有限。*
