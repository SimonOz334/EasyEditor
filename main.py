from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance
import os
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFileDialog, QListWidget, QButtonGroup, QGroupBox, QVBoxLayout, QHBoxLayout, QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QMessageBox, QRadioButton
from random import shuffle
from PyQt5.QtGui import QIcon, QPixmap

#['.jpg', '.png', '.gif', '.jpeg', '.bmp']
workdir = ''

def chooseWorkDir():
    global workdir
    workdir = QFileDialog.getExistingDirectory()

def filter(files, extension):
    result = list()
    for name in files:
        for exten in extension:
            if name.endswith(exten):
                result.append(name)
    return result

def showFilenamesList():

    chooseWorkDir()
    extension = ['.jpg', '.png', '.gif', '.jpeg', '.bmp']
    files = os.listdir(workdir)
    res = filter(files, extension)
    write1.clear()
    write1.addItems(res)

class ImageProcessor():
    def __init__(self):
        self.image = None
        self.filename = None
        self.save_dir = 'папка/'

    def loadImage(self, filename):
        self.filename = filename
        image_path = os.path.join(workdir, filename)
        self.image = Image.open(image_path)

    def showImage(self, path):
        hint_label.hide()
        pixmapimage = QPixmap(path)
        w, h = hint_label.width(), hint_label.height()
        pixmapimage = pixmapimage.scaled(w, h, Qt.KeepAspectRatio)
        hint_label.setPixmap(pixmapimage)
        hint_label.show()

    def do_bw(self):
        if write1.selectedItems():
            self.image = self.image.convert("L")
            self.saveImage()
            image_path = os.path.join(workdir, self.save_dir, self.filename)
            self.showImage(image_path)
        else:
            error = QMessageBox()
            error.setWindowTitle('Ошибка!')
            error.setText('Вы не выбрали картинку!')
            error.setIcon(QMessageBox.Critical)
            error.exec_()   
        
    def mirrow(self):
        if write1.selectedItems():
            self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
            self.saveImage()
            image_path = os.path.join(workdir, self.save_dir, self.filename)
            self.showImage(image_path)
        else:
            error = QMessageBox()
            error.setWindowTitle('Ошибка!')
            error.setText('Вы не выбрали картинку!')
            error.setIcon(QMessageBox.Critical)
            error.exec_()   

    def contr(self):
        if write1.selectedItems():
            self.image = ImageEnhance.Contrast(self.image)
            self.image = self.image.enhance(1.5)
            self.saveImage()
            image_path = os.path.join(workdir, self.save_dir, self.filename)
            self.showImage(image_path)
        else:
            error = QMessageBox()
            error.setWindowTitle('Ошибка!')
            error.setText('Вы не выбрали картинку!')
            error.setIcon(QMessageBox.Critical)
            error.exec_()   

    def right(self):
        if write1.selectedItems():
            self.image = self.image.transpose(Image.ROTATE_90)
            self.saveImage()
            image_path = os.path.join(workdir, self.save_dir, self.filename)
            self.showImage(image_path) 
        else:
            error = QMessageBox()
            error.setWindowTitle('Ошибка!')
            error.setText('Вы не выбрали картинку!')
            error.setIcon(QMessageBox.Critical)
            error.exec_() 

    def left(self):
        if write1.selectedItems():
            self.image = self.image.transpose(Image.ROTATE_270)
            self.saveImage()
            image_path = os.path.join(workdir, self.save_dir, self.filename)
            self.showImage(image_path)     
        else:
            error = QMessageBox()
            error.setWindowTitle('Ошибка!')
            error.setText('Вы не выбрали картинку!')
            error.setIcon(QMessageBox.Critical)
            error.exec_() 

    def CONTOUR(self):
        if write1.selectedItems():
            self.image = self.image.filter(ImageFilter.CONTOUR)
            self.saveImage()
            image_path = os.path.join(workdir, self.save_dir, self.filename)
            self.showImage(image_path)     
        else:
            error = QMessageBox()
            error.setWindowTitle('Ошибка!')
            error.setText('Вы не выбрали картинку!')
            error.setIcon(QMessageBox.Critical)
            error.exec_()

    def DETALL(self):
        if write1.selectedItems():
            self.image = self.image.filter(ImageFilter.DETAIL)
            self.saveImage()
            image_path = os.path.join(workdir, self.save_dir, self.filename)
            self.showImage(image_path)     
        else:
            error = QMessageBox()
            error.setWindowTitle('Ошибка!')
            error.setText('Вы не выбрали картинку!')
            error.setIcon(QMessageBox.Critical)
            error.exec_()

    def EDGE_ENHANCE(self):
        if write1.selectedItems():
            self.image = self.image.filter(ImageFilter.EDGE_ENHANCE)
            self.saveImage()
            image_path = os.path.join(workdir, self.save_dir, self.filename)
            self.showImage(image_path)     
        else:
            error = QMessageBox()
            error.setWindowTitle('Ошибка!')
            error.setText('Вы не выбрали картинку!')
            error.setIcon(QMessageBox.Critical)
            error.exec_()

    def EMBOSS(self):
        if write1.selectedItems():
            self.image = self.image.filter(ImageFilter.EMBOSS)
            self.saveImage()
            image_path = os.path.join(workdir, self.save_dir, self.filename)
            self.showImage(image_path)     
        else:
            error = QMessageBox()
            error.setWindowTitle('Ошибка!')
            error.setText('Вы не выбрали картинку!')
            error.setIcon(QMessageBox.Critical)
            error.exec_()

    def FIND_EDGES(self):
        if write1.selectedItems():
            self.image = self.image.filter(ImageFilter.FIND_EDGES)
            self.saveImage()
            image_path = os.path.join(workdir, self.save_dir, self.filename)
            self.showImage(image_path)     
        else:
            error = QMessageBox()
            error.setWindowTitle('Ошибка!')
            error.setText('Вы не выбрали картинку!')
            error.setIcon(QMessageBox.Critical)
            error.exec_()

    def SMOOTH(self):
        if write1.selectedItems():
            self.image = self.image.filter(ImageFilter.SMOOTH)
            self.saveImage()
            image_path = os.path.join(workdir, self.save_dir, self.filename)
            self.showImage(image_path)     
        else:
            error = QMessageBox()
            error.setWindowTitle('Ошибка!')
            error.setText('Вы не выбрали картинку!')
            error.setIcon(QMessageBox.Critical)
            error.exec_()

    def SMOOTH_MORE(self):
        if write1.selectedItems():
            self.image = self.image.filter(ImageFilter.SMOOTH_MORE)
            self.saveImage()
            image_path = os.path.join(workdir, self.save_dir, self.filename)
            self.showImage(image_path)     
        else:
            error = QMessageBox()
            error.setWindowTitle('Ошибка!')
            error.setText('Вы не выбрали картинку!')
            error.setIcon(QMessageBox.Critical)
            error.exec_()
     
     

    def saveImage(self):
        ''' сохраняет копию файла в подпапке '''
        path = os.path.join(workdir, self.save_dir)
        if not(os.path.exists(path) or os.path.isdir(path)):
            os.mkdir(path)
        image_path = os.path.join(path, self.filename)
        self.image.save(image_path)

