__copyright__ = """
    DaDuPo - An online calibration and measurement tool using XCP protocol

    (C) 2021 by Jun Yang <fever_sky@qq.com>

    All Rights Reserved

    This file is part of DaDuPo.

    DaDuPo is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

from PySide2 import QtWidgets
import pyqtgraph as pg

from DaDuPo.MainWindow import MainWindow

pg.setConfigOption('background', 'w')
pg.setConfigOption('foreground', 'b')

QSS = """
QMdiSubWindow:title{
    background: lightgray;
}
"""

if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow('.')
    # mainWin.showMaximized()
    mainWin.show()
    sys.exit(app.exec_())
