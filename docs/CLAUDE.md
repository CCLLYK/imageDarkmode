# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## docs/ 目录说明

本目录是项目的文档中心，存放需求分析、方案设计、标准定义与里程碑记录。

## 文档清单

- `需求分析与方案.md` —— 项目需求分析、图片分类、方案设计、流程图（Mermaid）
- `市场调研报告.md` —— 痛点与现有方案调研（Dark Reader、css-tricks、MDN、npm/GitHub 生态等）
- `项目初始化报告.md` —— 环境配置、项目结构、核心功能说明（含 2026-11-06 环境重建记录）
- `算法实现详解.md` —— A/B 类处理算法源码解读 + 演进记录（v1→v2）

> 注：文档中的代码片段是写作时的快照。2026-11-06 起源码统一经 black 格式化
> （单引号→双引号、折行位置有调整），片段可能与 `src/` 存在纯格式差异；
> **以 `src/` 下的实现为准**，行为层面无变化。

## 文档编写约定

- 使用中文撰写，技术术语可保留英文。
- 流程图使用 Mermaid 语法绘制，便于在 Markdown 中直接渲染。
- 每个新文档在"文档清单"中添加索引行。
- 重要的算法 / 标准 / 架构决策必须形成文档，避免只存在于对话中。