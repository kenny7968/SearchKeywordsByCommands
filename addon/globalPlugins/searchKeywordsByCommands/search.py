# -*- coding: utf-8 -*-

# Search Keywords by Commands add-on for NVDA
# Copyright (C) 2025 kenny7968
# This file is covered by the GNU General Public License.

import ui
import api
import textInfos
from browseMode import BrowseModeDocumentTreeInterceptor
import speech
import config
from logHandler import log
import addonHandler

addonHandler.initTranslation()

# Constants
MAX_KEYWORDS = 10
ADDON_CONFIG_SECTION = "searchKeywordsByCommands"

def isBrowseModeActive():
    """Check if browse mode is active."""
    focus = api.getFocusObject()
    if not focus:
        return False
    try:
        return isinstance(focus.treeInterceptor, BrowseModeDocumentTreeInterceptor) and focus.treeInterceptor.isReady
    except:
        return False

def getKeyword(index):
    """Get the keyword at the specified index."""
    if 1 <= index <= MAX_KEYWORDS:
        return config.conf[ADDON_CONFIG_SECTION][f"keyword{index}"]
    return ""

def searchKeyword(index):
    """Search for the keyword at the specified index."""
    if not isBrowseModeActive():
        # Only work in browse mode
        ui.message(_("This command is only available in browse mode."))
        return
    
    keyword = getKeyword(index)
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
            info.collapse(end=True)  # Move to end of matched string
            treeInterceptor.selection = info
            
            # Create a copy to get the end of the line
            lineEnd = info.copy()
            lineEnd.expand(textInfos.UNIT_LINE)
            lineEnd.collapse()  # Move to start of line
            lineEnd.setEndPoint(info.copy(), "startToEnd")  # Set start to current position
            lineEnd.expand(textInfos.UNIT_LINE)  # Expand to end of line
            lineEnd.setEndPoint(info, "startToStart")  # Set start to matched string end
            
            foundText = lineEnd.text
            speech.speakText(foundText)
            
        else:
            ui.message(_("Keyword {keyword} is not found").format(keyword=keyword))
    except Exception as e:
        log.error(f"Error in searchKeyword: {e}")
        ui.message(_("An error has occurred."))

def searchKeywordBackward(index):
    """Search for the keyword at the specified index in backward direction."""
    if not isBrowseModeActive():
        # Only work in browse mode
        ui.message(_("This command is only available in browse mode."))
        return
    
    keyword = getKeyword(index)
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
        res = info.find(keyword, reverse=True)
        if res:
            treeInterceptor.selection = info
            info.collapse(end=True)  # Move to end of matched string
            treeInterceptor.selection = info
            
            # Create a copy to get the end of the line
            lineEnd = info.copy()
            lineEnd.expand(textInfos.UNIT_LINE)
            lineEnd.collapse()  # Move to start of line
            lineEnd.setEndPoint(info.copy(), "startToEnd")  # Set start to current position
            lineEnd.expand(textInfos.UNIT_LINE)  # Expand to end of line
            lineEnd.setEndPoint(info, "startToStart")  # Set start to matched string end
            
            foundText = lineEnd.text
            speech.speakText(foundText)
            
        else:
            ui.message(_("Keyword {keyword} is not found").format(keyword=keyword))
    except Exception as e:
        log.error(f"Error in searchKeywordBackward: {e}")
        ui.message(_("An error has occurred."))

def announceKeyword(index):
    """Announce the keyword at the specified index."""
    keyword = getKeyword(index)
    if not keyword:
        ui.message(_("Keyword {index} is not set.").format(index=index))
    else:
        ui.message(_("Keyword {index}: {keyword}").format(index=index, keyword=keyword))
