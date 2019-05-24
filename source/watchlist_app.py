from source.watchlist_manager import WatchlistManager
from source.watchlist_app_table_widget import WatchlistAppTableWidget

from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QAction, QLayout, QWidget
from PyQt5.QtGui import QIcon

from win32gui import SetWindowPos
import win32con

class WatchlistApp(QMainWindow):

    def __init__(self, ver):
        super().__init__()
        
        self.title = 'Watchlist App v%s' % ver
        
        self.left = 50
        self.top = 50
        self.width = 1280
        self.height = 960
        
        self._manager = WatchlistManager()
        
        self.initUI()
        
    def initUI(self):
        
        self.setWindowTitle(self.title)
        
        self.setGeometry(self.left, self.top, self.width, self.height)
                
        # = always on top. only reliable way to bring it to the front on windows
        SetWindowPos(self.winId(),
            win32con.HWND_TOPMOST,
            0, 0, 0, 0,
            win32con.SWP_NOMOVE | win32con.SWP_NOSIZE | win32con.SWP_SHOWWINDOW)
        # disable the always on top, but leave window at its top position
        SetWindowPos(self.winId(),
            win32con.HWND_NOTOPMOST, 
            0, 0, 0, 0,
            win32con.SWP_NOMOVE | win32con.SWP_NOSIZE | win32con.SWP_SHOWWINDOW)
    
        self.raise_()
        
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('File')
        
        exitButton = QAction(QIcon('exit24.png'), 'Exit', self)
        exitButton.setShortcut('Ctrl+Q')
        exitButton.setStatusTip('Exit application')
        exitButton.triggered.connect(self.close)
        fileMenu.addAction(exitButton)
        
        self.addWidgetItems()
        
        self.show()
        
        
    def addWidgetItems(self):
              
        self._main_widget = QWidget(self)
        
        self._table_widget = WatchlistAppTableWidget(self, self._manager)
        
        self._main_layout = QVBoxLayout(self._main_widget)
        self._main_layout.sizeConstraint = QLayout.SetDefaultConstraint
        self._main_layout.addWidget(self._table_widget)
        
        self._main_widget.setLayout(self._main_layout)
        self.setCentralWidget(self._main_widget)

