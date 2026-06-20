from PySide6.QtWidgets import QGridLayout
from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QFrame,
    QHBoxLayout,
    QVBoxLayout,
    QStackedWidget,
    QScrollArea
)

from PySide6.QtGui import (
    QPixmap,
    QFontDatabase,
    QPainter,
    QPainterPath
)

from PySide6.QtCore import Qt

from ui.pages.add_figure_page import AddFigurePage

from services.figure_service import get_figures

from ui.widgets.figure_card import FigureCard



class MainWindow(QWidget):

    def __init__(self):

        super().__init__()

        self.setWindowTitle(
            "Pony Archive"
        )

        self.resize(
            1440,
            1024
        )


        self.load_font()
        self.loaded_figure_ids = []

        self.init_ui()



    def load_font(self):

        font_id = QFontDatabase.addApplicationFont(
            "assets/fonts/equestria_cyrillic.ttf"
        )


        fonts = QFontDatabase.applicationFontFamilies(
            font_id
        )


        self.pony_font = (

            fonts[0]

            if fonts

            else "Arial"

        )



    def create_avatar(self):

        size = 55


        pixmap = QPixmap(
            "assets/images/avatar.jpg"
        )


        pixmap = pixmap.scaled(
            size,
            size,
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        )


        result = QPixmap(
            size,
            size
        )


        result.fill(
            Qt.transparent
        )


        painter = QPainter(result)

        painter.setRenderHint(
            QPainter.Antialiasing
        )


        path = QPainterPath()

        path.addEllipse(
            0,
            0,
            size,
            size
        )


        painter.setClipPath(
            path
        )


        painter.drawPixmap(
            0,
            0,
            pixmap
        )


        painter.end()


        return result



    def init_ui(self):


        main = QHBoxLayout()


        main.setContentsMargins(
            0,
            0,
            0,
            0
        )


        sidebar = QFrame()


        sidebar.setFixedWidth(
            320
        )


        sidebar.setStyleSheet("""

        QFrame{

            background:#F8EEF2;

        }

        """)



        side = QVBoxLayout()


        side.setSpacing(
            8
        )


        side.setContentsMargins(
            20,
            20,
            20,
            20
        )



        logo = QLabel()


        logo.setPixmap(
            QPixmap(
                "assets/images/logo.png"
            ).scaled(
                240,
                120,
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            )
        )


        side.addWidget(
            logo,
            alignment=Qt.AlignCenter
        )



        menu = [

            "Коллекция",

            "Добавить фигурку",

            "Статистика",

            "Лист желаний",

            "Настройки",

            "О приложении"

        ]



        self.menu_buttons = []



        for text in menu:


            btn = QPushButton(text)


            btn.setFixedHeight(
                45
            )


            btn.setStyleSheet(f"""

            QPushButton{{

                background:#E99ABB;

                color:#B52A70;

                border:none;

                border-radius:18px;

                text-align:left;

                padding-left:20px;

                font-family:"{self.pony_font}";

                font-size:18px;

            }}


            QPushButton:hover{{

                background:#D84B8A;

                color:white;

            }}

            """)



            if text == "Коллекция":

                btn.clicked.connect(
                    lambda checked=False, b=btn:
                    self.change_page(0,b)
                )


            elif text == "Добавить фигурку":

                btn.clicked.connect(
                    lambda checked=False, b=btn:
                    self.change_page(1,b)
                )



            self.menu_buttons.append(
                btn
            )


            side.addWidget(
                btn
            )



        side.addStretch()


        profile = QFrame()


        profile.setFixedHeight(
            90
        )


        profile.setStyleSheet("""

        QFrame{

            background:white;

            border:2px solid #D84B8A;

            border-radius:20px;

        }

        """)



        profile_layout = QHBoxLayout()



        avatar = QLabel()


        avatar.setPixmap(
            self.create_avatar()
        )


        profile_layout.addWidget(
            avatar
        )



        user_layout = QVBoxLayout()



        nickname = QLabel(
            "Dsawari"
        )


        nickname.setStyleSheet("""

        color:#D84B8A;

        font-size:16px;

        font-weight:bold;

        """)



        email = QLabel(
            "apollinaxx@gmail.com"
        )


        email.setStyleSheet("""

        color:#D84B8A;

        font-size:11px;

        """)



        user_layout.addWidget(
            nickname
        )


        user_layout.addWidget(
            email
        )



        profile_layout.addLayout(
            user_layout
        )


        profile.setLayout(
            profile_layout
        )


        side.addWidget(
            profile
        )


        sidebar.setLayout(
            side
        )


        self.pages = QStackedWidget()


        collection = QWidget()


        collection_layout = QVBoxLayout()


        collection_layout.setAlignment(
            Qt.AlignTop
        )


        title = QLabel(
            "Моя коллекция"
        )


        title.setStyleSheet(f"""

        color:#D84B8A;

        font-size:42px;

        font-family:"{self.pony_font}";

        """)



        collection_layout.addWidget(
            title
        )



        self.cards_layout = QGridLayout()

        self.cards_layout.setSpacing(20)


        self.cards_layout.setSpacing(
            20
        )


        collection_layout.addLayout(
            self.cards_layout
        )


        collection.setLayout(
            collection_layout
        )



        add_page = AddFigurePage()



        self.pages.addWidget(
            collection
        )


        self.pages.addWidget(
            add_page
        )



        self.load_cards()


        background = QLabel()


        background.setPixmap(
            QPixmap(
                "assets/images/background.jpg"
            )
        )


        background.setScaledContents(
            True
        )



        bg_layout = QVBoxLayout(
            background
        )


        bg_layout.setContentsMargins(
            40,
            30,
            40,
            30
        )


        bg_layout.addWidget(
            self.pages
        )



        main.addWidget(
            sidebar
        )


        main.addWidget(
            background
        )



        self.setLayout(
            main
        )



    def load_cards(self):
        figures = get_figures()

        for index, figure in enumerate(figures):

            figure_id = figure[0]

            if figure_id in self.loaded_figure_ids:

                continue

            card = FigureCard(
                figure
            )

            position = self.cards_layout.count()

            row = position // 3

            column = position % 3


            self.cards_layout.addWidget(

                card,

                row,

                column

            )

            self.loaded_figure_ids.append(
                figure_id
            )


    def change_page(
        self,
        index,
        clicked_button
    ):


        self.pages.setCurrentIndex(
            index
        )


        if index == 0:

            self.load_cards()



        for button in self.menu_buttons:


            button.setStyleSheet(f"""

            QPushButton{{

                background:#E99ABB;

                color:#B52A70;

                border:none;

                border-radius:18px;

                text-align:left;

                padding-left:20px;

                font-family:"{self.pony_font}";

                font-size:18px;

            }}

            """)



        clicked_button.setStyleSheet(f"""

        QPushButton{{

            background:#D84B8A;

            color:white;

            border:none;

            border-radius:18px;

            text-align:left;

            padding-left:20px;

            font-family:"{self.pony_font}";

            font-size:18px;

        }}

        """)