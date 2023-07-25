import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QCheckBox, QGridLayout, QGroupBox,
        QMenu, QPushButton, QRadioButton, QVBoxLayout, QHBoxLayout, QWidget, QLabel)

class Window(QWidget):
    #%%
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.l_imagen = QLabel("Imagen")
        self.l_imagen.setAlignment(Qt.AlignCenter)

        grid = QHBoxLayout()
        grid.addWidget(self.l_imagen, 8)
        grid.addWidget(self.createExampleGroup(), 2)
        self.setLayout(grid)

        self.setWindowTitle("PyQt5 Group Box")
        #self.resize(400, 300)
    #%%    
    def createExampleGroup(self):
        groupBox = QGroupBox("Imagen")

        i_boton = 

        return groupBox
    
    
        #%% Dialog de archivos , despliega la primera imagen
    def openImageFile(self):
        """Despliega la imegen del archivo elegido"""
        hdr_file, _ = QFileDialog.getOpenFileName(self, "Abrir ...", 
            os.getenv('HOME'), "HDR (*.hdr)")
        a_file = hdr_file.split('.')
        float_file = a_file[0] + '.float'
    
        img = envi.open(hdr_file, float_file)
        
        # este es ek arreglo que tiene los datos del archivo hiperespectral
        self.data_img = img[:,:,:]
    
        l, r, b = self.data_img.shape
    
        self.tipo = (l, r, 3)
    
        x = 0
        y = 0
    
        self.data = np.zeros(self.tipo, dtype=np.uint8)
    
        for largo in self.data_img:
            for ancho in largo:
                b1 = int(ancho[25] * 255)
                b2 = int(ancho[20] * 255)
                b3 = int(ancho[10] * 255)
                self.data[x][y] = [b1, b2, b3]
                y = y + 1
            x = x + 1
            y = 0
        
        image = QImage(self.data.data, self.data.shape[1], self.data.shape[0], QImage.Format_RGB888)
        
        self.original_label.setPixmap(QPixmap.fromImage(image).scaled(self.original_label.width(), 
                                                                      self.original_label.height(), 
                                                                      Qt.KeepAspectRatioByExpanding))
    
            

if __name__ == '__main__':
    app = QApplication(sys.argv)
    clock = Window()
    clock.show()
    sys.exit(app.exec_())
        