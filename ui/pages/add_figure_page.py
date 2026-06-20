from services.figure_service import add_figure

from PySide6.QtWidgets import *

from PySide6.QtGui import (
    QPixmap,
    QFontDatabase
)

from PySide6.QtCore import Qt



class AddFigurePage(QWidget):


    def __init__(self):

        super().__init__()

        self.image_path = ""

        self.load_font()

        self.init_ui()



    def load_font(self):

        font_id = QFontDatabase.addApplicationFont(
            "assets/fonts/equestria_cyrillic.ttf"
        )

        fonts = QFontDatabase.applicationFontFamilies(
            font_id
        )


        self.font = (
            fonts[0]
            if fonts
            else "Arial"
        )



    def init_ui(self):


        main = QVBoxLayout()



        title = QLabel(
            "Добавление фигурки"
        )


        title.setStyleSheet(f"""

        color:#D84B8A;

        font-size:42px;

        font-family:"{self.font}";

        """)



        main.addWidget(
            title
        )



        body = QHBoxLayout()


        photo = QFrame()


        photo.setFixedSize(
            430,
            430
        )


        photo.setStyleSheet("""

        background:#F3B1CA;

        border-radius:25px;

        """)



        photo_layout = QVBoxLayout()



        self.image = QLabel(
            "Добавить фото"
        )


        self.image.setAlignment(
            Qt.AlignCenter
        )


        self.image.setStyleSheet(f"""

        color:#D84B8A;

        font-size:22px;

        font-family:"{self.font}";

        """)



        button = QPushButton(
            "📷 Добавить фото"
        )


        button.clicked.connect(
            self.choose_photo
        )



        photo_layout.addWidget(
            self.image
        )


        photo_layout.addWidget(
            button
        )


        photo.setLayout(
            photo_layout
        )



        body.addWidget(
            photo
        )

        fields = QVBoxLayout()



        self.name = QLineEdit()

        self.name.setPlaceholderText(
            "Имя"
        )



        self.type = QComboBox()

        self.type.addItems(
            [
                "Пони",
                "Набор",
                "Блайнд-бэг"
            ]
        )



        self.series = QLineEdit()

        self.series.setPlaceholderText(
            "Серия"
        )



        self.rarity = QComboBox()

        self.rarity.addItems(
            [
                "Обычная",
                "Редкая",
                "Эксклюзив"
            ]
        )



        self.date = QLineEdit()

        self.date.setPlaceholderText(
            "Дата покупки"
        )



        self.price = QLineEdit()

        self.price.setPlaceholderText(
            "Цена"
        )



        self.condition = QComboBox()

        self.condition.addItems(
            [
                "Новая",
                "Хорошее состояние",
                "Есть повреждения"
            ]
        )



        self.quantity = QLineEdit()

        self.quantity.setPlaceholderText(
            "Количество"
        )



        self.note = QTextEdit()

        self.note.setPlaceholderText(
            "Заметка"
        )



        widgets = [

            self.name,

            self.type,

            self.series,

            self.rarity,

            self.date,

            self.price,

            self.condition,

            self.quantity,

            self.note

        ]



        for widget in widgets:


            widget.setStyleSheet("""

            background:white;

            border:2px solid #D84B8A;

            border-radius:15px;

            padding:8px;

            """)


            fields.addWidget(
                widget
            )


        save = QPushButton(
            "Сохранить"
        )


        cancel = QPushButton(
            "Отмена"
        )



        save.clicked.connect(
            self.save_figure
        )



        for b in [
            save,
            cancel
        ]:


            b.setStyleSheet("""

            QPushButton{

            background:#D84B8A;

            color:white;

            border-radius:20px;

            height:45px;

            font-size:18px;

            }

            """)



            fields.addWidget(
                b
            )



        body.addLayout(
            fields
        )


        main.addLayout(
            body
        )


        self.setLayout(
            main
        )



    def choose_photo(self):


        file,_ = QFileDialog.getOpenFileName(

            self,

            "Выбрать фото",

            "",

            "Images (*.png *.jpg *.jpeg)"

        )


        if file:


            self.image_path = file



            pixmap = QPixmap(
                file
            )



            self.image.setPixmap(

                pixmap.scaled(

                    350,

                    350,

                    Qt.KeepAspectRatio

                )

            )



    def save_figure(self):


        data = {


            "name":
            self.name.text(),


            "type":
            self.type.currentText(),


            "series":
            self.series.text(),


            "rarity":
            self.rarity.currentText(),


            "date":
            self.date.text(),


            "price":
            self.price.text(),


            "condition":
            self.condition.currentText(),


            "quantity":
            self.quantity.text(),


            "note":
            self.note.toPlainText(),


            "image":
            self.image_path

        }



        add_figure(
            data
        )


        QMessageBox.information(

            self,

            "Готово",

            "Фигурка добавлена"

        )