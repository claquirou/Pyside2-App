from fbs_runtime.application_context.PySide2 import ApplicationContext

import package.main_window

import sys

if __name__ == '__main__':
    appctxt = ApplicationContext()       # 1. Instantiate ApplicationContext
    window = package.main_window.MainWindow(appctxt)
    window.setWindowTitle("PyCalculator")
    window.setFixedSize(330, 406)
    window.show()
    exit_code = appctxt.app.exec_()      # 2. Invoke appctxt.app.exec_()
    sys.exit(exit_code)