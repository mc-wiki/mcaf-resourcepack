# Minecraft愚人节翻译资源包

[English](README.md) | 简体中文

## 项目背景

从2024年愚人节快照起，愚人节快照的完成度已相当于一个小型模组。但历年愚人节快照所有字符串均不会通过Crowdin进行本地化，导致Wiki相关条目易出现共识问题。由此本人搭建这一项目以期望促进Wiki相关页面共识讨论工作，同时进行“与Wiki相一致的游戏内翻译的资源包”的分发工作。

## 项目特色

- 尽可能快速、准确地提供最新愚人节快照的（中文）本地化支持。
- 尽可能修复愚人节快照中发现的本地化键名缺失及错别字问题（例如2024年马铃薯牧羊人的纹理文件`shepherd_potato.png`错误拼写为`shepard_potato.png`等）。

## 如何使用

请在[最新Releases](https://github.com/mc-wiki/mcaf-resourcepack/releases/latest)中下载需要的版本，然后安装到你的游戏。

如果不会安装资源包，请阅读[这篇条目](https://zh.minecraft.wiki/?curid=10215#%E4%BD%BF%E7%94%A8%E8%B5%84%E6%BA%90%E5%8C%85)。

另，由于愚人节快照Minecraft 2.0发布时未加入资源包功能，该版本暂不在本项目计划内。

## 贡献方法

### 参与翻译

Crowdin：[https://crowdin.com/project/mcaf-resourcepack](https://crowdin.com/project/mcaf-resourcepack)

[![zh-CN翻译进度](https://img.shields.io/badge/dynamic/json?color=blue&label=zh-CN&style=flat&logo=crowdin&query=%24.progress.1.data.translationProgress&url=https%3A%2F%2Fbadges.awesome-crowdin.com%2Fstats-15691355-777584-update.json)](https://crowdin.com/project/mcaf-resourcepack)
[![zh-HK翻译进度](https://img.shields.io/badge/dynamic/json?color=blue&label=zh-HK&style=flat&logo=crowdin&query=%24.progress.2.data.translationProgress&url=https%3A%2F%2Fbadges.awesome-crowdin.com%2Fstats-15691355-777584-update.json)](https://crowdin.com/project/mcaf-resourcepack)
[![zh-TW翻译进度](https://img.shields.io/badge/dynamic/json?color=blue&label=zh-TW&style=flat&logo=crowdin&query=%24.progress.3.data.translationProgress&url=https%3A%2F%2Fbadges.awesome-crowdin.com%2Fstats-15691355-777584-update.json)](https://crowdin.com/project/mcaf-resourcepack)
[![lzh翻译进度](https://img.shields.io/badge/dynamic/json?color=blue&label=lzh&style=flat&logo=crowdin&query=%24.progress.0.data.translationProgress&url=https%3A%2F%2Fbadges.awesome-crowdin.com%2Fstats-15691355-777584-update.json)](https://crowdin.com/project/mcaf-resourcepack)

### 常见问题

若游玩过程中出现未翻译的文本：

- 到Crowdin参与贡献（见[上一段](#参与翻译)）。
- 如果在Crowdin也没发现此文本，大概率为硬编码所致，资源包无法修复此问题。

若游玩过程中出现本地化键名（类似`rule.food_restriction.air_block`）：

- 一般是语言文件中的缺失，可在本仓库[Issues](https://github.com/mc-wiki/mcaf-resourcepack/issues)中反馈。

<!-- Do not translate the following part -->
## 香港繁体和文言

香港繁体和文言的加入，向前覆盖至2019年8月22日发布的快照19w34a。其晚于2019年愚人节快照3D Shareware v1.34的发布时间。

因此，自15w14a至3D Shareware v1.34：

- Crowdin项目和自动打包的资源包中仍会包含相关语言文件，方便Wiki编写时参考。
- 上述两种语言不会出现在语言列表，正常游戏内不可用。
- 若有使用需求，请自行修改压缩包中的`pack.mcmeta`，格式如下（需去除注释）。

```jsonc
{
    "pack": { 
        // 无需修改此段内容
    },
    "language": {
        "zh_hk": {  // 15w14a时改为"zh_HK"
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
