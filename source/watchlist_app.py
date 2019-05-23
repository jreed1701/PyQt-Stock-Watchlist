from source.watchlist_manager import WatchlistManager
from source.watchlist_app_table_widget import WatchlistAppTableWidget

from PyQt5.QtWidgets import QWidget, QVBoxLayout

from win32gui import SetWindowPos
import win32con

class WatchlistApp(QWidget):

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
        
        self.addWidgetItems()
        
        SetWindowPos(self.winId(),
            win32con.HWND_TOPMOST, # = always on top. only reliable way to bring it to the front on windows
            0, 0, 0, 0,
            win32con.SWP_NOMOVE | win32con.SWP_NOSIZE | win32con.SWP_SHOWWINDOW)
        SetWindowPos(self.winId(),
            win32con.HWND_NOTOPMOST, # disable the always on top, but leave window at its top position
            0, 0, 0, 0,
            win32con.SWP_NOMOVE | win32con.SWP_NOSIZE | win32con.SWP_SHOWWINDOW)
    
        self.raise_()
        
        self.show()
        
        self.activateWindow()
        
    def addWidgetItems(self):
        
        self._layout = QVBoxLayout()
        
        self._table_widget = WatchlistAppTableWidget(self)
        
        self._layout.addWidget(self._table_widget)
        
        self.setLayout(self._layout)

