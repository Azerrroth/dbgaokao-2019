# -*- coding: utf-8 -*-

"""
Module implementing Form.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from Ui_cover import Ui_Form
from Ui_ChildrenForm2 import Ui_ChildrenForm

from Ui_ChildrenForm3 import Ui_ChildrenFrom3

class Form(QWidget, Ui_Form):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(Form, self).__init__(parent)
        self.setupUi(self)
    
    @pyqtSlot()
    def on_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
  
        self.child=ChildrenForm()
        self.child.show()
    
        
class ChildrenForm(QWidget, Ui_ChildrenForm):
    def __init__(self):
        super(ChildrenForm, self).__init__()
        self.setupUi(self)
    def on_pushButton_clicked(self):
        
        self.chil=Children()
        self.chil.show()
        
class Children(QWidget, Ui_ChildrenFrom3):
     def __init__(self):
        super(Children, self).__init__()
        self.setupUi(self)
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Form()
    ui.show()
    sys.exit(app.exec_())
