# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 项目简介

**image-dark-mode** —— 图片暗黑模式切换方案与工具。

解决暗黑模式下"图片刺眼"问题：当用户处于暗黑模式时，网页 / 电子书 / APP 中的图片也能自动切换为暗黑版本。

- **A 类（文字/图形类）**：流程图、示意图、图表 → 精确重着色，生成"完美"暗黑版。
- **B 类（照片/绘画类）**：照片、插画 → 色调映射（降亮度/降饱和度），牺牲部分信息，并提供"查看原图"切换。

交付物：
1. 一套通用准则（命名约定 + HTML 属性约定）
2. 图片处理工具（CLI → 浏览器扩展 / 阅读器插件 / APP SDK）

## 当前状态

**M1 进行中**：核心算法原型（Python CLI）已搭建框架，待实现和测试。

## 目录结构

- `docs/` —— 需求分析、方案设计、标准文档
  - `需求分析与方案.md` —— 需求分析 + 流程图（Mermaid）
  - `市场调研报告.md` —— 竞品分析（Dark Reader、pdf-dark-mode-converter 等）
  - `CLAUDE.md` —— docs 目录专属说明
- `src/` —— 核心算法与工具源码
  - `__init__.py` —— 包初始化
  - `cli.py` —— 命令行入口
  - `classifier.py` —— 图片分类器（A/B 类自动识别）
  - `processor.py` —— 图片处理器（A 类重着色 / B 类色调映射）
- `tests/` —— 测试用例
  - `test_classifier.py` —— 分类器测试
  - `test_processor.py` —— 处理器测试
- `.venv/` —— Python 虚拟环境（已在 .gitignore 中忽略）

## 核心约定

- **暗黑版命名**：`<name>.dark.<ext>`，与原图同目录（如 `flow.png` ↔ `flow.dark.png`）
- **HTML 约定**：`<img src="flow.png" data-dark-src="flow.dark.png">`
- **文档语言**：中文为主，技术名词保留英文；流程图使用 Mermaid。
- 涉及算法 / 标准 / 架构的决策需在 `docs/` 下留档，避免只存在于对话中。

## 虚拟环境管理

本项目使用 Python 虚拟环境（.venv）管理依赖。

### 创建虚拟环境

```bash
# Windows (PowerShell)
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# Windows (CMD)
python -m venv .venv
.venv\Scripts\activate.bat

# macOS/Linux
python3 -m venv .venv
source .venv/bin/activate
```

### 安装依赖

```bash
pip install -r requirements.txt
# 或开发安装（包含测试工具）
pip install -e ".[dev]"
```

### 验证安装

```bash
python --version  # 应显示 3.8+
pip list          # 检查依赖是否安装
python -m pytest tests/  # 运行测试
```

详细说明见 [VENV_SETUP.md](VENV_SETUP.md)

## 常用命令

### 开发命令

```bash
# 激活虚拟环境
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate

# 运行测试
pytest tests/ -v

# 运行测试并生成覆盖率报告
pytest tests/ --cov=src --cov-report=html

# 代码格式化
black src/ tests/
flake8 src/ tests/

# 类型检查
mypy src/
```

### CLI 命令

```bash
# 单文件处理
python src/cli.py --input flowchart.png --output flowchart.dark.png

# 指定类型和强度
python src/cli.py --input photo.jpg --type photo --intensity strong

# 批量处理
python src/cli.py --batch ./images --output-dir ./output
```

## 与 docs/CLAUDE.md 的关系

- 根目录 `CLAUDE.md`：全局约定与项目概览。
- `docs/CLAUDE.md`：文档编写规范与索引。
- 各子目录 `CLAUDE.md`：该目录的职责说明、模块清单和编码约定。

## 目录规范

**每次新建子目录时，必须同步创建该目录下的 `CLAUDE.md`**，内容至少包含：
1. 目录职责说明（一两句话）
2. 文件清单（文件名 → 作用）
3. 必要的编码/组织约定

已存在的目录说明：
- `src/` → `src/CLAUDE.md`（核心算法与工具）
- `docs/` → `docs/CLAUDE.md`（文档规范与索引）
- `tests/` → `tests/CLAUDE.md`（测试用例规范）
- `samples/` → `samples/CLAUDE.md`（测试图片样本）

## 文档更新规则

**涉及 docs/ 下文档的修改，必须先告知用户会不会删除/覆盖原有记录，由用户确认后再执行。**

- 追加新内容（不删原记录）→ 可直接执行
- 修改/重写已有内容（可能影响原记录）→ 先说明范围，等用户确认
- 新建文档 → 直接执行

## 测试规则

**即使在 auto mode 下，涉及运行测试前，必须先告知用户以下内容，经确认后再执行：**

1. **测试目标** — 要验证什么功能
2. **测试方式** — 怎么跑（命令、脚本、手动操作等）
3. **预期结果** — 期望看到什么输出或文件变化
4. **副作用** — 会生成哪些新文件、覆盖哪些现有文件、是否会修改原始数据

用户同意后方可开始测试。