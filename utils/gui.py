import os
import sys

from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

from utils.common import is_empty
from utils.logger import log_msg

def display(title, message):
    if is_empty(os.environ.get('DISPLAY')):
        log_msg("DEBUG", "[screen] no display found, using: 0.0")
        os.environ['DISPLAY'] = ':0.0'

    app = QApplication(sys.argv)

    window = QWidget()
    window.setWindowTitle(title)
    window.showFullScreen()

    label = QLabel(message)
    label.setAlignment(Qt.AlignCenter)

    # Set a font that supports emojis (requires `fonts-noto-color-emoji` installed)
    font = QFont("Noto Color Emoji", 32)  # Increase size if needed
    label.setFont(font)

    layout = QVBoxLayout()
    layout.addWidget(label)
    window.setLayout(layout)

    # Press Escape to exit fullscreen
    def exit_fullscreen(event):
        if event.key() == Qt.Key_Escape:
            window.showNormal()

    window.keyPressEvent = exit_fullscreen

    sys.exit(app.exec_())
