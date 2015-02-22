# -*- coding: utf-8 -*-
'''
    Squirell main app.
'''

# This file is part of squirrel.

# Distributed under the terms of the last Apache License.
# The full license is in the file LICENCE, distributed as part of this software.

__author__ = 'Jean Chassoul'


import taskbar
import wx


class Colours(wx.Dialog):
    def __init__(self, parent, id, title):
        """
            Constructor
        """
        wx.Dialog.__init__(self, parent, id, title, size=(300, 300))        
        
        self.tbIcon = taskbar.CustomTaskBarIcon(self)
 
        self.Bind(wx.EVT_ICONIZE, self.onMinimize)
        self.Bind(wx.EVT_CLOSE, self.onClose)

        vbox = wx.BoxSizer(wx.VERTICAL)
        self.pnl1 = wx.Panel(self, -1)
        self.pnl2 = wx.Panel(self, -1)
        self.pnl3 = wx.Panel(self, -1)
        self.pnl4 = wx.Panel(self, -1)
        self.pnl5 = wx.Panel(self, -1)
        self.pnl6 = wx.Panel(self, -1)
        self.pnl7 = wx.Panel(self, -1)
        self.pnl8 = wx.Panel(self, -1)

        gs = wx.GridSizer(4,2,3,3)
        gs.AddMany([ (self.pnl1, 0 ,wx.EXPAND),
            (self.pnl2, 0, wx.EXPAND),
            (self.pnl3, 0, wx.EXPAND),
            (self.pnl4, 0, wx.EXPAND),
            (self.pnl5, 0, wx.EXPAND),
            (self.pnl6, 0, wx.EXPAND),
            (self.pnl7, 0, wx.EXPAND),
            (self.pnl8, 0, wx.EXPAND) ])

        vbox.Add(gs, 1, wx.EXPAND | wx.TOP, 5)
        self.SetSizer(vbox)
        self.SetColors()
        self.Centre()
        self.Hide()

    def SetColors(self):
        self.pnl1.SetBackgroundColour(wx.BLACK)
        self.pnl2.SetBackgroundColour(wx.Colour(139,105,20))
        self.pnl3.SetBackgroundColour(wx.RED)
        self.pnl4.SetBackgroundColour('#0000FF')
        self.pnl5.SetBackgroundColour('sea green')
        self.pnl6.SetBackgroundColour('midnight blue')
        self.pnl7.SetBackgroundColour(wx.LIGHT_GREY)
        self.pnl8.SetBackgroundColour('plum')

    def onClose(self, evt):
        """
            Destroy the taskbar icon and the frame
        """
        self.tbIcon.RemoveIcon()
        self.tbIcon.Destroy()
        self.Destroy()
 
    def onMinimize(self, event):
        """
            When minimizing, hide the frame so it "minimizes to tray"
        """
        self.Hide()


def main():
    """"""
    app = wx.App(False)
    Colours(None, -1, 'colours.py')
    app.MainLoop()

if __name__ == "__main__":
    main()