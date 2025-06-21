# -*- coding: utf-8 -*-

# Search Keywords by Commands add-on for NVDA
# Copyright (C) 2025 kenny7968
# This file is covered by the GNU General Public License.

import addonHandler
import globalPluginHandler
import scriptHandler
from . import panel_manager
from . import search

addonHandler.initTranslation()

class GlobalPlugin(globalPluginHandler.GlobalPlugin):
    """Global plugin for Search Keywords by Commands add-on."""
    
    def __init__(self):
        super(GlobalPlugin, self).__init__()
        # Initialize settings
        panel_manager.initSettings()
        # Add settings panel to NVDA settings dialog
        panel_manager.addSettingsPanel()
    
    def terminate(self):
        """Clean up when the add-on is disabled."""
        # Remove settings panel from NVDA settings dialog
        panel_manager.removeSettingsPanel()
        super(GlobalPlugin, self).terminate()
    
    # Script functions for searching keywords
    @scriptHandler.script(
        description=_("Search for keyword 1"),
        gesture="kb:NVDA+control+1"
    )
    def script_searchKeyword1(self, gesture):
        search.searchKeyword(1)
    
    @scriptHandler.script(
        description=_("Search for keyword 2"),
        gesture="kb:NVDA+control+2"
    )
    def script_searchKeyword2(self, gesture):
        search.searchKeyword(2)
    
    @scriptHandler.script(
        description=_("Search for keyword 3"),
        gesture="kb:NVDA+control+3"
    )
    def script_searchKeyword3(self, gesture):
        search.searchKeyword(3)
    
    @scriptHandler.script(
        description=_("Search for keyword 4"),
        gesture="kb:NVDA+control+4"
    )
    def script_searchKeyword4(self, gesture):
        search.searchKeyword(4)
    
    @scriptHandler.script(
        description=_("Search for keyword 5"),
        gesture="kb:NVDA+control+5"
    )
    def script_searchKeyword5(self, gesture):
        search.searchKeyword(5)
    
    @scriptHandler.script(
        description=_("Search for keyword 6"),
        gesture="kb:NVDA+control+6"
    )
    def script_searchKeyword6(self, gesture):
        search.searchKeyword(6)
    
    @scriptHandler.script(
        description=_("Search for keyword 7"),
        gesture="kb:NVDA+control+7"
    )
    def script_searchKeyword7(self, gesture):
        search.searchKeyword(7)
    
    @scriptHandler.script(
        description=_("Search for keyword 8"),
        gesture="kb:NVDA+control+8"
    )
    def script_searchKeyword8(self, gesture):
        search.searchKeyword(8)
    
    @scriptHandler.script(
        description=_("Search for keyword 9"),
        gesture="kb:NVDA+control+9"
    )
    def script_searchKeyword9(self, gesture):
        search.searchKeyword(9)
    
    @scriptHandler.script(
        description=_("Search for keyword 10"),
        gesture="kb:NVDA+control+0"
    )
    def script_searchKeyword10(self, gesture):
        search.searchKeyword(10)
    
    # Script functions for announcing keywords
    @scriptHandler.script(
        description=_("Announce keyword 1"),
        gesture="kb:NVDA+alt+1"
    )
    def script_announceKeyword1(self, gesture):
        search.announceKeyword(1)
    
    @scriptHandler.script(
        description=_("Announce keyword 2"),
        gesture="kb:NVDA+alt+2"
    )
    def script_announceKeyword2(self, gesture):
        search.announceKeyword(2)
    
    @scriptHandler.script(
        description=_("Announce keyword 3"),
        gesture="kb:NVDA+alt+3"
    )
    def script_announceKeyword3(self, gesture):
        search.announceKeyword(3)
    
    @scriptHandler.script(
        description=_("Announce keyword 4"),
        gesture="kb:NVDA+alt+4"
    )
    def script_announceKeyword4(self, gesture):
        search.announceKeyword(4)
    
    @scriptHandler.script(
        description=_("Announce keyword 5"),
        gesture="kb:NVDA+alt+5"
    )
    def script_announceKeyword5(self, gesture):
        search.announceKeyword(5)
    
    @scriptHandler.script(
        description=_("Announce keyword 6"),
        gesture="kb:NVDA+alt+6"
    )
    def script_announceKeyword6(self, gesture):
        search.announceKeyword(6)
    
    @scriptHandler.script(
        description=_("Announce keyword 7"),
        gesture="kb:NVDA+alt+7"
    )
    def script_announceKeyword7(self, gesture):
        search.announceKeyword(7)
    
    @scriptHandler.script(
        description=_("Announce keyword 8"),
        gesture="kb:NVDA+alt+8"
    )
    def script_announceKeyword8(self, gesture):
        search.announceKeyword(8)
    
    @scriptHandler.script(
        description=_("Announce keyword 9"),
        gesture="kb:NVDA+alt+9"
    )
    def script_announceKeyword9(self, gesture):
        search.announceKeyword(9)
    
    @scriptHandler.script(
        description=_("Announce keyword 10"),
        gesture="kb:NVDA+alt+0"
    )
    def script_announceKeyword10(self, gesture):
        search.announceKeyword(10)
