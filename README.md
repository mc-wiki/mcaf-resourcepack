# Minecraft April Fools' Translation Packs

English | [简体中文](README.zh-cn.md)

**Play April Fools' snapshots with community-driven translations from the Minecraft Wiki.**

April Fools' snapshots are not officially localized via Crowdin, but the Minecraft Wiki community provides translations for their features. This project consolidates those translations to facilitate communication and promote consensus on item names.

## Features

- Provides accurate and up-to-date localization for April Fools' snapshots.
- Fixes missing translation keys and major typos (e.g., correcting `shepard_potato.png` to `shepherd_potato.png` in 24w14potato).

All currently supported languages:

- `lzh`: 文言
- `zh_cn`: 简体中文（中国大陆）
- `zh_hk`: 繁體中文（香港特別行政區）
- `zh_tw`: 繁體中文（台灣）

## How to use

1. Visit the [Latest Release](https://github.com/mc-wiki/mcaf-resourcepack/releases/latest) page.
2. Download the resource pack for your language.
3. Install it in your game.

Need help installing? See the [wiki tutorial](https://minecraft.wiki/w/Tutorial:Loading_a_resource_pack).

> [!NOTE]
> Minecraft 2.0 is not included in this project as resource packs were unavailable in that version.

## Contributing

### Translating

Help improve translations on Crowdin:
[https://crowdin.com/project/mcaf-resourcepack](https://crowdin.com/project/mcaf-resourcepack)

[![zh-CN translation progress](https://img.shields.io/badge/dynamic/json?color=blue&label=zh-CN&style=flat&logo=crowdin&query=%24.progress.1.data.translationProgress&url=https%3A%2F%2Fbadges.awesome-crowdin.com%2Fstats-15691355-777584-update.json)](https://crowdin.com/project/mcaf-resourcepack)
[![zh-HK translation progress](https://img.shields.io/badge/dynamic/json?color=blue&label=zh-HK&style=flat&logo=crowdin&query=%24.progress.2.data.translationProgress&url=https%3A%2F%2Fbadges.awesome-crowdin.com%2Fstats-15691355-777584-update.json)](https://crowdin.com/project/mcaf-resourcepack)
[![zh-TW translation progress](https://img.shields.io/badge/dynamic/json?color=blue&label=zh-TW&style=flat&logo=crowdin&query=%24.progress.3.data.translationProgress&url=https%3A%2F%2Fbadges.awesome-crowdin.com%2Fstats-15691355-777584-update.json)](https://crowdin.com/project/mcaf-resourcepack)
[![lzh translation progress](https://img.shields.io/badge/dynamic/json?color=blue&label=lzh&style=flat&logo=crowdin&query=%24.progress.0.data.translationProgress&url=https%3A%2F%2Fbadges.awesome-crowdin.com%2Fstats-15691355-777584-update.json)](https://crowdin.com/project/mcaf-resourcepack)

## FAQ

**Q: I see untranslated text in-game. What should I do?**

A: Contribute translations on [Crowdin](#translating). If the text isn't on Crowdin, it's likely hardcoded and can't be fixed by a resource pack.

**Q: I see raw translation keys (e.g., `rule.food_restriction.air_block`).**

A: This usually means a missing entry in the language files. Please report it in the [Issues](https://github.com/mc-wiki/mcaf-resourcepack/issues) section.
