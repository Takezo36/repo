# -*- coding: utf-8 -*-

# Copyright (C) 2018 - Benjamin Hebgen <mail>
# This program is Free Software see LICENSE file for details

from .. import Constants

def addForceRefreshButton(contextMenu):
  contextMenu.append((FORCE_REFRESH_STRING, PLUGIN_ACTION+ACTION+"="+ACTION_FORCE_REFRESH+")"))
  return contextMenu

def addSideCallEntries(contextMenu, sideCalls):
  for sideCall in sideCalls:
    contextMenu.append((sideCall[Constants.NAME], PLUGIN_ACTION+ACTION+"="+ACTION_EXEC+"&"+ACTION_EXEC+"="+sideCall[Constants.EXEC]+"&"+ARGS_PARAM+"="+",".join(sideCall[Constants.ARGS])+")"))
  return contextMenu

def addMoveEntryToFolderEntry(contextMenu, path):
  contextMenu.append((MOVE_TO_FOLDER_STRING, PLUGIN_ACTION+ACTION+"="+ACTION_MOVE_TO_FOLDER+"&"+DIR+"="+path+")"))
  return contextMenu

def addRemoveCustomEntry(contextMenu, path):
  contextMenu.append((REMOVE_CUSTOM_ENTRY_STRING, PLUGIN_ACTION+ACTION+"="+ACTION_REMOVE_FROM_CUSTOMS+"&"+DIR+"="+path+")"))
  return contextMenu
def addAddStartToCustomEntries(contextMenu, path):
  contextMenu.append((ADD_START_ENTRY_TO_CUSTOMS_STRING, PLUGIN_ACTION+ACTION+"="+ACTION_ADD_START_TO_CUSTOM+"&"+DIR+"="+path+")"))
  return contextMenu
def addCustomVariantEntry(contextMenu, path):
  contextMenu.append((CREATE_CUSTOM_VARIANT_STRING, PLUGIN_ACTION+ACTION+"="+ACTION_ADD_CUSTOM_VARIANT+"&"+DIR+"="+path+")"))
  return contextMenu
def addUnsetCustomIconEntry(contextMenu, path):
  contextMenu.append((UNSET_CUSTOM_ICON_STRING, PLUGIN_ACTION+ACTION+"="+ACTION_UNSET_CUSTOM_ICON+"&"+DIR+"="+path+")"))
  return contextMenu
def addUnsetCustomBackgroundEntry(contextMenu, path):
  contextMenu.append((UNSET_CUSTOM_BACKGROUND_STRING, PLUGIN_ACTION+ACTION+"="+ACTION_UNSET_CUSTOM_BACKGROUND+"&"+DIR+"="+path+")"))
  return contextMenu
def addSetCustomIconEntry(contextMenu, path, isCustom):
  contextMenu.append((SET_CUSTOM_ICON_STRING, PLUGIN_ACTION+ACTION+"="+ACTION_SET_CUSTOM_ICON+"&"+DIR+"="+path+"&"+IS_CUSTOM+"="+str(int(isCustom))+")"))
  return contextMenu
def addSetCustomBackgroundEntry(contextMenu, path, isCustom):
  contextMenu.append((SET_CUSTOM_BACKGROUND_STRING, PLUGIN_ACTION+ACTION+"="+ACTION_SET_CUSTOM_BACKGROUND+"&"+DIR+"="+path+"&"+IS_CUSTOM+"="+str(int(isCustom))+")"))
  return contextMenu
def addBaseContextMenu(contextMenu, path, isCustom, isFolder, hasCustomIcon=True, hasCustomBackground=True):
  if isCustom:
    if not isFolder:
      addMoveEntryToFolderEntry(contextMenu, path)
    addRemoveCustomEntry(contextMenu, path)
  else:
    if not isFolder:
      addCustomVariantEntry(contextMenu, path)
      addAddStartToCustomEntries(contextMenu, path)
  if not isFolder:
    if hasCustomIcon:
      addUnsetCustomIconEntry(contextMenu, path)
    else:
      addSetCustomIconEntry(contextMenu, path, isCustom)
    if hasCustomBackground:
      addUnsetCustomBackgroundEntry(contextMenu, path)
    else:
      addSetCustomBackgroundEntry(contextMenu, path, isCustom)


  addForceRefreshButton(contextMenu)
