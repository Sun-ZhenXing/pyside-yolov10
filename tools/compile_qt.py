import os
import subprocess
from pathlib import Path

BASE_DIR = "app/"
UI_FILE_DIR = f"{BASE_DIR}widgets"
RESOURCE_FILE = "resources.qrc"
RESOURCE_DIR = "assets"

QRC_TEMPLATE = """<RCC>
    <qresource prefix="/res">
        {items}
    </qresource>
</RCC>"""


def generate_qrc():
    """生成 .qrc 文件"""
    items = []
    for root, _, files in os.walk(RESOURCE_DIR):
        for file in files:
            items.append(
                os.path.join(BASE_DIR, root, file)
                .replace("\\", "/")
                .removeprefix(BASE_DIR)
            )
    with open(RESOURCE_FILE, "w", encoding="utf-8") as f:
        f.write(
            QRC_TEMPLATE.format(
                items="\n        ".join(f"<file>{item}</file>" for item in items)
            )
        )
        f.write("\n")
    cmd = [
        "pyside6-rcc",
        "-o",
        os.path.normpath(RESOURCE_FILE).replace(".qrc", "_rc.py"),
        os.path.normpath(RESOURCE_FILE),
    ]
    subprocess.run(cmd)


def generate_uic():
    """通过 .ui 文件生成 .py 文件"""
    ui_files = Path(UI_FILE_DIR).glob("*.ui")
    for ui_file in ui_files:
        ui_file = str(ui_file)
        py_file = ui_file.replace(".ui", "_ui.py")
        subprocess.run(["pyside6-uic", ui_file, "-o", py_file])


if __name__ == "__main__":
    generate_qrc()
    generate_uic()
