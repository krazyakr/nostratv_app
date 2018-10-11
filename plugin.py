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
    screenHeigth = getDesktop(0).size().heigth()-10
    skin = """<screen position="center,center" size=""" + screenWidth + """,""" + screenHeigth + """ title="NOStraTV App" >
            <widget name="myLabel" position="center,10" size="720,50" font="Regular;20"/>
            <widget name="myMenu" position="center,60" size="720,454" scrollbarMode="showOnDemand" />
            </screen>"""
    # if screenWidth and screenWidth == 1280:
    #     skin = """<screen position="center,center" size="730,514" title="NOStraTV App" >
    #         <widget name="myLabel" position="center,10" size="720,50" font="Regular;20"/>
    #         <widget name="myMenu" position="center,60" size="720,454" scrollbarMode="showOnDemand" />
    #         </screen>"""
    # elif screenWidth and screenWidth == 1920:
    #     skin = """<screen position="center,center" size="1095,771" title="NOStraTV App" >
    #         <widget name="myLabel" position="center,center" size="1085,761" font="Regular;20"/>
    #         </screen>"""
    # else:
    #     skin = """<screen position="center,center" size="630,370" title="NOStraTV App" >
    #         <widget name="myLabel" position="center,center" size="620,370" font="Regular;20"/>
    #         </screen>"""

    def __init__(self, session, args = None):
        self.session = session
        Screen.__init__(self, session)

        actions = {
            "cancel": self.close # add the RC Command "cancel" to close your Screen
        }

        self["myLabel"] = Label("WIP :)")
        # self['myMenu'].hide()

        events = API.GetEventsFromSource('nflfullhd')['events']
        list = []
        for event in events:
            list.append( ( event['title'], event['id'] ) )
        
        self["myLabel"] = Label("List") 

        self['myMenu'] = MenuList(list)
        actions['ok'] = self.go
        
        self["myActionMap"] = ActionMap(["SetupActions"], actions, -1)

    def go(self):
        returnValue = self["myMenu"].l.getCurrentSelection()[1]
        log.d('Plugin | List Selected: {0}'.format(returnValue) )

def main(session, **kwargs):
    session.open(MainViewEnigma2)

def Plugins(**kwargs):
    return PluginDescriptor(
        name="NOStraTV App",
        description="Play on-demand contents: sports (NFL)",
        where = PluginDescriptor.WHERE_PLUGINMENU,
        icon="./icon.png",
        fnc=main)
