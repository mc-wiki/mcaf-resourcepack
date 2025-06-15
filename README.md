# Minecraft April Fools' Translation Resource Pack

English | [简体中文](README.zh-cn.md)

## Introduction

Since 2024, the April Fools' snapshots were fulfilled like a small mod. However, these snapshots will never be localized through Crowdin, which may make editors confusing while editing/translating related entries.

Therefore, this project was created both to promote consensus in Wiki groups while editing/translating and to distribute *in-game Wiki-translation resource packs*.

## Features

- For other language players, this project provides the latest localization support for April Fools' snapshots as quickly and accurately as possible.
  - Currently support 4 languages (`zh-CN`, `zh-HK`, `zh-TW` and `lzh`).
- For English players, this project also fixes issues like missing translation keys or severe typos as it can (like file `shepherd_potato.png` for Potato Shepherd was misspelled as `shepard_potato.png` in 2024).

## How to Use

Check the [Latest Release](https://github.com/mc-wiki/mcaf-resourcepack/releases/latest), download the pack you need and install it in your game.

In case you don't know how to install a resource pack, please read [this article](https://minecraft.wiki/w/Tutorial:Loading_a_resource_pack).

Additionally, since resource pack hadn't been available when Minecraft 2.0 was released, currently that version will not be planned for this project.

## Contribution Guidance

### Participate in Translation

Crowdin: [https://crowdin.com/project/mcaf-resourcepack](https://crowdin.com/project/mcaf-resourcepack)

[![zh-CN translation](https://img.shields.io/badge/dynamic/json?color=blue&label=zh-CN&style=flat&logo=crowdin&query=%24.progress.1.data.translationProgress&url=https%3A%2F%2Fbadges.awesome-crowdin.com%2Fstats-15691355-777584-update.json)](https://crowdin.com/project/mcaf-resourcepack)
[![zh-HK translation](https://img.shields.io/badge/dynamic/json?color=blue&label=zh-HK&style=flat&logo=crowdin&query=%24.progress.2.data.translationProgress&url=https%3A%2F%2Fbadges.awesome-crowdin.com%2Fstats-15691355-777584-update.json)](https://crowdin.com/project/mcaf-resourcepack)
[![zh-TW translation](https://img.shields.io/badge/dynamic/json?color=blue&label=zh-TW&style=flat&logo=crowdin&query=%24.progress.3.data.translationProgress&url=https%3A%2F%2Fbadges.awesome-crowdin.com%2Fstats-15691355-777584-update.json)](https://crowdin.com/project/mcaf-resourcepack)
[![lzh translation](https://img.shields.io/badge/dynamic/json?color=blue&label=lzh&style=flat&logo=crowdin&query=%24.progress.0.data.translationProgress&url=https%3A%2F%2Fbadges.awesome-crowdin.com%2Fstats-15691355-777584-update.json)](https://crowdin.com/project/mcaf-resourcepack)

### FAQ

During gameplay, if you encounter untranslated texts:

- Contribute on Crowdin (see [above](#participate-in-translation)).
- If the text is not found on Crowdin, it is most likely hardcoded and cannot be fixed by the resource pack.

If you encounter raw translation keys (such as `rule.food_restriction.air_block`) during gameplay:

- This is usually due to missing entries in language files. You can report it in this repository's [Issues](https://github.com/mc-wiki/mcaf-resourcepack/issues).
