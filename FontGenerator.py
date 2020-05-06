from PyQt5 import QtCore, QtGui, QtWidgets
from functools import partial
from PIL import Image
import sys
from PIL.ImageQt import ImageQt

from keras.layers import Lambda, Input, Dense, Conv2D, BatchNormalization, Reshape, \
                        MaxPool2D, GlobalAveragePooling2D, LeakyReLU, UpSampling2D, Flatten, Conv2DTranspose
from keras.models import Model
from keras.losses import mean_squared_error, binary_crossentropy, categorical_crossentropy
from keras.utils import plot_model
from keras import backend as K

from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.preprocessing.image import array_to_img
from keras.preprocessing.image import save_img
import keras
import numpy as np


sys._excepthook = sys.excepthook

def my_exception_hook(exctype, value, traceback):
    """Execption Hook allows errors to be printed out to a file"""

    exepath = sys.executable
    r = exepath.split("\\")[-1]
    exepath = exepath.replace(r, "")
    path = exepath + "Error.txt"
    errors = open(path, 'w+')
    handler = logging.StreamHandler(errors)
    #logger.removeHandler(logger.handlers[0])
    logger.addHandler(handler)
    logger.error("Uncaught exception", exc_info=(exctype, value, traceback))
    errors.write("\nSend This File And An Explanation Of The Error To yigit.atay@vanderbilt.edu")
    Ui_MainWindow.openErrorWindow(Ui_Dialog)



sys.excepthook = my_exception_hook

latent_params = {}
for i in range(100):
    latent_params['Param ' + str(i+1)] = 0.0

## TO CHANGE RANGES OF ALL PARAMETERS
upper_limit = 50.0
lower_limit = 0.0
latent_ranges = [(lower_limit,upper_limit) for x in latent_params]

## TO CHANGE THE RANGE OF A SINGLE PARAMETER
#latent_ranges[2] = (.20, .84)  # Change Single Param

# Load decoder weights
weights_path = 'allDataDecoder.h5'

