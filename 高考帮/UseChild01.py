# -*- coding: utf-8 -*-

"""
Module implementing Form.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from Ui_ChildrenForm2 import Ui_ChildrenForm

from Ui_ChildrenForm3 import Ui_ChildrenFrom3
from PyQt5 import*
    
        
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
        

