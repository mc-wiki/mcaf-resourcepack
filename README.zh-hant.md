# 愚人節翻譯包

[English](README.md) | [日本語](README.ja.md) | [简体中文](README.zh-hans.md) | 繁體中文

**使用來自 Minecraft Wiki 的翻譯，暢玩愚人節快照。**

愚人節快照不會透過 Crowdin 官方在地化，但 Minecraft Wiki 社群會為其內容提供翻譯。本項目整合了這些翻譯，便於玩家間交流和對 wiki 條目命名達成共識。

## 項目特色

- 提供準確、及時的愚人節快照在地化支援。
- 修復缺失的在地化鍵名和嚴重錯字（如將 24w14potato 中的 `shepard_potato.png` 更正為 `shepherd_potato.png`）。

目前支援的語言有：

- `en_ud`：ɥsᴉꞁᵷuƎ (uʍoᗡ ǝpᴉsd∩)
- `ja_jp`：日本語 (日本)
- `lzh`：文言（華夏）
- `zh_cn`：简体中文 (中国大陆)
- `zh_hk`：繁體中文 (香港特別行政區)
- `zh_tw`：繁體中文 (台灣)

## 如何使用

1. 前往[最新 Releases](https://github.com/mc-wiki/mcaf-resourcepack/releases/latest)頁面（每3小時同步）或 [Modrinth](https://modrinth.com/resourcepack/april-fools-translation)（每週同步）。
2. 下載所需語言的資源包。
3. 安裝到你的遊戲中。

不會安裝？請參閱 [wiki 教學](https://zh.minecraft.wiki/w/Tutorial:加载资源包)。

> [!NOTE]
> Minecraft 2.0 版本因當時不支援資源包，暫不包含在本項目中。

## 貢獻方法

### 參與翻譯

歡迎在 Crowdin 上完善翻譯：
[https://zh.crowdin.com/project/mcaf-resourcepack](https://zh.crowdin.com/project/mcaf-resourcepack)

![en_ud 翻譯進度](https://img.shields.io/badge/dynamic/json?color=blue&label=en_ud&style=flat&logo=crowdin&query=%24.progress.0.data.translationProgress&url=https%3A%2F%2Fbadges.awesome-crowdin.com%2Fstats-15691355-777584-update.json)
![ja_jp 翻譯進度](https://img.shields.io/badge/dynamic/json?color=blue&label=ja_jp&style=flat&logo=crowdin&query=%24.progress.1.data.translationProgress&url=https%3A%2F%2Fbadges.awesome-crowdin.com%2Fstats-15691355-777584-update.json)
![lzh 翻譯進度](https://img.shields.io/badge/dynamic/json?color=blue&label=lzh&style=flat&logo=crowdin&query=%24.progress.2.data.translationProgress&url=https%3A%2F%2Fbadges.awesome-crowdin.com%2Fstats-15691355-777584-update.json)
![zh_cn 翻譯進度](https://img.shields.io/badge/dynamic/json?color=blue&label=zh_cn&style=flat&logo=crowdin&query=%24.progress.3.data.translationProgress&url=https%3A%2F%2Fbadges.awesome-crowdin.com%2Fstats-15691355-777584-update.json)
![zh_hk 翻譯進度](https://img.shields.io/badge/dynamic/json?color=blue&label=zh_hk&style=flat&logo=crowdin&query=%24.progress.4.data.translationProgress&url=https%3A%2F%2Fbadges.awesome-crowdin.com%2Fstats-15691355-777584-update.json)
![zh_tw 翻譯進度](https://img.shields.io/badge/dynamic/json?color=blue&label=zh_tw&style=flat&logo=crowdin&query=%24.progress.5.data.translationProgress&url=https%3A%2F%2Fbadges.awesome-crowdin.com%2Fstats-15691355-777584-update.json)

## 常見問題

**Q1：遊戲內出現未翻譯文字怎麼辦？**

A1：請到[Crowdin](#參與翻譯)參與貢獻。如果 Crowdin 上也沒有該文字，通常為硬編碼，資源包無法修復。

**Q2：遊戲內出現在地化鍵名（如 `rule.food_restriction.air_block`）怎麼辦？**

A2：通常是語言檔案缺失。請在 [Issues](https://github.com/mc-wiki/mcaf-resourcepack/issues) 回饋。

<!-- Do not translate the following part -->

## 香港繁體和文言

香港繁體和文言的加入，向前覆蓋至 2019 年 8 月 22 日發布的快照 19w34a。其晚於 2019 年愚人節快照 3D Shareware v1.34 的發布時間。

因此，自 15w14a 至 3D Shareware v1.34：

- Crowdin 項目和自動打包的資源包中仍會包含相關語言檔案，方便 Wiki 編寫時參考。
- 上述兩種語言不會出現在語言清單，正常遊戲內不可用。
- 若有使用需求，請自行修改壓縮檔中的 `pack.mcmeta`，格式如下（需去除註釋）。

```jsonc
{
  "pack": {
    // 無需修改此段內容
  },
  "language": {
    "zh_hk": {
      // 15w14a時改為"zh_HK"
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