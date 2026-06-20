from PySide6.QtWidgets import (
    QFrame,
    QLabel,
    QVBoxLayout
)

from PySide6.QtGui import QPixmap

from PySide6.QtCore import Qt



class FigureCard(QFrame):


    def __init__(self, figure):

        super().__init__()


        self.setFixedSize(
            220,
            300
        )


        self.setStyleSheet("""

        QFrame{

            background:white;

            border-radius:20px;

            border:2px solid #F3A9C5;

        }

        """)



        layout = QVBoxLayout()



        image = QLabel()



        image_path = figure[11]



        if image_path and isinstance(image_path, str):


            pixmap = QPixmap(
                image_path
            )


            if not pixmap.isNull():

                image.setPixmap(

                    pixmap.scaled(

                        170,

                        170,

                        Qt.KeepAspectRatio,

                        Qt.SmoothTransformation

                    )

                )

            else:

                image.setText(
                    "Фото не найдено"
                )


        else:

            image.setText(
                "Нет фото"
            )



        image.setAlignment(
            Qt.AlignCenter
        )



        name = QLabel(
            str(figure[2])
        )


        name.setStyleSheet("""

        color:#D84B8A;

        font-size:18px;

        font-weight:bold;

        """)



        rarity = QLabel(

            "Редкость: "

            + str(figure[6])

        )



        rarity.setStyleSheet("""

        color:#B52A70;

        font-size:14px;

        """)



        layout.addWidget(
            image
        )


        layout.addWidget(
            name
        )


        layout.addWidget(
            rarity
        )


        self.setLayout(
            layout
        )