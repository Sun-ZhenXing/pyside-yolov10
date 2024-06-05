# pyside-yolo-ui

## 1. 开始

推荐环境：

- Python 3.10+

创建虚拟环境：

```bash
python -m venv venv
```

激活虚拟环境：

```bash
# Windows
venv\Scripts\activate
# Linux / MacOS
source venv/bin/activate
```

> [!TIP]
> 如果没有安装 `pipx` 先安装 `pipx`：
>
> ```bash
> pip install pipx
> ```
>
> 本项目使用 Poetry 管理，推荐使用 VS Code 开发，如果没有安装 Poetry，请先安装：
>
> ```bash
> pipx install poetry
> ```

下面的操作请在虚拟环境下工作，安装依赖：

```bash
poetry install --no-root
```

安装 Git 钩子：

```bash
pre-commit install
```

运行：

```bash
python main.py
```

格式化：

```bash
ruff . --fix
```

或者：

```bash
isort .
black .
```

测试 Git 钩子：

```bash
pre-commit run --all-files
```

## 2. 构建可执行程序

使用 Nuitka 编译 Python 代码：

```bash
python -m nuitka --standalone --mingw64 ^
    --plugin-enable=pyside6 ^
    --output-dir=dist ^
    --python-flag=no_docstrings,no_asserts ^
    --assume-yes-for-downloads ^
    main.py
```

## 3. 说明

先检查你的 PyTorch 是否支持 CUDA 推理：

```bash
python -c "print(__import__('torch').cuda.is_available())"
pip list | grep torch
```

如果你的返回结果是 `True` 和以 `cu121` 等结尾的版本号，那么你的 PyTorch 支持 CUDA 推理。

训练：

```bash
yolo detect train data=data/logo.yaml model=yolov10m.pt epochs=100 imgsz=640 batch=-1 seed=20242024
```
