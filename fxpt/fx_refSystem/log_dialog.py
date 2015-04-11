from PySide import QtGui

from fxpt.fx_prefsaver import PrefSaver, Serializers
from fxpt.fx_refSystem.com import getMayaQMainWindow
from fxpt.fx_refSystem.log_dialog_ui import Ui_Dialog

OPT_VAR_NAME_LOG_DLG = 'fx_refSystem_logDlg_prefs'


class LogDialog(QtGui.QDialog):

    def __init__(self):
        super(LogDialog, self).__init__(parent=getMayaQMainWindow())
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui_initSettings()
        self.ui_loadSettings()

    # noinspection PyAttributeOutsideInit
    def ui_initSettings(self):
        self.prefSaver = PrefSaver.PrefSaver(Serializers.SerializerOptVar(OPT_VAR_NAME_LOG_DLG))
        self.prefSaver.addControl(self, PrefSaver.UIType.PYSIDEWindow, (200, 200, 800, 500))

    def ui_loadSettings(self):
        self.prefSaver.loadPrefs()

    def ui_saveSettings(self):
        self.prefSaver.savePrefs()

    def showLog(self, strings):
        if strings:
            self.ui.uiTXT_log.clear()
            for s in strings:
                self.ui.uiTXT_log.appendPlainText(s)
            self.exec_()

    def onDialogFinished(self):
        self.ui_saveSettings()
