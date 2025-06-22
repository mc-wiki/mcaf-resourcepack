# Minecraft 愚人节翻译包

[English](README.md) | [日本語](README.ja.md) | 简体中文

**使用来自 Minecraft Wiki 的翻译，畅玩愚人节快照。**

愚人节快照不会通过 Crowdin 官方本地化，但 Minecraft Wiki 社区会为其内容提供翻译。本项目整合了这些翻译，便于玩家间交流和对 wiki 条目命名达成共识。

## 项目特色

- 提供准确、及时的愚人节快照本地化支持。
- 修复缺失的本地化键名和严重错别字（如将 24w14potato 中的`shepard_potato.png`更正为`shepherd_potato.png`）。

当前支持的语言有：

- `ja`: 日本語
- `lzh`: 文言
- `zh_cn`: 简体中文（中国大陆）
- `zh_hk`: 繁體中文（香港特別行政區）
- `zh_tw`: 繁體中文（台灣）

## 如何使用

1. 前往[最新 Releases](https://github.com/mc-wiki/mcaf-resourcepack/releases/latest)页面。
2. 下载所需语言的资源包。
3. 安装到你的游戏中。

不会安装？请参阅[wiki 教程](https://minecraft.wiki/w/Tutorial:Loading_a_resource_pack)。

> [!NOTE]
> Minecraft 2.0 版本因当时不支持资源包，暂不包含在本项目中。

## 贡献方法

### 参与翻译

欢迎在 Crowdin 上完善翻译：
[https://crowdin.com/project/mcaf-resourcepack](https://crowdin.com/project/mcaf-resourcepack)

[![zh-CN翻译进度](https://img.shields.io/badge/dynamic/json?color=blue&label=zh-CN&style=flat&logo=crowdin&query=%24.progress.2.data.translationProgress&url=https%3A%2F%2Fbadges.awesome-crowdin.com%2Fstats-15691355-777584-update.json)](https://crowdin.com/project/mcaf-resourcepack)
[![zh-HK翻译进度](https://img.shields.io/badge/dynamic/json?color=blue&label=zh-HK&style=flat&logo=crowdin&query=%24.progress.3.data.translationProgress&url=https%3A%2F%2Fbadges.awesome-crowdin.com%2Fstats-15691355-777584-update.json)](https://crowdin.com/project/mcaf-resourcepack)
[![zh-TW翻译进度](https://img.shields.io/badge/dynamic/json?color=blue&label=zh-TW&style=flat&logo=crowdin&query=%24.progress.4.data.translationProgress&url=https%3A%2F%2Fbadges.awesome-crowdin.com%2Fstats-15691355-777584-update.json)](https://crowdin.com/project/mcaf-resourcepack)
[![lzh翻译进度](https://img.shields.io/badge/dynamic/json?color=blue&label=lzh&style=flat&logo=crowdin&query=%24.progress.1.data.translationProgress&url=https%3A%2F%2Fbadges.awesome-crowdin.com%2Fstats-15691355-777584-update.json)](https://crowdin.com/project/mcaf-resourcepack)
[![ja翻译进度](https://img.shields.io/badge/dynamic/json?color=blue&label=ja&style=flat&logo=crowdin&query=%24.progress.0.data.translationProgress&url=https%3A%2F%2Fbadges.awesome-crowdin.com%2Fstats-15691355-777584-update.json)](https://crowdin.com/project/mcaf-resourcepack)

## 常见问题

**Q: 游戏内出现未翻译文本怎么办？**

A: 请到[Crowdin](#参与翻译)参与贡献。如果 Crowdin 上也没有该文本，通常为硬编码，资源包无法修复。

**Q: 游戏内出现本地化键名（如`rule.food_restriction.air_block`）怎么办？**

A: 通常是语言文件缺失。请在[Issues](https://github.com/mc-wiki/mcaf-resourcepack/issues)反馈。

<!-- Do not translate the following part -->

## 香港繁体和文言

香港繁体和文言的加入，向前覆盖至 2019 年 8 月 22 日发布的快照 19w34a。其晚于 2019 年愚人节快照 3D Shareware v1.34 的发布时间。

因此，自 15w14a 至 3D Shareware v1.34：

- Crowdin 项目和自动打包的资源包中仍会包含相关语言文件，方便 Wiki 编写时参考。
- 上述两种语言不会出现在语言列表，正常游戏内不可用。
- 若有使用需求，请自行修改压缩包中的`pack.mcmeta`，格式如下（需去除注释）。

```jsonc
{
  "pack": {
    // 无需修改此段内容
  },
  "language": {
    "zh_hk": {
      // 15w14a时改为"zh_HK"
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
