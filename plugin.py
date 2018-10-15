from Plugins.Plugin import PluginDescriptor
from Screens.Screen import Screen
from Components.Label import Label
from Components.MenuList import MenuList
from Components.ActionMap import ActionMap
from Screens.MessageBox import MessageBox
from enigma import getDesktop
from Tools.Directories import fileExists

import api as API
import log

# class MainViewEnigma2(Screen):
#     screenWidth = getDesktop(0).size().width()-10
#     screenHeight = getDesktop(0).size().height()-10
#     skin = """<screen position="center,center" size=""" + str(screenWidth) + """,""" + str(screenHeight) + """ title="NOStraTV App" >
#             <widget name="myLabel" position="center,10" size="720,50" font="Regular;20"/>
#             <widget name="myMenu" position="center,60" size="720,454" scrollbarMode="showOnDemand" />
#             </screen>"""

#     def __init__(self, session, args = None):
#         self.session = session

#         events = API.GetEventsFromSource('nflfullhd')['events']
#         list = []
#         for event in events:
#             list.append( ( str(event['title']), str(event['id']) ) )

#         Screen.__init__(self, session)

#         actions = {
#             'cancel': self.close # add the RC Command "cancel" to close your Screen
#         }
        
#         self["myLabel"] = Label("List") 

#         self['myMenu'] = MenuList(list)
#         actions['ok'] = self.go
        
#         self["myActionMap"] = ActionMap(["SetupActions"], actions, -1)

#     def go(self):
#         returnValue = self["myMenu"].l.getCurrentSelection()[1]
#         log.d('Plugin | List Selected: {0}'.format( str( returnValue ) ) )

class MainViewEnigma2(Screen):
    screenWidth = getDesktop(0).size().width()
    screenHeight = getDesktop(0).size().height()

    windowWidth = 1050
    windowHeight = 550

    skin = """
        <screen position="{0},{1}" size="{2},{3}" title="{4}" >
            <widget name="myLabel" position="10,60" size="200,200" font="Regular;20"/>
        </screen>""".format('100', '100', str(windowWidth), str(windowHeight), 'NOStraTV App')
    
    def __init__(self, session, args = 0):
        self.session = session
        Screen.__init__(self, session)
        self["myLabel"] = Label(_("please press OK\nWith: {0}\nHeight: {1}".format(str(MainViewEnigma2.screenWidth), str(MainViewEnigma2.screenHeight))))
        self["myActionMap"] = ActionMap(["SetupActions"],
        {
            "ok": self.myMsg,
            "cancel": self.cancel
        }, -1)

    def myMsg(self):
        log.d("\n[NOStraTV App] OK pressed \n")
        self.session.open(MessageBox,_("NOStraTV App!"), MessageBox.TYPE_INFO)

    def cancel(self):
        log.d("\n[NOStraTV App] cancel\n")
        self.close(False,self.session)

def main(session, **kwargs):
    log.i("**** NOStraTV App start ****")
    session.open(MainViewEnigma2)

def Plugins(**kwargs):
    return PluginDescriptor(
        name="NOStraTV App",
        description="Play on-demand contents: sports (NFL)",
        where = PluginDescriptor.WHERE_PLUGINMENU,
        icon="./icon.png",
        fnc=main)
