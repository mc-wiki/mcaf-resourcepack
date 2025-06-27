# Minecraft エイプリルフール翻訳パック

[English](README.md) | 日本語 | [简体中文](README.zh-hans.md) | [繁體中文](README.zh-hant.md)

**Minecraft Wiki コミュニティによるエイプリルフールバージョンの翻訳リソースパックです。**

エイプリルフールのバージョンは Crowdin での公式翻訳が行われておらず、通常では独自の要素は英語で表示されてしまいます。

このリソースパックは Minecraft Wiki コミュニティによる翻訳を適用し、Wiki 上の表記と整合性の取れた翻訳でエイプリルフールのバージョンを遊べるようにします。

## 機能

- エイプリルフールのバージョンの正確で最新の翻訳を適用します。
- 欠落した翻訳や、主要な誤植（24w14potato：`shepard_potato.png`→`shepherd_potato.png`など）を修正します。

現在対応している言語：

- `en_ud`：ɥsᴉꞁᵷuƎ (uʍoᗡ ǝpᴉsd∩)
- `ja_jp`：日本語 (日本)
- `lzh`：文言（華夏）
- `zh_cn`：简体中文 (中国大陆)
- `zh_hk`：繁體中文 (香港特別行政區)
- `zh_tw`：繁體中文 (台灣)

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
[https://ja.crowdin.com/project/mcaf-resourcepack](https://ja.crowdin.com/project/mcaf-resourcepack)

![en_ud 翻訳進行度](https://img.shields.io/badge/dynamic/json?color=blue&label=en_ud&style=flat&logo=crowdin&query=%24.progress.0.data.translationProgress&url=https%3A%2F%2Fbadges.awesome-crowdin.com%2Fstats-15691355-777584-update.json)
![ja_jp 翻訳進行度](https://img.shields.io/badge/dynamic/json?color=blue&label=ja_jp&style=flat&logo=crowdin&query=%24.progress.1.data.translationProgress&url=https%3A%2F%2Fbadges.awesome-crowdin.com%2Fstats-15691355-777584-update.json)
![lzh 翻訳進行度](https://img.shields.io/badge/dynamic/json?color=blue&label=lzh&style=flat&logo=crowdin&query=%24.progress.2.data.translationProgress&url=https%3A%2F%2Fbadges.awesome-crowdin.com%2Fstats-15691355-777584-update.json)
![zh_cn 翻訳進行度](https://img.shields.io/badge/dynamic/json?color=blue&label=zh_cn&style=flat&logo=crowdin&query=%24.progress.3.data.translationProgress&url=https%3A%2F%2Fbadges.awesome-crowdin.com%2Fstats-15691355-777584-update.json)
![zh_hk 翻訳進行度](https://img.shields.io/badge/dynamic/json?color=blue&label=zh_hk&style=flat&logo=crowdin&query=%24.progress.4.data.translationProgress&url=https%3A%2F%2Fbadges.awesome-crowdin.com%2Fstats-15691355-777584-update.json)
![zh_tw 翻訳進行度](https://img.shields.io/badge/dynamic/json?color=blue&label=zh_tw&style=flat&logo=crowdin&query=%24.progress.5.data.translationProgress&url=https%3A%2F%2Fbadges.awesome-crowdin.com%2Fstats-15691355-777584-update.json)

## よくある質問

**Q1：ゲーム上で未翻訳のテキストが出現します。**

A1：[Crowdin](#翻訳) から翻訳にご協力ください。Crowdin に文字列が存在しない場合、そのテキストはゲームのコード上で直接定義されていてリソースパックで翻訳できないものです。

**Q2：生の翻訳キー（例：`rule.food_restriction.air_block`）が出現します。**

A2：言語ファイルから項目が欠落しています。[Issues](https://github.com/mc-wiki/mcaf-resourcepack/issues) から報告していただけると幸いです。
