# -*- coding: utf-8 -*-
'''
    Squirell wxWidgets TaskBar.
'''

# This file is part of squirrel.

# Distributed under the terms of the last Apache License.
# The full license is in the file LICENCE, distributed as part of this software.

__author__ = 'Jean Chassoul'


import wx
import webbrowser
import logging


io_fun_website = 'http://iofun.techgcs.com'
io_fun_help = 'http://iofun.techgcs.com/#help'


class CustomTaskBarIcon(wx.TaskBarIcon):
    """
        Custom TaskBar Icon
    """
    TBMENU_WEBSITE = wx.NewId()
    TBMENU_PAUSE = wx.NewId()
    TBMENU_RESTORE = wx.NewId()
    TBMENU_CHANGE = wx.NewId()
    TBMENU_REMOVE = wx.NewId()
    TBMENU_PREFERENCES = wx.NewId()
    TBMENU_HELP = wx.NewId()
    TBMENU_CLOSE = wx.NewId()

    def __init__(self, frame):
        """
            Constructor
        """
        wx.TaskBarIcon.__init__(self)
        self.frame = frame
 
        img = wx.Image("24x24.png", wx.BITMAP_TYPE_ANY)
        bmp = wx.BitmapFromImage(img)
        self.icon = wx.EmptyIcon()
        self.icon.CopyFromBitmap(bmp)

        self.SetIcon(self.icon, "Squirrel monkey")
        
        # bind some events
        self.Bind(wx.EVT_MENU, self.OnTaskBarClose, id=self.TBMENU_CLOSE)
        self.Bind(wx.EVT_MENU, self.OnLaunchWebsite, id=self.TBMENU_WEBSITE)
        self.Bind(wx.EVT_MENU, self.OnPreferences, id=self.TBMENU_PREFERENCES)
        self.Bind(wx.EVT_MENU, self.OnHelpCenter, id=self.TBMENU_HELP)
        self.Bind(wx.EVT_TASKBAR_LEFT_DOWN, self.OnTaskBarLeftClick)
        self.Bind(wx.EVT_TASKBAR_RIGHT_DOWN, self.OnTaskBarRightClick)

    def CreatePopupMenu(self, event=None):
        """
            This method is called by the base class when it need to popup
            the menu for the default EVT_RIGHT_DOWN event.

            Just create the menu how you want it and return it from this function,
            the base class takes care of the rest.
        """
        menu = wx.Menu()
        menu.Append(self.TBMENU_WEBSITE, "Launch Website")
        menu.AppendSeparator()
        menu.Append(self.TBMENU_PAUSE, "Pause Assistant")
        menu.AppendSeparator()
        menu.Append(self.TBMENU_PREFERENCES, "Preferences")
        menu.Append(self.TBMENU_HELP, "Help")
        menu.AppendSeparator()
        menu.Append(self.TBMENU_CLOSE, "Exit")
        return menu

    def OnTaskBarActivate(self, event):
        """

        """
        pass
 
    def OnTaskBarClose(self, event):
        """
            Destroy the taskbar icon and frame from the taskbar icon itself
        """
        logging.info('on taskbar close')
        self.frame.Close()
 
    def OnTaskBarLeftClick(self, event):
        """
            Show the hidden squirrel
        """
        logging.info('on taskbar left click')
        print('on taskbar left click')

    def OnTaskBarRightClick(self, event):
        """
            Create the right-click menu
        """
        logging.info('on taskbar right click')
        print('on taskbar right click')
        #self.frame.Hide()
        menu = self.CreatePopupMenu()
        self.PopupMenu(menu)
        menu.Destroy()

    def OnLaunchWebsite(self, event):
        """
            Launch Website
        """
        print('on launch website')
        webbrowser.open(io_fun_website)

    def OnPreferences(self, event):
        """
            On Preferences
        """
        print('on preferences')
        self.frame.Show()
        self.frame.Restore()

    def OnHelpCenter(self, event):
        """
            Launch Help center
        """
        print('on help center')
        webbrowser.open(io_fun_help)