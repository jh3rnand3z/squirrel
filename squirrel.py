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


class MainFrame(wx.Frame):
    """
    """

    def __init__(self):
        """
            Constructor
        """
        wx.Frame.__init__(self, None, title="Minimize to Tray")
        panel = wx.Panel(self)
        self.tbIcon = taskbar.CustomTaskBarIcon(self)
 
        self.Bind(wx.EVT_ICONIZE, self.onMinimize)
        self.Bind(wx.EVT_CLOSE, self.onClose)
 
        self.Show()
 
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
    frame = MainFrame()
    app.MainLoop()
 
if __name__ == "__main__":
    main()