from PyQt6 import QtWidgets

class CustomListItemWidget(QtWidgets.QWidget):
    def __init__(self, id, title, content):
        self.id = id
        self.title = title
        self.content = content
        super().__init__()
        self.setAutoFillBackground(True) 
        
        closeButton = QtWidgets.QPushButton('X')
        closeButton.setFixedSize(20, 20)
        # closeButton.clicked.connect(self.onCloseClicked)

        titleLabel = QtWidgets.QLabel(title)
        contentLabel = QtWidgets.QLabel(' '.join(content.split()[:5]) + '...') #so that the content show in the layout will be 5 words + "..."

        titleFont = titleLabel.font()
        titleFont.setPointSize(titleFont.pointSize() + 4)
        titleFont.setBold(True)
        titleLabel.setFont(titleFont) #setting for the font

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(titleLabel)
        layout.addWidget(contentLabel)
        self.setLayout(layout)
    
    def update(self):
        self.layout().itemAt(0).widget().setText(self.title)
        self.layout().itemAt(1).widget().setText(' '.join(self.content.split()[:5]) + '...')
        self.layout().itemAt(2).widget().setText(self.updated_at)