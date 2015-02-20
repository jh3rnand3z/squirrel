# -*- coding: utf-8 -*-
'''
    Squirell wxWidgets TaskBar.
'''

# This file is part of squirrel.

# Distributed under the terms of the last Apache License.
# The full license is in the file LICENCE, distributed as part of this software.

__author__ = 'Jean Chassoul'


import wx


class CustomTaskBarIcon(wx.TaskBarIcon):
    """
        Custom TaskBar Icon
    """

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

        self.SetIcon(self.icon, "Restore")
        self.Bind(wx.EVT_TASKBAR_LEFT_DOWN, self.OnTaskBarLeftClick)
 
    def OnTaskBarActivate(self, evt):
        """"""
        pass
 
    def OnTaskBarClose(self, evt):
        """
            Destroy the taskbar icon and frame from the taskbar icon itself
        """
        self.frame.Close()
 
    def OnTaskBarLeftClick(self, evt):
        """
            Create the right-click menu
        """
        self.frame.Show()
        self.frame.Restore()