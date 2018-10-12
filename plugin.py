from Plugins.Plugin import PluginDescriptor
from Screens.Screen import Screen
from Components.Label import Label
from Components.MenuList import MenuList
from Components.ActionMap import ActionMap
from enigma import getDesktop
from Tools.Directories import fileExists

import api as API
import log

class MainViewEnigma2(Screen):
    screenWidth = getDesktop(0).size().width()-10
    screenHeight = getDesktop(0).size().height()-10
    skin = """<screen position="center,center" size=""" + str(screenWidth) + """,""" + str(screenHeight) + """ title="NOStraTV App" >
            <widget name="myLabel" position="center,10" size="720,50" font="Regular;20"/>
            <widget name="myMenu" position="center,60" size="720,454" scrollbarMode="showOnDemand" />
            </screen>"""

    def __init__(self, session, args = None):
        self.session = session

        # events = API.GetEventsFromSource('nflfullhd')['events']
        # list = []
        # for event in events:
        #     list.append( ( str(event['title']), str(event['id']) ) )

        Screen.__init__(self, session)

        actions = {
            "cancel": self.close # add the RC Command "cancel" to close your Screen
        }
        
        self["myLabel"] = Label("List") 

        # self['myMenu'] = MenuList(list)
        # actions['ok'] = self.go
        
        self["myActionMap"] = ActionMap(["SetupActions"], actions, -1)

    def go(self):
        returnValue = self["myMenu"].l.getCurrentSelection()[1]
        log.d('Plugin | List Selected: {0}'.format( str( returnValue ) ) )

def main(session, **kwargs):
    session.open(MainViewEnigma2)

def Plugins(**kwargs):
    return PluginDescriptor(
        name="NOStraTV App",
        description="Play on-demand contents: sports (NFL)",
        where = PluginDescriptor.WHERE_PLUGINMENU,
        icon="./icon.png",
        fnc=main)
