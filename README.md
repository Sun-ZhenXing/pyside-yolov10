# YOLOv10 & PySide

使用 PySide6 构建 UI，部署 ONNX YOLOv10 模型，可轻量化打包，使用 ONNXRuntime 推理。

## 特征

本项目为 YOLOv10 参考项目，提供了 训练、推理、导出和 ONNX 模型的部署示例。

更多：

- [x] [YOLOv8 OBB：训练旋转框检测](./notebook/obb.ipynb)
- [x] 提供 ONNX 推理示例
- [ ] 提供 OBB 的 ONNX 推理示例
- [ ] 支持更多平台，包括 MacOS 和 Ubuntu
- [ ] 文档：训练、推理、模型导出
- [ ] 文档：打包部署

参考了 [X-AnyLabeling: `export_yolov10_onnx.py`](https://github.com/CVHub520/X-AnyLabeling/blob/main/tools/export_yolov10_onnx.py) 的实现。

## 开始

推荐环境：Python 3.10

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

## 构建可执行程序

使用 Nuitka 编译 Python 代码，Windows 打包：

```bash
set UPX_PATH=...
scripts\build.bat
```

Windows 测试打包：

```bash
scripts\build-test.bat
```

## 协议

[AGPLv3](./LICENSE).
