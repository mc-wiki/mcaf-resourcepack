# Minecraft エイプリルフール翻訳パック

[English](README.md) | 日本語 | [简体中文](README.zh-cn.md)

**Minecraft Wiki コミュニティによるエイプリルフールバージョンの翻訳リソースパックです。**

エイプリルフールのバージョンは Crowdin での公式翻訳が行われておらず、通常では独自の要素は英語で表示されてしまいます。

このリソースパックは Minecraft Wiki コミュニティによる翻訳を適用し、Wiki 上の表記と整合性の取れた翻訳でエイプリルフールのバージョンを遊べるようにします。

## 機能

- エイプリルフールのバージョンの正確で最新の翻訳を適用します。
- 欠落した翻訳や、主要な誤植（24w14potato：`shepard_potato.png`→`shepherd_potato.png`など）を修正します。

現在対応している言語：

- `ja`: 日本語
- `lzh`: 漢文
- `zh_cn`: 簡体字（中国本土）
- `zh_hk`: 繁体字（香港）
- `zh_tw`: 繁体字（台湾）

## 使用方法

1. [最新の Release 版](https://github.com/mc-wiki/mcaf-resourcepack/releases/latest)のページを開く
2. 希望のバージョンのリソースパックをダウンロード
3. ゲーム内に追加

リソースパックの追加方法については[Wikiの該当ページ](https://ja.minecraft.wiki/w/リソースパック_(Java_Edition)#リソースパックの追加)を参照してください。

> [!NOTE]
> Minecraft 2.0 はこのバージョン自体がリソースパックに対応していないため、本プロジェクトには含まれていません。

## 貢献

### 翻訳

Crowdin から翻訳に参加できます：
[https://crowdin.com/project/mcaf-resourcepack](https://crowdin.com/project/mcaf-resourcepack)

[![zh-CN translation progress](https://img.shields.io/badge/dynamic/json?color=blue&label=zh-CN&style=flat&logo=crowdin&query=%24.progress.2.data.translationProgress&url=https%3A%2F%2Fbadges.awesome-crowdin.com%2Fstats-15691355-777584-update.json)](https://crowdin.com/project/mcaf-resourcepack)
[![zh-HK translation progress](https://img.shields.io/badge/dynamic/json?color=blue&label=zh-HK&style=flat&logo=crowdin&query=%24.progress.3.data.translationProgress&url=https%3A%2F%2Fbadges.awesome-crowdin.com%2Fstats-15691355-777584-update.json)](https://crowdin.com/project/mcaf-resourcepack)
[![zh-TW translation progress](https://img.shields.io/badge/dynamic/json?color=blue&label=zh-TW&style=flat&logo=crowdin&query=%24.progress.4.data.translationProgress&url=https%3A%2F%2Fbadges.awesome-crowdin.com%2Fstats-15691355-777584-update.json)](https://crowdin.com/project/mcaf-resourcepack)
[![lzh translation progress](https://img.shields.io/badge/dynamic/json?color=blue&label=lzh&style=flat&logo=crowdin&query=%24.progress.1.data.translationProgress&url=https%3A%2F%2Fbadges.awesome-crowdin.com%2Fstats-15691355-777584-update.json)](https://crowdin.com/project/mcaf-resourcepack)
[![ja translation progress](https://img.shields.io/badge/dynamic/json?color=blue&label=ja&style=flat&logo=crowdin&query=%24.progress.0.data.translationProgress&url=https%3A%2F%2Fbadges.awesome-crowdin.com%2Fstats-15691355-777584-update.json)](https://crowdin.com/project/mcaf-resourcepack)

## よくある質問

**Q: ゲーム上で未翻訳のテキストが出現します。**

A: [Crowdin](#translating) から翻訳にご協力ください。Crowdin に文字列が存在しない場合、そのテキストはゲームのコード上で直接定義されていてリソースパックで翻訳できないものです。

**Q: 生の翻訳キー（例：`rule.food_restriction.air_block`）が出現します。**

A: 言語ファイルから項目が欠落しています。[Issues](https://github.com/mc-wiki/mcaf-resourcepack/issues) から報告していただけると幸いです。
