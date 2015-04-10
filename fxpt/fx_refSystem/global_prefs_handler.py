from fxpt.fx_prefsaver import PrefSaver, Serializers

OPT_VAR_NAME_COMMON_PREFS = 'fx_refSystem_common_prefs'


class GlobalPrefsHandler(object):

    KEY_LAST_BROWSED_CREATE_REF = 'lastBrowsedCreateRef'

    def __init__(self):
        self.globalPrefs = None
        self.prefSaver = PrefSaver.PrefSaver(Serializers.SerializerOptVar(OPT_VAR_NAME_COMMON_PREFS))
        self.initPrefs()

    def initPrefs(self):
        self.prefSaver.addVariable('globalPrefs', self.getterGlobalPrefs, self.setterGlobalPrefs, dict())

    def savePrefs(self):
        self.prefSaver.savePrefs()

    def loadPrefs(self):
        self.prefSaver.loadPrefs()

    def setterGlobalPrefs(self, value):
        self.globalPrefs = value

    def getterGlobalPrefs(self):
        return self.globalPrefs

    def getValue(self, key):
        return self.globalPrefs.get(key, None)

    def setValue(self, key, value):
        self.globalPrefs[key] = value
