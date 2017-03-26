from PyQt5 import QtGui, QtCore, QtWidgets
import sys

import mainwindow
import statebrowserwindow
import taskwindow

import os

class PlotGenerationEngine(QtWidgets.QMainWindow, mainwindow.Ui_MainWindow):
    def __init__(self, parent=None):
        super(PlotGenerationEngine, self).__init__(parent)
        self.setupUi(self)

        self.stateBrowserWindow = None
        self.taskWindow = None
        task = {'Task': {'Name': "Task A", 'Parameters': {"Param0": "A", "Param1": "B"}, "Preconditions": {"Precondition0": "P0", "Precondition1": "P1"} }}
        self.actionOpen.triggered.connect(self.browseFolder)
        self.actionState_Browser.triggered.connect(self.showStateBrowser)
        self.actionPlanner.triggered.connect(self.hideStateBrowser)
        self.pushButton_2.clicked.connect(self.showStateBrowser)
        self.pushButton_3.clicked.connect(self.showStateBrowser)
        self.pushButton.clicked.connect( lambda: self.showTaskWindow(task) )

    #                "parameters":
    #                    {
    #                    "0": "parameter0",
    #                    "1": "parameter1",
    #                    "2": "parameter2"
    #                    },
    #                 "preconditions":
    #                    {
    #                    "0": {"message": "message0", "isMet": "false"},
    #                    "1": {"message": "message1", "isMet": "true"}
    #                    }
    #                }

    def browseFolder(self):
        #self.listWidget.clear()
        file_name = str(QtWidgets.QFileDialog.getOpenFileName(self)[0])

        currentp = QtCore.QDir.current()
        relativeName = currentp.relativeFilePath(file_name)
        self.setWindowTitle(relativeName)

    def showStateBrowser(self):
        if self.stateBrowserWindow is None:
            self.stateBrowserWindow = statebrowserwindow.StateBrowserWindow(self)
        self.stateBrowserWindow.show()

    def hideStateBrowser(self):
        if self.stateBrowserWindow is not None:
            self.stateBrowserWindow.hide()

    def showTaskWindow(self, task):
        if self.taskWindow is None:
            self.taskWindow = taskwindow.TaskWindow(self)
        self.taskWindow.task = task
        self.taskWindow.show()

def main():
    app = QtWidgets.QApplication(sys.argv)
    form = PlotGenerationEngine()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()
