from PyQt5 import QtWidgets
from CourseWorkQt import Ui_MainWindow  # импорт нашего сгенерированного файла
from PyQt5.QtCore import pyqtSignal, QObject
import sys
 
 
class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
       
app = QtWidgets.QApplication([])
application = mywindow()
application.show()
 
sys.exit(app.exec())