class Ui_MainWindow(object):
    latent_param_labels = [x for x in latent_params.keys()]

    model = object()

    def setupVAE(self):

        ## VAE DECODER
        conv_shape = (None, 128, 128, 16)
        num_channels = 1

        latent_inputs = Input(shape=(100,), name='decoder_input')
        x = Dense(conv_shape[1] * conv_shape[2] * conv_shape[3], activation='relu')(latent_inputs)
        x = BatchNormalization()(x)
        x = Reshape((conv_shape[1], conv_shape[2], conv_shape[3]))(x)
        cx = Conv2DTranspose(filters=16, kernel_size=3, strides=2, padding='same', activation='relu')(x)
        cx = BatchNormalization()(cx)
        cx = Conv2DTranspose(filters=8, kernel_size=3, strides=2, padding='same', activation='relu')(cx)
        cx = BatchNormalization()(cx)
        outputs = Conv2DTranspose(filters=num_channels, kernel_size=3, activation='sigmoid', padding='same',
                                  name='decoder_output')(cx)

        self.model = Model(latent_inputs, outputs, name='decoder')
        self.model.compile(optimizer='adam',loss=keras.losses.mse)
        self.model.load_weights(weights_path)

    def runInf(self):
        latent_space = np.random.normal(0.0,1.0,100)
        latent_space = np.reshape(latent_space,[1,100])
        print(latent_space.shape)
        generation = self.model.predict(latent_space)
        print(generation.shape)
        generation = np.reshape(generation, [512,512])
        im = Image.fromarray(np.uint8(generation * 255), 'L')
        qim = ImageQt(im)
        pix = QtGui.QPixmap.fromImage(qim)
        pixmap = QtGui.QPixmap(pix)
        # pix = QtGui.QPixmap.fromImage(qim)
        self.graphicLabel.setPixmap(pixmap)
        self.graphicLabel.update()
        #self.runInf()
        print(generation * 255)

    def generateImage(self):
        latent_space = list(latent_params.values())
        latent_space = np.reshape(latent_space, [1, 100])
        generation = self.model.predict(latent_space)
        #print(generation.shape)
        generation = self.model.predict(latent_space)
        generation = np.reshape(generation, [512, 512])
        im = Image.fromarray(np.uint8(generation * 255), 'L')
        qim = ImageQt(im)
        pix = QtGui.QPixmap.fromImage(qim)
        pixmap = QtGui.QPixmap(pix)
        # pix = QtGui.QPixmap.fromImage(qim)
        self.graphicLabel.setPixmap(pixmap)
        self.graphicLabel.update()
        print(list(latent_params.values()))

    def valuechange(self, id, val):
        #print(id, val)
        slider = id[0]

        maxMin = latent_ranges[slider]
        range = maxMin[1] - maxMin[0]
        trueVal = (range * (val / 100)) + maxMin[0]
        latent_params[self.latent_param_labels[slider]] = trueVal
        exec('self.label_%d_b.setText(str(%.2f))' % (slider, trueVal))
        self.generateImage()
        #print(latent_params[self.latent_param_labels[slider]])


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_1)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.scrollArea = QtWidgets.QScrollArea(self.tab_1)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 355, 472))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")

        for i in range(len(latent_params)):

            exec('self.label_%d_a = QtWidgets.QLabel(self.tab_1,text=list(latent_params.keys())[%d])' % (i,i))

            exec('self.label_%d_a.setObjectName("label_%d_a")' % (i, i))
            exec('self.gridLayout_2.addWidget(self.label_%d_a, %d, 0, 1, 1)' % (i, i))
            exec('self.horizontalSlider_%d = QtWidgets.QSlider(self.tab_1)' % i)
            exec('self.horizontalSlider_%d.setOrientation(QtCore.Qt.Horizontal)' % i)
            exec('self.horizontalSlider_%d.setObjectName("horizontalSlider_%d")' % (i, i))
            exec('self.horizontalSlider_%d.setMinimum(0)' % i)
            exec('self.horizontalSlider_%d.setMaximum(100)' % i)
            exec('self.horizontalSlider_%d.setSingleStep(1)' %  i)
            exec('self.horizontalSlider_%d.setValue(0)' % i)
            exec('self.horizontalSlider_%d.valueChanged.connect(partial(self.valuechange,(%d,self.horizontalSlider_%d.value())))' % (i,i,i))
            exec('self.gridLayout_2.addWidget(self.horizontalSlider_%d, %d, 1, 1, 1)' % (i, i))
            exec('self.label_%d_b = QtWidgets.QLabel(self.tab_1,text=str(self.horizontalSlider_%d.value()))' % (i,i))
            exec('self.label_%d_b.setObjectName("label_%d_b")' % (i, i))
            exec('self.gridLayout_2.addWidget(self.label_%d_b, %d, 2, 1, 1)' % (i, i))
            exec('self.checkBox_%d = QtWidgets.QCheckBox(self.tab_1)' % i)
            exec('self.checkBox_%d.setObjectName("checkBox_%d")' % (i, i))
            exec('self.gridLayout_2.addWidget(self.checkBox_%d, %d, 3, 1, 1)' % (i, i))

        #QtWidgets.QCheckBox
        # self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        # self.label_2.setObjectName("label_2")
        # self.gridLayout_2.addWidget(self.label_2, 0, 2, 1, 1)
        # self.horizontalSlider = QtWidgets.QSlider(self.scrollAreaWidgetContents)
        # self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        # self.horizontalSlider.setObjectName("horizontalSlider")
        # self.gridLayout_2.addWidget(self.horizontalSlider, 0, 1, 1, 1)
        # self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        # self.label.setObjectName("label")
        # self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        # self.radioButton = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        # self.radioButton.setObjectName("radioButton")
        # self.gridLayout_2.addWidget(self.radioButton, 0, 3, 1, 1)
        self.gridLayout_7.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_3.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.horizontalSlider_5 = QtWidgets.QSlider(self.tab_2)
        self.horizontalSlider_5.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_5.setObjectName("horizontalSlider_5")
        self.gridLayout_5.addWidget(self.horizontalSlider_5, 0, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.tab_2)
        self.label_10.setObjectName("label_10")
        self.gridLayout_5.addWidget(self.label_10, 0, 2, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.tab_2)
        self.label_9.setObjectName("label_9")
        self.gridLayout_5.addWidget(self.label_9, 0, 0, 1, 1)
        self.radioButton_5 = QtWidgets.QRadioButton(self.tab_2)
        self.radioButton_5.setObjectName("radioButton_5")
        self.gridLayout_5.addWidget(self.radioButton_5, 0, 3, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_5, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.horizontalLayout_2.addWidget(self.tabWidget)

        '''self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName("graphicsView")
        '''
        self.graphicLabel = QtWidgets.QLabel(self.centralwidget)
        self.graphicLabel.setObjectName('graphicLabel')
        self.horizontalLayout_2.addWidget(self.graphicLabel)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.setupVAE()
        self.generateImage()
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Font Params"))
        # self.label_2.setText(_translate("MainWindow", "TextLabel"))
        # self.label.setText(_translate("MainWindow", "TextLabel"))
        # self.radioButton.setText(_translate("MainWindow", "RadioButton"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("MainWindow", "All"))
        # self.label_10.setText(_translate("MainWindow", "0"))
        # self.label_9.setText(_translate("MainWindow", "Cursed"))
        # self.radioButton_5.setText(_translate("MainWindow", "RadioButton"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Favorites"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('fusion')
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
