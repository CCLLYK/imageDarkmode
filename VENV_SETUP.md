# Python 虚拟环境配置

## 创建虚拟环境

本项目使用 Python 虚拟环境管理依赖。虚拟环境创建于项目根目录下的 `.venv` 文件夹。

### Windows (PowerShell)

```powershell
cd D:\ClaudeCode\image-dark-mode
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### Windows (CMD)

```cmd
cd D:\ClaudeCode\image-dark-mode
python -m venv .venv
.venv\Scripts\activate.bat
pip install -r requirements.txt
```

### macOS/Linux

```bash
cd /path/to/image-dark-mode
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## 验证安装

```bash
python --version
pip list
```

## 常用命令

```bash
# 激活虚拟环境
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate

# 安装包
pip install <package>

# 保存依赖到 requirements.txt
pip freeze > requirements.txt

# 退出虚拟环境
deactivate
```

## 当前项目依赖

- Python 3.8+
- OpenCV (cv2)
- NumPy
- Pillow