import sys

from PySide6.QtCore import QProcess
from PySide6.QtWidgets import QApplication

from yolo_ui.config import GlobalConfig
from yolo_ui.views.main import MainWindow


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    exit_code = app.exec()
    if exit_code == GlobalConfig.RESTART_CODE:
        QProcess.startDetached(app.applicationFilePath(), sys.argv)
        sys.exit(GlobalConfig.EXIT_CODE)
    sys.exit(exit_code)
