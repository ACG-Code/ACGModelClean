from PyQt5 import QtCore, QtGui, QtWidgets
from base_settings import  APP_NAME, APP_VERSION


class Ui_about_window(object):
    def setupUi(self, about_window):
        about_window.setObjectName("about_window")
        about_window.resize(400, 300)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ACG.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        about_window.setWindowIcon(icon)
        self.gridLayoutWidget = QtWidgets.QWidget(about_window)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 10, 391, 281))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.le_about = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.le_about.setFont(font)
        self.le_about.setAlignment(QtCore.Qt.AlignCenter)
        self.le_about.setObjectName("le_about")
        self.gridLayout.addWidget(self.le_about, 0, 1, 1, 1)

        self.retranslateUi(about_window)
        QtCore.QMetaObject.connectSlotsByName(about_window)

    def retranslateUi(self, about_window):
        _translate = QtCore.QCoreApplication.translate
        about_window.setWindowTitle(_translate("about_window", "ACG Model Cleanup - About"))
        self.label.setText(_translate("about_window", "<html><head/><body><p><img src=\":/acg_logo.jpg\"/></p></body></html>"))
        self.le_about.setText(_translate("about_window", "TextLabel"))
import resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    about_window = QtWidgets.QDialog()
    ui = Ui_about_window()
    ui.setupUi(about_window)
    about_window.show()
    sys.exit(app.exec_())
