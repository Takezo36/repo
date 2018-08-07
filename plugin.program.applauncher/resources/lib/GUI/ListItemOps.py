def addAddCustomEntryButton(handle, path):
  li = xbmcgui.ListItem(CREATE_CUSTOM_ENTRY_STRING)
  li.setPath(path="plugin://plugin.program.applauncher?"+ACTION+"="+ACTION_ADD_CUSTOM_ENTRY+"&"+DIR+"="+urllib.quote(path))
  xbmcplugin.addDirectoryItem(handle, li.getPath(), li)
def addAddCustomFolderButton(handle, path):
  li = xbmcgui.ListItem(CREATE_CUSTOM_FOLDER_STRING)
  li.setPath(path="plugin://plugin.program.applauncher?"+ACTION+"="+ACTION_ADD_CUSTOM_FOLDER+"&"+DIR+"="+urllib.quote(path))
  xbmcplugin.addDirectoryItem(handle, li.getPath(), li) 
def createFolder(name, target, path, isCustom):
  li = xbmcgui.ListItem(name)
  li.setPath(path=target)
  contextMenu = []
  addBaseContextMenu(contextMenu, path, isCustom, True)
  li.addContextMenuItems(contextMenu)
  return li

def createAppEntry(entry, addToStartPath, isCustom = False):
  li = xbmcgui.ListItem(entry[Constants.NAME])
  arts = loadData()[CUSTOM_ARTS]
  try:
    for key in addToStartPath.split(DIR_SEP):
      arts = arts[key]
  except:
    arts = None
  hasCustomIcon = False
  hasCustomBackground = False
  if arts and Constants.ICON in arts.keys():
    icon = arts[Constants.ICON]
    hasCustomIcon = True
  elif Constants.ICON in entry:
    icon = entry[Constants.ICON]
  else:
    icon = ""
  #this is a stupid bugfix for a strange serialization bug in powershell
  if type(icon) is list:
    icon = icon[1]
  if arts and Constants.BACKGROUND in arts.keys():
    background = arts[Constants.BACKGROUND]
    hasCustomBackground = True
  elif Constants.BACKGROUND in entry:
    background = entry[Constants.BACKGROUND]
  else:
    background = icon
  try:
    li.setArt({'icon' : icon,
               'thumb':icon,
               'poster':icon,
               'banner':icon,
               'fanart':background,
               'clearart':icon,
               'clearlogo':icon,
               'landscape':icon})
  except:
    xbmc.log("Failed to load icon " + str(icon), xbmc.LOGDEBUG)
  contextMenu = []
  if Constants.SIDECALLS in entry.keys():
    addSideCallEntries(contextMenu, entry[Constants.SIDECALLS])
  addBaseContextMenu(contextMenu, addToStartPath, isCustom, False, hasCustomIcon, hasCustomBackground)
  li.addContextMenuItems(contextMenu)
  try:
    li.setPath(path="plugin://plugin.program.applauncher?"+ACTION+"="+ACTION_EXEC+"&"+ACTION_EXEC+"="+entry[Constants.EXEC]+"&"+ARGS_PARAM+"="+urllib.quote(",".join(entry[Constants.ARGS])))
  except:
    xbmc.log("Failed to load entry", xbmc.LOGDEBUG)
  return li