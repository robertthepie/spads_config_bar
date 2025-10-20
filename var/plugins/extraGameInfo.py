import perl
from datetime import datetime
spads=perl.ExtraGameInfo

pluginVersion = '0.1'
requiredSpadsVersion = '0.12.29'

def getVersion(pluginObject):
    return pluginVersion

def getRequiredSpadsVersion(pluginName):
    return requiredSpadsVersion


class ExtraGameInfo:

    def __init__(self,context):
        spads.slog("ExtraGameInfo plugin loaded (version %s)" % pluginVersion,3)

    def addStartScriptTags(self, additionalData):
        bosses = spads.getBosses()
        today = datetime.today()
        return {
            "game/modoption/bosses": ",".join(bosses),
            "game/modoptions/dateDay": today.day,
            "game/modoptions/dateMonth": today.month,
            "game/modoptions/dateYear": today.year
            }