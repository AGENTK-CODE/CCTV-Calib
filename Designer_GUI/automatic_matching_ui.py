# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AutomaticMatching.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Automatic_matching_Dialog(object):
    def setupUi(self, Automatic_matching_Dialog):
        Automatic_matching_Dialog.setObjectName("Automatic_matching_Dialog")
        Automatic_matching_Dialog.resize(869, 817)
        self.sat_im_graphicsView = QtWidgets.QGraphicsView(Automatic_matching_Dialog)
        self.sat_im_graphicsView.setGeometry(QtCore.QRect(10, 70, 321, 231))
        self.sat_im_graphicsView.setObjectName("sat_im_graphicsView")
        self.cropped_sat_im_graphicsView = QtWidgets.QGraphicsView(Automatic_matching_Dialog)
        self.cropped_sat_im_graphicsView.setGeometry(QtCore.QRect(410, 30, 201, 161))
        self.cropped_sat_im_graphicsView.setObjectName("cropped_sat_im_graphicsView")
        self.rot_left_pushButton = QtWidgets.QPushButton(Automatic_matching_Dialog)
        self.rot_left_pushButton.setGeometry(QtCore.QRect(80, 30, 71, 21))
        self.rot_left_pushButton.setObjectName("rot_left_pushButton")
        self.rot_right_pushButton = QtWidgets.QPushButton(Automatic_matching_Dialog)
        self.rot_right_pushButton.setGeometry(QtCore.QRect(160, 30, 71, 21))
        self.rot_right_pushButton.setObjectName("rot_right_pushButton")
        self.label = QtWidgets.QLabel(Automatic_matching_Dialog)
        self.label.setGeometry(QtCore.QRect(120, 10, 67, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Automatic_matching_Dialog)
        self.label_2.setGeometry(QtCore.QRect(110, 50, 111, 17))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Automatic_matching_Dialog)
        self.label_3.setGeometry(QtCore.QRect(420, 10, 171, 17))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Automatic_matching_Dialog)
        self.label_4.setGeometry(QtCore.QRect(630, 10, 151, 17))
        self.label_4.setObjectName("label_4")
        self.cctv_im_graphicsView = QtWidgets.QGraphicsView(Automatic_matching_Dialog)
        self.cctv_im_graphicsView.setGeometry(QtCore.QRect(10, 330, 321, 221))
        self.cctv_im_graphicsView.setObjectName("cctv_im_graphicsView")
        self.compute_matching_pushButton = QtWidgets.QPushButton(Automatic_matching_Dialog)
        self.compute_matching_pushButton.setGeometry(QtCore.QRect(500, 210, 251, 21))
        self.compute_matching_pushButton.setObjectName("compute_matching_pushButton")
        self.matching_im_graphicsView = QtWidgets.QGraphicsView(Automatic_matching_Dialog)
        self.matching_im_graphicsView.setGeometry(QtCore.QRect(410, 250, 441, 371))
        self.matching_im_graphicsView.setObjectName("matching_im_graphicsView")
        self.label_7 = QtWidgets.QLabel(Automatic_matching_Dialog)
        self.label_7.setGeometry(QtCore.QRect(10, 700, 131, 17))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Automatic_matching_Dialog)
        self.label_8.setGeometry(QtCore.QRect(452, 701, 138, 17))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Automatic_matching_Dialog)
        self.label_9.setGeometry(QtCore.QRect(110, 310, 91, 17))
        self.label_9.setObjectName("label_9")
        self.cropped_cctv_im_graphicsView = QtWidgets.QGraphicsView(Automatic_matching_Dialog)
        self.cropped_cctv_im_graphicsView.setGeometry(QtCore.QRect(620, 30, 201, 161))
        self.cropped_cctv_im_graphicsView.setObjectName("cropped_cctv_im_graphicsView")
        self.Disp_Lines_checkBox = QtWidgets.QCheckBox(Automatic_matching_Dialog)
        self.Disp_Lines_checkBox.setGeometry(QtCore.QRect(430, 640, 171, 23))
        self.Disp_Lines_checkBox.setObjectName("Disp_Lines_checkBox")
        self.label_20 = QtWidgets.QLabel(Automatic_matching_Dialog)
        self.label_20.setGeometry(QtCore.QRect(452, 724, 38, 17))
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(Automatic_matching_Dialog)
        self.label_21.setGeometry(QtCore.QRect(452, 747, 71, 17))
        self.label_21.setObjectName("label_21")
        self.result_nb_matches_label = QtWidgets.QLabel(Automatic_matching_Dialog)
        self.result_nb_matches_label.setGeometry(QtCore.QRect(650, 701, 91, 17))
        self.result_nb_matches_label.setText("")
        self.result_nb_matches_label.setObjectName("result_nb_matches_label")
        self.result_focal_label = QtWidgets.QLabel(Automatic_matching_Dialog)
        self.result_focal_label.setGeometry(QtCore.QRect(650, 724, 91, 17))
        self.result_focal_label.setText("")
        self.result_focal_label.setObjectName("result_focal_label")
        self.result_disto_label = QtWidgets.QLabel(Automatic_matching_Dialog)
        self.result_disto_label.setGeometry(QtCore.QRect(650, 747, 91, 17))
        self.result_disto_label.setText("")
        self.result_disto_label.setObjectName("result_disto_label")
        self.layoutWidget = QtWidgets.QWidget(Automatic_matching_Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 580, 153, 106))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 0, 0, 1, 1)
        self.color_align_checkBox = QtWidgets.QCheckBox(self.layoutWidget)
        self.color_align_checkBox.setObjectName("color_align_checkBox")
        self.gridLayout_3.addWidget(self.color_align_checkBox, 1, 0, 1, 1)
        self.sat_denoise_checkBox = QtWidgets.QCheckBox(self.layoutWidget)
        self.sat_denoise_checkBox.setObjectName("sat_denoise_checkBox")
        self.gridLayout_3.addWidget(self.sat_denoise_checkBox, 2, 0, 1, 1)
        self.cctv_denoise_checkBox = QtWidgets.QCheckBox(self.layoutWidget)
        self.cctv_denoise_checkBox.setObjectName("cctv_denoise_checkBox")
        self.gridLayout_3.addWidget(self.cctv_denoise_checkBox, 3, 0, 1, 1)
        self.layoutWidget1 = QtWidgets.QWidget(Automatic_matching_Dialog)
        self.layoutWidget1.setGeometry(QtCore.QRect(200, 580, 188, 207))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_13 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 0, 0, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 1, 0, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 2, 0, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_16.setObjectName("label_16")
        self.gridLayout.addWidget(self.label_16, 3, 0, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_17.setObjectName("label_17")
        self.gridLayout.addWidget(self.label_17, 4, 0, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_18.setObjectName("label_18")
        self.gridLayout.addWidget(self.label_18, 5, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 6, 1)
        self.sp_resize_w_lineEdit = QtWidgets.QLineEdit(self.layoutWidget1)
        self.sp_resize_w_lineEdit.setObjectName("sp_resize_w_lineEdit")
        self.gridLayout_2.addWidget(self.sp_resize_w_lineEdit, 0, 1, 1, 1)
        self.sp_resize_h_lineEdit = QtWidgets.QLineEdit(self.layoutWidget1)
        self.sp_resize_h_lineEdit.setObjectName("sp_resize_h_lineEdit")
        self.gridLayout_2.addWidget(self.sp_resize_h_lineEdit, 1, 1, 1, 1)
        self.sp_sinkhorn_it_lineEdit = QtWidgets.QLineEdit(self.layoutWidget1)
        self.sp_sinkhorn_it_lineEdit.setObjectName("sp_sinkhorn_it_lineEdit")
        self.gridLayout_2.addWidget(self.sp_sinkhorn_it_lineEdit, 2, 1, 1, 1)
        self.sp_nb_pts_lineEdit = QtWidgets.QLineEdit(self.layoutWidget1)
        self.sp_nb_pts_lineEdit.setObjectName("sp_nb_pts_lineEdit")
        self.gridLayout_2.addWidget(self.sp_nb_pts_lineEdit, 3, 1, 1, 1)
        self.sp_kp_thresh_lineEdit = QtWidgets.QLineEdit(self.layoutWidget1)
        self.sp_kp_thresh_lineEdit.setObjectName("sp_kp_thresh_lineEdit")
        self.gridLayout_2.addWidget(self.sp_kp_thresh_lineEdit, 4, 1, 1, 1)
        self.sp_matching_thresh_lineEdit = QtWidgets.QLineEdit(self.layoutWidget1)
        self.sp_matching_thresh_lineEdit.setObjectName("sp_matching_thresh_lineEdit")
        self.gridLayout_2.addWidget(self.sp_matching_thresh_lineEdit, 5, 1, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_2, 1, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_6.setObjectName("label_6")
        self.gridLayout_4.addWidget(self.label_6, 0, 0, 1, 1)
        self.layoutWidget2 = QtWidgets.QWidget(Automatic_matching_Dialog)
        self.layoutWidget2.setGeometry(QtCore.QRect(12, 721, 181, 89))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget2)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_10 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_10.setObjectName("label_10")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.ransac_thresh_lineEdit = QtWidgets.QLineEdit(self.layoutWidget2)
        self.ransac_thresh_lineEdit.setObjectName("ransac_thresh_lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.ransac_thresh_lineEdit)
        self.label_11 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_11.setObjectName("label_11")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.ransac_it_lineEdit = QtWidgets.QLineEdit(self.layoutWidget2)
        self.ransac_it_lineEdit.setObjectName("ransac_it_lineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.ransac_it_lineEdit)
        self.label_12 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_12.setObjectName("label_12")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.model_comboBox = QtWidgets.QComboBox(self.layoutWidget2)
        self.model_comboBox.setEditable(False)
        self.model_comboBox.setObjectName("model_comboBox")
        self.model_comboBox.addItem("")
        self.model_comboBox.addItem("")
        self.model_comboBox.addItem("")
        self.model_comboBox.addItem("")
        self.model_comboBox.addItem("")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.model_comboBox)
        self.validate_buttonBox = QtWidgets.QDialogButtonBox(Automatic_matching_Dialog)
        self.validate_buttonBox.setGeometry(QtCore.QRect(690, 740, 166, 25))
        self.validate_buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Apply)
        self.validate_buttonBox.setObjectName("validate_buttonBox")

        self.retranslateUi(Automatic_matching_Dialog)
        QtCore.QMetaObject.connectSlotsByName(Automatic_matching_Dialog)

    def retranslateUi(self, Automatic_matching_Dialog):
        _translate = QtCore.QCoreApplication.translate
        Automatic_matching_Dialog.setWindowTitle(_translate("Automatic_matching_Dialog", "Dialog"))
        self.rot_left_pushButton.setText(_translate("Automatic_matching_Dialog", "↶"))
        self.rot_right_pushButton.setText(_translate("Automatic_matching_Dialog", "↷"))
        self.label.setText(_translate("Automatic_matching_Dialog", "Rotation"))
        self.label_2.setText(_translate("Automatic_matching_Dialog", "Satellite image"))
        self.label_3.setText(_translate("Automatic_matching_Dialog", "Cropped satellite image"))
        self.label_4.setText(_translate("Automatic_matching_Dialog", "Cropped CCTV image"))
        self.compute_matching_pushButton.setText(_translate("Automatic_matching_Dialog", "⇩ Compute keypoints matching ⇩"))
        self.label_7.setText(_translate("Automatic_matching_Dialog", "<html><head/><body><p><span style=\" font-style:italic;\">RANSAC options</span></p></body></html>"))
        self.label_8.setText(_translate("Automatic_matching_Dialog", "Number of matches:"))
        self.label_9.setText(_translate("Automatic_matching_Dialog", " CCTV image"))
        self.Disp_Lines_checkBox.setText(_translate("Automatic_matching_Dialog", "Display matching lines"))
        self.label_20.setText(_translate("Automatic_matching_Dialog", "focal:"))
        self.label_21.setText(_translate("Automatic_matching_Dialog", "distortion:"))
        self.label_5.setText(_translate("Automatic_matching_Dialog", "<html><head/><body><p><span style=\" font-style:italic;\">Image preprocessing</span></p></body></html>"))
        self.color_align_checkBox.setText(_translate("Automatic_matching_Dialog", "Color alignment"))
        self.sat_denoise_checkBox.setText(_translate("Automatic_matching_Dialog", "Satellite denoising"))
        self.cctv_denoise_checkBox.setText(_translate("Automatic_matching_Dialog", "CCTV denoising"))
        self.label_13.setText(_translate("Automatic_matching_Dialog", "Resized_w:"))
        self.label_14.setText(_translate("Automatic_matching_Dialog", "Resized_h:"))
        self.label_15.setText(_translate("Automatic_matching_Dialog", "Sinkhorn it:"))
        self.label_16.setText(_translate("Automatic_matching_Dialog", "Max nb points:"))
        self.label_17.setText(_translate("Automatic_matching_Dialog", "Thresh kp:"))
        self.label_18.setText(_translate("Automatic_matching_Dialog", "Thresh matching:"))
        self.sp_resize_w_lineEdit.setText(_translate("Automatic_matching_Dialog", "640"))
        self.sp_resize_h_lineEdit.setText(_translate("Automatic_matching_Dialog", "480"))
        self.sp_sinkhorn_it_lineEdit.setText(_translate("Automatic_matching_Dialog", "20"))
        self.sp_nb_pts_lineEdit.setText(_translate("Automatic_matching_Dialog", "1024"))
        self.sp_kp_thresh_lineEdit.setText(_translate("Automatic_matching_Dialog", "0.005"))
        self.sp_matching_thresh_lineEdit.setText(_translate("Automatic_matching_Dialog", "0.2"))
        self.label_6.setText(_translate("Automatic_matching_Dialog", "<html><head/><body><p><span style=\" font-style:italic;\">SuperPoint options</span></p></body></html>"))
        self.label_10.setText(_translate("Automatic_matching_Dialog", "Repro thresh:"))
        self.ransac_thresh_lineEdit.setText(_translate("Automatic_matching_Dialog", "10"))
        self.label_11.setText(_translate("Automatic_matching_Dialog", "RANSAC it:"))
        self.ransac_it_lineEdit.setText(_translate("Automatic_matching_Dialog", "10000"))
        self.label_12.setText(_translate("Automatic_matching_Dialog", "Model:"))
        self.model_comboBox.setCurrentText(_translate("Automatic_matching_Dialog", "p5pfr"))
        self.model_comboBox.setItemText(0, _translate("Automatic_matching_Dialog", "p5pfr"))
        self.model_comboBox.setItemText(1, _translate("Automatic_matching_Dialog", "p4pf"))
        self.model_comboBox.setItemText(2, _translate("Automatic_matching_Dialog", "p4pfr"))
        self.model_comboBox.setItemText(3, _translate("Automatic_matching_Dialog", "homog"))
        self.model_comboBox.setItemText(4, _translate("Automatic_matching_Dialog", "radial homog"))
