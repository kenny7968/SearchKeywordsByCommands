# -*- coding: utf-8 -*-

# Search Keywords by Commands add-on for NVDA
# Copyright (C) 2025 kenny7968
# This file is covered by the GNU General Public License.

import os
import wx
import gui
import addonHandler
import globalPluginHandler
import ui
import api
import textInfos
from browseMode import BrowseModeDocumentTreeInterceptor
import braille
import speech
import scriptHandler
import config
from logHandler import log
from . import settings

#addonHandler.initTranslation()

# Constants
MAX_KEYWORDS = 10
ADDON_CONFIG_SECTION = "searchKeywordsByCommands"

class GlobalPlugin(globalPluginHandler.GlobalPlugin):
    """Global plugin for Search Keywords by Commands add-on."""
    
    def __init__(self):
        super(GlobalPlugin, self).__init__()
        # Initialize settings
        self.initSettings()
        # Add settings panel to NVDA settings dialog
        gui.settingsDialogs.NVDASettingsDialog.categoryClasses.append(settings.SearchKeywordsSettingsPanel)
    
    def initSettings(self):
        """Initialize settings for the add-on."""
        # Create config section if it doesn't exist
        if not config.conf.get(ADDON_CONFIG_SECTION):
            config.conf[ADDON_CONFIG_SECTION] = {}
        # Initialize keywords if they don't exist
        for i in range(1, MAX_KEYWORDS + 1):
            key = f"keyword{i}"
            if key not in config.conf[ADDON_CONFIG_SECTION]:
                config.conf[ADDON_CONFIG_SECTION][key] = ""
    
    def terminate(self):
        """Clean up when the add-on is disabled."""
        # Remove settings panel from NVDA settings dialog
        gui.settingsDialogs.NVDASettingsDialog.categoryClasses.remove(settings.SearchKeywordsSettingsPanel)
        super(GlobalPlugin, self).terminate()
    
    def getKeyword(self, index):
        """Get the keyword at the specified index."""
        if 1 <= index <= MAX_KEYWORDS:
            return config.conf[ADDON_CONFIG_SECTION][f"keyword{index}"]
        return ""
    
    def isBrowseModeActive(self):
        """Check if browse mode is active."""
        focus = api.getFocusObject()
        if not focus:
            return False
        try:
            return isinstance(focus.treeInterceptor, BrowseModeDocumentTreeInterceptor) and focus.treeInterceptor.isReady
        except:
            return False
    
    def searchKeyword(self, index):
        """Search for the keyword at the specified index."""
        if not self.isBrowseModeActive():
            # Only work in browse mode
            ui.message(_("This command is only available in browse mode."))
            return
        
        keyword = self.getKeyword(index)
        if not keyword:
            ui.message(_("Keyword {index} is not set.").format(index=index))
            return
        
        # Get the browse mode object
        focus = api.getFocusObject()
        if not focus:
            return
        
        treeInterceptor = focus.treeInterceptor
        try:
            info = treeInterceptor.makeTextInfo(textInfos.POSITION_CARET)
            res = info.find(keyword)
            if res:
                treeInterceptor.selection = info
                info.collapse()
                treeInterceptor.selection = info
                
                info.expand(textInfos.UNIT_LINE)
                foundText = info.text
                speech.speakText(foundText)
                
            else:
                ui.message(f"Keyword {keyword} is not found")
        except Exception as e:
            log.error(f"Error in searchKeyword: {e}")
            ui.message("An error has occurred.")

    def announceKeyword(self, index):
        """Announce the keyword at the specified index."""
        keyword = self.getKeyword(index)
        if not keyword:
            ui.message(_("Keyword {index} is not set.").format(index=index))
        else:
            ui.message(_("Keyword {index}: {keyword}").format(index=index, keyword=keyword))
    
    # Script functions for searching keywords
    @scriptHandler.script(
        description=_("Search for keyword 1"),
        gesture="kb:NVDA+control+1"
    )
    def script_searchKeyword1(self, gesture):
        self.searchKeyword(1)
    
    @scriptHandler.script(
        description=_("Search for keyword 2"),
        gesture="kb:NVDA+control+2"
    )
    def script_searchKeyword2(self, gesture):
        self.searchKeyword(2)
    
    @scriptHandler.script(
        description=_("Search for keyword 3"),
        gesture="kb:NVDA+control+3"
    )
    def script_searchKeyword3(self, gesture):
        self.searchKeyword(3)
    
    @scriptHandler.script(
        description=_("Search for keyword 4"),
        gesture="kb:NVDA+control+4"
    )
    def script_searchKeyword4(self, gesture):
        self.searchKeyword(4)
    
    @scriptHandler.script(
        description=_("Search for keyword 5"),
        gesture="kb:NVDA+control+5"
    )
    def script_searchKeyword5(self, gesture):
        self.searchKeyword(5)
    
    @scriptHandler.script(
        description=_("Search for keyword 6"),
        gesture="kb:NVDA+control+6"
    )
    def script_searchKeyword6(self, gesture):
        self.searchKeyword(6)
    
    @scriptHandler.script(
        description=_("Search for keyword 7"),
        gesture="kb:NVDA+control+7"
    )
    def script_searchKeyword7(self, gesture):
        self.searchKeyword(7)
    
    @scriptHandler.script(
        description=_("Search for keyword 8"),
        gesture="kb:NVDA+control+8"
    )
    def script_searchKeyword8(self, gesture):
        self.searchKeyword(8)
    
    @scriptHandler.script(
        description=_("Search for keyword 9"),
        gesture="kb:NVDA+control+9"
    )
    def script_searchKeyword9(self, gesture):
        self.searchKeyword(9)
    
    @scriptHandler.script(
        description=_("Search for keyword 10"),
        gesture="kb:NVDA+control+0"
    )
    def script_searchKeyword10(self, gesture):
        self.searchKeyword(10)
    
    # Script functions for announcing keywords
    @scriptHandler.script(
        description=_("Announce keyword 1"),
        gesture="kb:NVDA+control+shift+1"
    )
    def script_announceKeyword1(self, gesture):
        self.announceKeyword(1)
    
    @scriptHandler.script(
        description=_("Announce keyword 2"),
        gesture="kb:NVDA+control+shift+2"
    )
    def script_announceKeyword2(self, gesture):
        self.announceKeyword(2)
    
    @scriptHandler.script(
        description=_("Announce keyword 3"),
        gesture="kb:NVDA+control+shift+3"
    )
    def script_announceKeyword3(self, gesture):
        self.announceKeyword(3)
    
    @scriptHandler.script(
        description=_("Announce keyword 4"),
        gesture="kb:NVDA+control+shift+4"
    )
    def script_announceKeyword4(self, gesture):
        self.announceKeyword(4)
    
    @scriptHandler.script(
        description=_("Announce keyword 5"),
        gesture="kb:NVDA+control+shift+5"
    )
    def script_announceKeyword5(self, gesture):
        self.announceKeyword(5)
    
    @scriptHandler.script(
        description=_("Announce keyword 6"),
        gesture="kb:NVDA+control+shift+6"
    )
    def script_announceKeyword6(self, gesture):
        self.announceKeyword(6)
    
    @scriptHandler.script(
        description=_("Announce keyword 7"),
        gesture="kb:NVDA+control+shift+7"
    )
    def script_announceKeyword7(self, gesture):
        self.announceKeyword(7)
    
    @scriptHandler.script(
        description=_("Announce keyword 8"),
        gesture="kb:NVDA+control+shift+8"
    )
    def script_announceKeyword8(self, gesture):
        self.announceKeyword(8)
    
    @scriptHandler.script(
        description=_("Announce keyword 9"),
        gesture="kb:NVDA+control+shift+9"
    )
    def script_announceKeyword9(self, gesture):
        self.announceKeyword(9)
    
    @scriptHandler.script(
        description=_("Announce keyword 10"),
        gesture="kb:NVDA+control+shift+0"
    )
    def script_announceKeyword10(self, gesture):
        self.announceKeyword(10)
