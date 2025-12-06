# 愚人节翻译包

[![Modrinth](https://img.shields.io/modrinth/dt/april-fools-translation?label=Modrinth&color=darkgreen&labelColor=black&logo=modrinth)](https://modrinth.com/mod/april-fools-translation)
[![Crowdin](https://badges.crowdin.net/mcaf-resourcepack/localized.svg)](https://crowdin.com/project/mcaf-resourcepack)

[Deutsch](README.de.md) | [English](README.md) | [日本語](README.ja.md) | 简体中文 | [繁體中文](README.zh-hant.md)

**使用来自 Minecraft Wiki 的翻译，畅玩愚人节快照。**

愚人节快照不会通过 Crowdin 官方本地化，但 Minecraft Wiki 社区会为其内容提供翻译。本项目整合了这些翻译，便于玩家间交流和对 wiki 条目命名达成共识。

## 项目特色

- 提供准确、及时的愚人节快照本地化支持。
- 修复缺失的本地化键名和严重错别字（如将 24w14potato 中的`shepard_potato.png`更正为`shepherd_potato.png`）。

### 支持版本

- [15w14a](https://zh.minecraft.wiki/w/15w14a)（2015）
- [1.RV-Pre1](https://zh.minecraft.wiki/w/Java版1.RV-Pre1)（2016）
- [3D Shareware v1.34](https://zh.minecraft.wiki/w/Java版3D_Shareware_v1.34)（2019）
- [20w14∞](https://zh.minecraft.wiki/w/20w14infinite)（2020）
- [22w13oneBlockAtATime](https://zh.minecraft.wiki/w/22w13oneBlockAtATime)（2022）
- [23w13a_or_b](https://zh.minecraft.wiki/w/23w13a_or_b)（2023）
- [24w14potato](https://zh.minecraft.wiki/w/24w14potato)（2024）
- [25w14craftmine](https://zh.minecraft.wiki/w/25w14craftmine)（2025）

因[Minecraft 2.0](https://zh.minecraft.wiki/w/Java版2.0)（2013）发布时还未支持资源包功能，此版本将**不会**包含在本项目中。

### 支持语言

本项目的翻译工作在[https://zh.crowdin.com/project/mcaf-resourcepack](https://zh.crowdin.com/project/mcaf-resourcepack)上进行。

| 代码 | 语言 | 显示名称 | 进度 | 已翻译 | 已批准 |
| --- | --- | --- | --- | ---: | ---: |
| `de_de` | 德语 | Deutsch (Deutschland) | <img src="badges/de_de.png"> | 17% | 0% |
| `en_ud` | 颠倒英语 | ɥsᴉꞁᵷuƎ (uʍoᗡ ǝpᴉsd∩) | <img src="badges/en_ud.png"> | 100% | 100% |
| `enp` | 纯粹英语 | Anglish (Oned Riches) | <img src="badges/enp.png"> | 36% | 36% |
| `es_es` | 西班牙语 | Español (España) | <img src="badges/es_es.png"> | 0% | 0% |
| `fr_fr` | 法语 | Français (France) | <img src="badges/fr_fr.png"> | 1% | 0% |
| `it_it` | 意大利语 | Italiano (Italia) | <img src="badges/it_it.png"> | 0% | 0% |
| `ja_jp` | 日语 | 日本語 (日本) | <img src="badges/ja_jp.png"> | 100% | 29% |
| `ko_kr` | 韩语 | 한국어 (대한민국)| <img src="badges/ko_kr.png"> | 82% | 1% |
| `lzh` | 汉语（文言文） | 文言 (華夏)| <img src="badges/lzh.png"> | 100% | 37% |
| `nl_nl` | 荷兰语 | Nederlands (Nederland) | <img src="badges/nl_nl.png"> | 0% | 0% |
| `pt_br` | 巴西葡萄牙语 | Português (Brasil) | <img src="badges/pt_br.png"> | 3% | 3% |
| `pt_pt` | 葡萄牙语 | Português (Portugal) | <img src="badges/pt_pt.png"> | 0% | 0% |
| `ru_ru` | 俄语 | Русский (Россия) | <img src="badges/ru_ru.png"> | 9% | 0% |
| `th_th` | 泰语 | ไทย (ประเทศไทย) | <img src="badges/th_th.png"> | 0% | 0% |
| `uk_ua` | 乌克兰语 | Українська (Україна) | <img src="badges/uk_ua.png"> | 0% | 0% |
| `zh_cn` | 汉语 | 简体中文 (中国大陆) | <img src="badges/zh_cn.png"> | 100% | 89% |
| `zh_hk` | 汉语 | 繁體中文 (香港特別行政區) | <img src="badges/zh_hk.png"> | 52% | 43% |
| `zh_tw` | 汉语 | 繁體中文 (台灣) | <img src="badges/zh_tw.png"> | 66% | 1% |

可以在本仓库中[提交issue](https://github.com/mc-wiki/mcaf-resourcepack/issues)申请新语言。

## 如何使用

1. 前往[最新 Releases](https://github.com/mc-wiki/mcaf-resourcepack/releases/latest)页面（每3小时同步）或[Modrinth](https://modrinth.com/resourcepack/april-fools-translation)（每周同步）。
2. 下载所需语言的资源包。
3. 安装到你的游戏中。

不会安装？请参阅[wiki 教程](https://zh.minecraft.wiki/w/Tutorial:加载资源包)。

## 贡献方法

欢迎在 Crowdin 上完善翻译：
[https://zh.crowdin.com/project/mcaf-resourcepack](https://zh.crowdin.com/project/mcaf-resourcepack)

## 常见问题

**Q1：游戏内出现未翻译文本怎么办？**

A1：请到[Crowdin](#贡献方法)参与贡献。如果 Crowdin 上也没有该文本，通常为硬编码，资源包无法修复。

**Q2：游戏内出现本地化键名（如`rule.food_restriction.air_block`）怎么办？**

A2：通常是语言文件缺失。请在[Issues](https://github.com/mc-wiki/mcaf-resourcepack/issues)反馈。

<!-- The following content is specifically provided for zh_hk and lzh players, and can be omitted.-->

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
