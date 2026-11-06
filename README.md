# image-dark-mode

> 图片暗黑模式自动转换器 —— 让任何平台的图片都能完美适配暗黑模式

## 🎯 项目简介

解决暗黑模式下"图片刺眼"问题：当用户处于暗黑模式时，网页、电子书、APP 中的图片也能自动切换为暗黑版本。

### 核心功能

- **A 类（文字/图形类）**：流程图、示意图、图表 → 精确重着色，生成"完美"暗黑版
- **B 类（照片/绘画类）**：照片、插画 → 色调映射，牺牲部分信息，优先保证暗黑体验
- **一键查看原图**：用户可以随时切换回原图

### 技术路线

1. **CLI 工具**：Python 原型，支持批量处理
2. **浏览器扩展**：自动拦截未适配图片，提供降级方案
3. **标准推动**：`image.dark.png` 命名约定 + `<img data-dark-src="">` 属性

## 📦 安装

### 系统要求

- Python 3.8+
- pip

### 创建虚拟环境

```bash
# Windows (PowerShell)
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# macOS/Linux
python3 -m venv .venv
source .venv/bin/activate
```

### 安装依赖

```bash
pip install -r requirements.txt
```

### 开发安装（推荐）

```bash
pip install -e ".[dev]"
```

## 🚀 快速开始

### 单文件处理

```bash
# 自动分类处理
python src/cli.py --input flowchart.png --output flowchart.dark.png

# 指定类型和强度
python src/cli.py --input photo.jpg --type photo --intensity strong
```

### 批量处理

```bash
python src/cli.py --batch ./images --output-dir ./output
```

### 命令行选项

| 参数 | 说明 | 默认值 |
|------|------|--------|
| `--input`, `-i` | 输入图片路径 | 必填 |
| `--output`, `-o` | 输出图片路径 | `<input>.dark.<ext>` |
| `--type`, `-t` | 图片类型：auto/text/photo | auto |
| `--intensity`, `-I` | 变暗强度：light/medium/strong | medium |
| `--batch`, `-b` | 批量处理目录 | - |
| `--output-dir` | 批量处理输出目录 | 与输入目录相同（暗黑版与原图同目录） |

## 📊 项目结构

```
image-dark-mode/
├── src/                    # 源码目录
│   ├── __init__.py         # 包初始化
│   ├── cli.py              # 命令行入口
│   ├── classifier.py       # 图片分类器
│   └── processor.py        # 图片处理器
├── tests/                  # 测试目录
│   ├── __init__.py
│   ├── test_classifier.py
│   └── test_processor.py
├── docs/                   # 文档目录
│   ├── 需求分析与方案.md
│   ├── 市场调研报告.md
│   ├── 算法实现详解.md      # A/B 类算法解读 + 演进记录
│   ├── 项目初始化报告.md
│   └── CLAUDE.md
├── samples/                # 测试图片（原图 + .dark 对比图）
├── .venv/                  # 虚拟环境（已忽略）
├── .flake8                 # flake8 配置（flake8 不读 pyproject.toml）
├── .gitignore
├── pyproject.toml
├── requirements.txt
└── VENV_SETUP.md
```

## 🧪 运行测试

```bash
# 运行所有测试
pytest

# 运行测试并生成覆盖率报告
pytest --cov=src --cov-report=html

# 运行特定测试文件
pytest tests/test_classifier.py -v
```

## 🧹 代码检查

```bash
# 格式化（配置见 pyproject.toml 的 [tool.black]）
black src tests

# 静态检查（配置见根目录 .flake8；flake8 不读取 pyproject.toml）
flake8 src tests

# 类型检查
mypy src
```

## 📚 技术方案

详见 [docs/需求分析与方案.md](docs/需求分析与方案.md) 与 [docs/算法实现详解.md](docs/算法实现详解.md)

### 图片分类

- **A 类特征**：高白底比例、低饱和度、高边缘密度、颜色数量少
- **B 类特征**：低白底比例、高饱和度、低边缘密度、颜色数量多

### 处理算法

#### A 类（文字/图形）
全图统一反色：`new = 255 - old`，白底变黑底、深色文字变浅色。
与浏览器/阅读器的暗黑模式做法一致，逻辑简单、对比度稳定。

> 注：全图反色会同时翻转**色相**，彩色语义块（如绿色图例）会变成补色（紫色）。
> 这是 [算法实现详解](docs/算法实现详解.md) §8.1 v2 决策的已知代价——当初的评估只覆盖了
> 浅灰文字的对比度，没有纳入彩色元素这一维度。是否改为「只翻明度、保留色相」尚未决定，
> 它与 [需求分析](docs/需求分析与方案.md) §3.1「彩色元素保持色相」的表述存在冲突，待评估。
> 另注：`--intensity` 三档强度目前**对 A 类无效**，只影响 B 类。

#### B 类（照片/绘画）
1. RGB → HSV 转换
2. 降亮度：`V = V × 0.7`
3. 降饱和度：`S = S × 0.6`
4. HSV → RGB 还原

## 🎯 里程碑

- [x] M0: 项目初始化 + 需求分析
- [x] M1: 核心算法原型（Python CLI）
- [ ] M2: 浏览器扩展
- [ ] M3: 标准文档 + Calibre 插件集成

## 🤝 贡献指南

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启 Pull Request

## 📄 许可证

MIT License

## 🔗 相关链接

- [需求分析与方案](docs/需求分析与方案.md)
- [市场调研报告](docs/市场调研报告.md)
- [算法实现详解](docs/算法实现详解.md)
- [项目初始化报告](docs/项目初始化报告.md)
- [竞品分析：dark_mode_generator](https://github.com/francofbv/dark_mode_generator)
- [Dark Reader 源码分析](https://github.com/darkreader/darkreader)

---

*项目状态：Alpha*
*最后更新：2026-11-06*