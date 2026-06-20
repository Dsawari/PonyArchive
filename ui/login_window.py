from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QFrame,
    QMessageBox
)

from PySide6.QtGui import (
    QPixmap,
    QFontDatabase
)

from PySide6.QtCore import Qt

from services.auth_service import (
    login_user,
    register_user
)


class LoginWindow(QWidget):

    def __init__(self):

        super().__init__()

        self.setWindowTitle("Pony Archive")

        self.resize(1440, 1024)

        self.load_font()

        self.init_ui()

    def load_font(self):

        font_id = QFontDatabase.addApplicationFont(
            "assets/fonts/equestria_cyrillic.ttf"
        )

        families = QFontDatabase.applicationFontFamilies(
            font_id
        )

        if families:
            self.pony_font = families[0]
        else:
            self.pony_font = "Arial"

    def init_ui(self):

        self.setStyleSheet("""
            QWidget {
                background-color: #F3E8EE;
            }
        """)

        main_layout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignCenter)

        top_layout = QHBoxLayout()
        top_layout.setAlignment(Qt.AlignCenter)

        logo = QLabel()

        logo.setPixmap(
            QPixmap(
                "assets/images/logo.png"
            ).scaledToHeight(
                140,
                Qt.SmoothTransformation
            )
        )

        pinkie = QLabel()

        pinkie.setPixmap(
            QPixmap(
                "assets/images/pinkie.png"
            ).scaledToHeight(
                180,
                Qt.SmoothTransformation
            )
        )

        top_layout.addWidget(logo)
        top_layout.addSpacing(40)
        top_layout.addWidget(pinkie)

        card = QFrame()

        card.setFixedSize(520, 620)

        card.setStyleSheet("""
            QFrame {
                background-color: white;
                border-radius: 30px;
            }
        """)

        card_layout = QVBoxLayout()

        card_layout.setContentsMargins(
            40,
            40,
            40,
            40
        )

        card_layout.setSpacing(20)

        title = QLabel(
            "Войти в свою коллекцию"
        )

        title.setAlignment(
            Qt.AlignCenter
        )

        title.setStyleSheet(f"""
            color: #D13B84;
            font-size: 28px;
            font-family: "{self.pony_font}";
            background: transparent;
        """)

        self.username_input = QLineEdit()

        self.username_input.setPlaceholderText(
            "Имя пользователя"
        )

        self.username_input.setFixedHeight(
            50
        )

        self.username_input.setStyleSheet("""
            QLineEdit {
                background-color: #F7BFD0;
                border: 2px solid #D13B84;
                border-radius: 15px;
                padding-left: 15px;
                font-size: 14px;
            }
        """)

        self.password_input = QLineEdit()

        self.password_input.setPlaceholderText(
            "Пароль"
        )

        self.password_input.setEchoMode(
            QLineEdit.Password
        )

        self.password_input.setFixedHeight(
            50
        )

        self.password_input.setStyleSheet("""
            QLineEdit {
                background-color: #F7BFD0;
                border: 2px solid #D13B84;
                border-radius: 15px;
                padding-left: 15px;
                font-size: 14px;
            }
        """)

        login_button = QPushButton(
            "Войти"
        )

        login_button.setFixedHeight(
            55
        )

        login_button.clicked.connect(
            self.login
        )

        login_button.setStyleSheet("""
            QPushButton {
                background-color: #D13B84;
                color: white;
                border-radius: 15px;
                font-size: 18px;
                font-weight: bold;
            }

            QPushButton:hover {
                background-color: #B72D70;
            }
        """)

        register_button = QPushButton(
            "Создать аккаунт"
        )

        register_button.setFixedHeight(
            55
        )

        register_button.clicked.connect(
            self.register
        )

        register_button.setStyleSheet("""
            QPushButton {
                background-color: #F0C3D3;
                color: #D13B84;
                border-radius: 15px;
                font-size: 18px;
                font-weight: bold;
            }

            QPushButton:hover {
                background-color: #E8B3C7;
            }
        """)

        card_layout.addWidget(title)

        card_layout.addSpacing(20)

        card_layout.addWidget(
            self.username_input
        )

        card_layout.addWidget(
            self.password_input
        )

        card_layout.addSpacing(20)

        card_layout.addWidget(
            login_button
        )

        card_layout.addWidget(
            register_button
        )

        card.setLayout(card_layout)

        main_layout.addLayout(
            top_layout
        )

        main_layout.addSpacing(
            20
        )

        main_layout.addWidget(
            card,
            alignment=Qt.AlignCenter
        )

        self.setLayout(main_layout)

    def register(self):

        username = (
            self.username_input.text()
        )

        password = (
            self.password_input.text()
        )

        success = register_user(
            username,
            password
        )

        if success:

            QMessageBox.information(
                self,
                "Успех",
                "Пользователь создан"
            )

        else:

            QMessageBox.warning(
                self,
                "Ошибка",
                "Такой логин уже существует"
            )

    def login(self):

        username = (
            self.username_input.text()
        )

        password = (
            self.password_input.text()
        )

        success = login_user(
            username,
            password
        )

        if success:

            QMessageBox.information(
                self,
                "Успех",
                "Вход выполнен"
            )

        else:

            QMessageBox.warning(
                self,
                "Ошибка",
                "Неверный логин или пароль"
            )