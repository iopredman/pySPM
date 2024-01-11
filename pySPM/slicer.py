# Form implementation generated from reading ui file 'C:\Users\ols\Dropbox\Python\pySPM\slicer.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets


class Ui_slicer:
    def setupUi(self, slicer):
        slicer.setObjectName("slicer")
        slicer.resize(802, 547)
        self.gridLayout = QtWidgets.QGridLayout(slicer)
        self.gridLayout.setObjectName("gridLayout")
        self.peakList = QtWidgets.QTableWidget(slicer)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.peakList.sizePolicy().hasHeightForWidth())
        self.peakList.setSizePolicy(sizePolicy)
        self.peakList.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.peakList.setObjectName("peakList")
        self.peakList.setColumnCount(3)
        self.peakList.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.peakList.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.peakList.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.peakList.setHorizontalHeaderItem(2, item)
        self.gridLayout.addWidget(self.peakList, 0, 0, 1, 1)
        self.mpl = MplWidget(slicer)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mpl.sizePolicy().hasHeightForWidth())
        self.mpl.setSizePolicy(sizePolicy)
        self.mpl.setMinimumSize(QtCore.QSize(500, 500))
        self.mpl.setObjectName("mpl")
        self.gridLayout.addWidget(self.mpl, 0, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.status = QtWidgets.QLabel(slicer)
        self.status.setObjectName("status")
        self.horizontalLayout.addWidget(self.status)
        self.correction = QtWidgets.QCheckBox(slicer)
        self.correction.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.correction.setObjectName("correction")
        self.horizontalLayout.addWidget(self.correction)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pb = QtWidgets.QProgressBar(slicer)
        self.pb.setEnabled(True)
        self.pb.setProperty("value", 0)
        self.pb.setInvertedAppearance(False)
        self.pb.setObjectName("pb")
        self.horizontalLayout_2.addWidget(self.pb)
        self.label_2 = QtWidgets.QLabel(slicer)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.prof1daxis = QtWidgets.QComboBox(slicer)
        self.prof1daxis.setObjectName("prof1daxis")
        self.prof1daxis.addItem("")
        self.prof1daxis.addItem("")
        self.prof1daxis.addItem("")
        self.horizontalLayout_2.addWidget(self.prof1daxis)
        self.label = QtWidgets.QLabel(slicer)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.cmap = QtWidgets.QComboBox(slicer)
        self.cmap.setObjectName("cmap")
        self.cmap.addItem("")
        self.cmap.addItem("")
        self.cmap.addItem("")
        self.cmap.addItem("")
        self.horizontalLayout_2.addWidget(self.cmap)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 1, 1, 1)

        self.retranslateUi(slicer)
        QtCore.QMetaObject.connectSlotsByName(slicer)

    def retranslateUi(self, slicer):
        _translate = QtCore.QCoreApplication.translate
        slicer.setWindowTitle(_translate("slicer", "Slicer"))
        item = self.peakList.horizontalHeaderItem(0)
        item.setText(_translate("slicer", "Name"))
        item = self.peakList.horizontalHeaderItem(1)
        item.setText(_translate("slicer", "center mass"))
        item = self.peakList.horizontalHeaderItem(2)
        item.setText(_translate("slicer", "Δ mass"))
        self.status.setText(_translate("slicer", "Loading..."))
        self.correction.setText(_translate("slicer", "Apply Correction"))
        self.label_2.setText(_translate("slicer", "1D plot on"))
        self.prof1daxis.setItemText(0, _translate("slicer", "X"))
        self.prof1daxis.setItemText(1, _translate("slicer", "Y"))
        self.prof1daxis.setItemText(2, _translate("slicer", "Z"))
        self.label.setText(_translate("slicer", "Colormap"))
        self.cmap.setItemText(0, _translate("slicer", "viridis"))
        self.cmap.setItemText(1, _translate("slicer", "gray"))
        self.cmap.setItemText(2, _translate("slicer", "hot"))
        self.cmap.setItemText(3, _translate("slicer", "jet"))


from mplwidget import MplWidget
