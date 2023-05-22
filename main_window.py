from PyQt5 import QtCore, QtGui, QtWidgets
from create_window import Ui_create_window
from update_window import Ui_update_window
from about_window import Ui_about_window
from utilities import retrieve_sections
from ModelCleanup import perform_clean
import resources_rc
from base_settings import APP_NAME
from utilities import get_config
from PyQt5.QtWidgets import QMessageBox

# Next line to prevent removal of resources_rc during optimization
var = resources_rc


class CreateDialog(QtWidgets.QDialog, Ui_create_window):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.setupUi(self)


class UpdateDialog(QtWidgets.QDialog, Ui_update_window):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self)
        self.setupUi(self)


class AboutDialog(QtWidgets.QDialog, Ui_about_window):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.setupUi(self)


class Ui_winMain(object):
    def setupUi(self, winMain):
        winMain.setObjectName("winMain")
        winMain.resize(800, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ACG.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        winMain.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(winMain)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 781, 541))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        self.groupBox.setObjectName("groupBox")
        self.gridLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(190, 20, 391, 80))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.cmb_config = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.cmb_config.setObjectName("cmb_config")
        self.gridLayout.addWidget(self.cmb_config, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.gridLayoutWidget_4 = QtWidgets.QWidget(self.groupBox)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(10, 109, 761, 61))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.le_user = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.le_user.setObjectName("le_user")
        self.gridLayout_4.addWidget(self.le_user, 1, 0, 1, 1)
        self.le_password = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.le_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.le_password.setObjectName("le_password")
        self.gridLayout_4.addWidget(self.le_password, 1, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_4.addWidget(self.label_3, 0, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem, 0, 1, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.groupBox_2)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(20, 40, 741, 101))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.le_file = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.le_file.setObjectName("le_file")
        self.gridLayout_2.addWidget(self.le_file, 0, 0, 1, 1)
        self.btn_browse = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.btn_browse.setObjectName("btn_browse")
        self.gridLayout_2.addWidget(self.btn_browse, 0, 1, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.groupBox_3)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(10, 50, 761, 78))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 0, 0, 1, 1)
        self.btn_clean = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_clean.setFont(font)
        self.btn_clean.setObjectName("btn_clean")
        self.gridLayout_3.addWidget(self.btn_clean, 0, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem2, 0, 2, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_3)
        winMain.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(winMain)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuSetup = QtWidgets.QMenu(self.menubar)
        self.menuSetup.setObjectName("menuSetup")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        winMain.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(winMain)
        self.statusbar.setObjectName("statusbar")
        winMain.setStatusBar(self.statusbar)
        self.actionCreate_Configuration = QtWidgets.QAction(winMain)
        self.actionCreate_Configuration.setObjectName("actionCreate_Configuration")
        self.actionEdit_Configuration = QtWidgets.QAction(winMain)
        self.actionEdit_Configuration.setObjectName("actionEdit_Configuration")
        self.actionAbout = QtWidgets.QAction(winMain)
        self.actionAbout.setObjectName("actionAbout")
        self.menuSetup.addAction(self.actionCreate_Configuration)
        self.menuSetup.addAction(self.actionEdit_Configuration)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuSetup.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.actionCreate_Configuration.triggered.connect(self.open_create)
        self.actionAbout.triggered.connect(self.open_about)
        self.actionEdit_Configuration.triggered.connect(self.open_update)
        self.retranslateUi(winMain)
        sections = retrieve_sections()
        self.cmb_config.addItems(sections)
        self.btn_browse.clicked.connect(self.browse_files)
        self.btn_clean.clicked.connect(self.clean_model)
        QtCore.QMetaObject.connectSlotsByName(winMain)

    def open_create(self) -> None:
        dlg = CreateDialog()
        dlg.exec_()
        self.cmb_config.clear()
        sections = retrieve_sections()
        self.cmb_config.addItems(sections)

    def open_about(self) -> None:
        dlg = AboutDialog()
        dlg.exec_()

    def open_update(self) -> None:
        dlg = UpdateDialog()
        dlg.exec_()
        self.cmb_config.clear()
        sections = retrieve_sections()
        self.cmb_config.addItems(sections)

    def clean_model(self) -> None:
        self.statusbar.showMessage("Cleaning...")
        section = get_config(instance=self.cmb_config.currentText())
        username = self.le_user.text()
        password = self.le_password.text()
        section['user'] = username
        section['password'] = password
        section['session_context'] = APP_NAME
        file = self.le_file.text()
        perform_clean(file=file, config=section, instance=self.cmb_config.currentText())
        msg = QMessageBox()
        msg.setWindowTitle("Success")
        msg.setText("Clean Complete, check log files")
        msg.setIcon(QMessageBox.Information)
        x = msg.exec_()
        self.statusbar.showMessage("Ready")
        self.cmb_config.setCurrentText('')
        self.le_user.setText('')
        self.le_password.setText('')
        self.le_file.setText('')

    def browse_files(self) -> None:
        filename, _ = QtWidgets.QFileDialog.getOpenFileName(caption="Choose File", directory="", filter="CSV Files (*.csv)")
        self.le_file.setText(filename)

    def retranslateUi(self, winMain):
        _translate = QtCore.QCoreApplication.translate
        winMain.setWindowTitle(_translate("winMain", "ACG Model Cleanup"))
        self.groupBox.setTitle(_translate("winMain", "Configuration"))
        self.label.setText(_translate("winMain", "Choose Configuration"))
        self.label_2.setText(_translate("winMain", "Username"))
        self.label_3.setText(_translate("winMain", "Password"))
        self.groupBox_2.setTitle(_translate("winMain", "File Selection"))
        self.btn_browse.setText(_translate("winMain", "Choose File"))
        self.groupBox_3.setTitle(_translate("winMain", "Execution"))
        self.btn_clean.setText(_translate("winMain", "Perform Clean"))
        self.menuSetup.setTitle(_translate("winMain", "Setup"))
        self.menuHelp.setTitle(_translate("winMain", "Help"))
        self.actionCreate_Configuration.setText(_translate("winMain", "Create Configuration"))
        self.actionEdit_Configuration.setText(_translate("winMain", "Edit Configuration"))
        self.actionAbout.setText(_translate("winMain", "About"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    winMain = QtWidgets.QMainWindow()
    ui = Ui_winMain()
    ui.setupUi(winMain)
    winMain.show()
    sys.exit(app.exec_())
