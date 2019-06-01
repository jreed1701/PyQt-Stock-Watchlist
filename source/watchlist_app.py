from PyQt5.QtWidgets import QMainWindow, QHBoxLayout, QAction, QLayout, QWidget
from PyQt5.QtGui import QIcon

from source.watchlist_manager import WatchlistManager
from source.watchlist_command_widget import WatchlistCommandWidget
from source.watchlist_table_widget import WatchlistTableWidget

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

        self.addWidgetItems()

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu(' &File')

        updateButton = QAction(QIcon('resources/load.png'), ' &Update', self)
        updateButton.setShortcut('Ctrl+U')
        updateButton.setStatusTip('Update Stock Information')
        updateButton.triggered.connect(self._manager.updateStockInfos)
        updateButton.triggered.connect(self._table_widget.updateTable)
        fileMenu.addAction(updateButton)

        exitButton = QAction(QIcon('exit24.png'), ' &Exit', self)
        exitButton.setShortcut('Ctrl+Q')
        exitButton.setStatusTip('Exit application')
        exitButton.triggered.connect(self.close)
        fileMenu.addAction(exitButton)

        
        self.show()
        
        
    def addWidgetItems(self):
              
        self._main_widget = QWidget(self)
               
        self._table_widget = WatchlistTableWidget(self, self._manager)
        
        self._cw = WatchlistCommandWidget(self, self._manager, self._table_widget)
        
        self._main_layout = QHBoxLayout(self._main_widget)
        self._main_layout.sizeConstraint = QLayout.SetDefaultConstraint
        self._main_layout.addWidget(self._cw)
        self._main_layout.addWidget(self._table_widget)
        
        self._main_widget.setLayout(self._main_layout)
        self.setCentralWidget(self._main_widget)