def showChosenImage():
    if write1.currentRow() >= 0:
        filename = write1.currentItem().text()
        workimage.loadImage(filename)
        image_path = os.path.join(workdir, workimage.filename)
        workimage.showImage(image_path)
        


app = QApplication([])

workimage = ImageProcessor()

main_win = QWidget()
main_win.setWindowIcon(QIcon("im.PNG"))
main_win.resize(1000,700)
main_win.setWindowTitle('Easy Editor')

########################################################

hint_label = QLabel('Картинка')

button1 = QPushButton('Папка')
button2 = QPushButton('Лево')
button3 = QPushButton('Право')
button4 = QPushButton('Зеркало')
button5 = QPushButton('Резкость')
button6 = QPushButton('Ч/б')
button7 = QPushButton('Рельеф')
button8 = QPushButton('Поиск по краю')
button9 = QPushButton('Сглаживание')
button10 = QPushButton('Плавность')
button11 = QPushButton('Улучшение деталей')
button12 = QPushButton('Контур')
button13 = QPushButton('Улучшение краёв')

write1 = QListWidget()

v_line1 = QVBoxLayout()
h_line2 = QHBoxLayout()
v_line3 = QVBoxLayout()
h_line4 = QHBoxLayout()
h_line5 = QHBoxLayout()

h_line2.addWidget(button2)
h_line2.addWidget(button3)
h_line2.addWidget(button4)
h_line2.addWidget(button5)
h_line2.addWidget(button6)
h_line2.addWidget(button7)
h_line5.addWidget(button8)
h_line5.addWidget(button9)
h_line5.addWidget(button10)
h_line5.addWidget(button11)
h_line5.addWidget(button12)
h_line5.addWidget(button13)

v_line1.addWidget(button1)
v_line1.addWidget(write1)
v_line3.addWidget(hint_label)
v_line3.addLayout(h_line2)
v_line3.addLayout(h_line5)
h_line4.addLayout(v_line1)
h_line4.addLayout(v_line3)

main_win.setLayout(h_line4)
write1.currentRowChanged.connect(showChosenImage)

button1.clicked.connect(showFilenamesList)
button2.clicked.connect(workimage.left)
button3.clicked.connect(workimage.right)
button4.clicked.connect(workimage.mirrow)
button5.clicked.connect(workimage.contr)
button6.clicked.connect(workimage.do_bw)
button7.clicked.connect(workimage.EMBOSS)
button8.clicked.connect(workimage.FIND_EDGES)
button9.clicked.connect(workimage.SMOOTH)
button10.clicked.connect(workimage.SMOOTH_MORE)
button11.clicked.connect(workimage.DETALL)
button12.clicked.connect(workimage.CONTOUR)
button13.clicked.connect(workimage.EDGE_ENHANCE)

main_win.show()
app.exec_()

