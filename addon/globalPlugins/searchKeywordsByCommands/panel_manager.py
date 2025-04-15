# -*- coding: utf-8 -*-

# Search Keywords by Commands add-on for NVDA
# Copyright (C) 2025 kenny7968
# This file is covered by the GNU General Public License.

import gui
import config
import addonHandler
from . import settings

addonHandler.initTranslation()

# Constants
ADDON_CONFIG_SECTION = "searchKeywordsByCommands"
MAX_KEYWORDS = 10

def initSettings():
    """Initialize settings for the add-on."""
    # Create config section if it doesn't exist
    if not config.conf.get(ADDON_CONFIG_SECTION):
        config.conf[ADDON_CONFIG_SECTION] = {}
    # Initialize keywords if they don't exist
    for i in range(1, MAX_KEYWORDS + 1):
        key = f"keyword{i}"
        if key not in config.conf[ADDON_CONFIG_SECTION]:
            config.conf[ADDON_CONFIG_SECTION][key] = ""

def addSettingsPanel():
    """Add settings panel to NVDA settings dialog."""
    gui.settingsDialogs.NVDASettingsDialog.categoryClasses.append(settings.SearchKeywordsSettingsPanel)

def removeSettingsPanel():
    """Remove settings panel from NVDA settings dialog."""
    try:
        gui.settingsDialogs.NVDASettingsDialog.categoryClasses.remove(settings.SearchKeywordsSettingsPanel)
    except ValueError:
        pass  # Panel was not in the list
