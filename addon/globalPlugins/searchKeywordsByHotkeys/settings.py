# -*- coding: utf-8 -*-

# Search Keywords by Hotkeys add-on for NVDA
# Copyright (C) 2025 NVDA User
# This file is covered by the GNU General Public License.

import wx
import gui
import addonHandler
import config
from gui.settingsDialogs import SettingsPanel

#addonHandler.initTranslation()

# Constants
MAX_KEYWORDS = 10
ADDON_CONFIG_SECTION = "searchKeywordsByHotkeys"

class SearchKeywordsSettingsPanel(SettingsPanel):
    """Settings panel for Search Keywords by Hotkeys add-on."""
    
    # Translators: Title of the settings panel
    title = _("Search Keywords by Hotkeys")
    
    def makeSettings(self, settingsSizer):
        """Create the settings controls."""
        # Create a helper sizer
        helper = gui.guiHelper.BoxSizerHelper(self, sizer=settingsSizer)
        
        # Create a list to store the text controls
        self.keywordEdits = []
        
        # Create text controls for each keyword
        for i in range(1, MAX_KEYWORDS + 1):
            # Translators: Label for keyword text field
            label = _("Keyword {index}:").format(index=i)
            edit = helper.addLabeledControl(label, wx.TextCtrl)
            # Set the current value
            edit.SetValue(config.conf[ADDON_CONFIG_SECTION][f"keyword{i}"])
            # Add to the list
            self.keywordEdits.append(edit)
        
        # Add a reset button
        # Translators: Label for reset button
        resetButton = helper.addItem(wx.Button(self, label=_("Reset")))
        resetButton.Bind(wx.EVT_BUTTON, self.onReset)
    
    def onReset(self, evt):
        """Reset all keywords to empty."""
        for edit in self.keywordEdits:
            edit.SetValue("")
    
    def onSave(self):
        """Save the settings."""
        # Save each keyword
        for i, edit in enumerate(self.keywordEdits, 1):
            config.conf[ADDON_CONFIG_SECTION][f"keyword{i}"] = edit.GetValue()
