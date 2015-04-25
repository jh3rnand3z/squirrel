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

import  wx.lib.mixins.listctrl  as  listmix

from panels import panelOne, panelTwo, panelThree, panelFour, panelFive, panelSix

import images


def getNextImageID(count) :
    '''
        Some while loop yielding some shit out while counting
    '''
    imID = 0
    while True :
        yield imID
        imID += 1


class TestListCtrl( wx.ListCtrl, listmix.ListCtrlAutoWidthMixin ) :
    
    def __init__( self, parent, id=-1, pos=wx.DefaultPosition,
                        size=wx.DefaultSize, style=0 ) :
        
        wx.ListCtrl.__init__( self, parent, id, pos, size, style )
        
        listmix.ListCtrlAutoWidthMixin.__init__( self )


class TabPanel(wx.Panel, listmix.ColumnSorterMixin) :
    '''
        This will be the second notebook tab
    '''

    def __init__(self, parent) :
        '''
            TabPanel Constructor
        '''
        wx.Panel.__init__( self, parent=parent, id=wx.ID_ANY )
        self.createAndLayout()

    def createAndLayout( self ) :
        '''
            Create and Layout
        '''
        sizer = wx.BoxSizer( wx.VERTICAL )
        self.list = TestListCtrl( self, wx.ID_ANY, style=wx.LC_REPORT
                                        | wx.BORDER_NONE
                                        | wx.LC_EDIT_LABELS
                                        | wx.LC_SORT_ASCENDING )
        sizer.Add( self.list, proportion=1, flag=wx.EXPAND )
        self.populateList()
        
        # Now that the list exists we can init the other base class,
        #   see [ wx/lib/mixins/listctrl.py ].
        self.itemDataMap = musicdata
        numCols = 5
        listmix.ColumnSorterMixin.__init__( self, numCols )
        
        self.SetSizer( sizer )
        self.Layout()

    def populateList( self ) :
        '''
            Populate list
        '''
        self.list.InsertColumn( 0, 'Artist' )
        self.list.InsertColumn( 1, 'Title', wx.LIST_FORMAT_RIGHT )
        self.list.InsertColumn( 2, 'Genre' )
        items = musicdata.items()

        for key, data in items :
            index = self.list.InsertStringItem( sys.maxint, data[ 0 ] )
            self.list.SetStringItem( index, 1, data[ 1 ] )
            self.list.SetStringItem( index, 2, data[ 2 ] )
            self.list.SetItemData( index, key )

        self.list.SetColumnWidth( 0, wx.LIST_AUTOSIZE )
        self.list.SetColumnWidth( 1, wx.LIST_AUTOSIZE )
        self.list.SetColumnWidth( 2, 100 )

        # show how to select an item
        self.list.SetItemState(5, wx.LIST_STATE_SELECTED, wx.LIST_STATE_SELECTED)

        # show how to change the colour of a couple items
        item = self.list.GetItem( 1 )
        item.SetTextColour( wx.BLUE )
        self.list.SetItem( item )
        
        item = self.list.GetItem( 4 )
        item.SetTextColour( wx.RED )
        self.list.SetItem( item )

        self.currentItem = 0
    
    def GetListCtrl( self ) :
        '''
            Used by the ColumnSorterMixin, see wx/lib/mixins/listctrl.py
        '''
        return self.list


class ToolbookDemo(wx.Toolbook) :
    
    def __init__(self, parent) :
        '''
            Toolbook Constructor
        '''
        wx.Toolbook.__init__(self, parent, wx.ID_ANY, style=wx.BK_DEFAULT)

        # Make an image list using the LBXX images
        il = wx.ImageList(32, 32)
        for x in range(6):
            imgObj = getattr(images, 'LB%02d' % (x+1))
            bmp = imgObj.GetBitmap()
            il.Add(bmp)

        self.AssignImageList(il)
        imageIdGenerator = getNextImageID(il.GetImageCount())

        notebookPageList = [(panelOne.TabPanel(self), 'General'),
                            (panelTwo.TabPanel(self), 'Account'),
                            (panelThree.TabPanel(self), 'Applications'),
                            (panelFive.TabPanel(self), 'Trash'),
                            (panelSix.TabPanel(self), 'Import')]
        imID = 0
        for page, label in notebookPageList:
            
            self.AddPage(page, label, imageId=imageIdGenerator.next())
            imID += 1

        # An undocumented method in the official docs:
        self.ChangeSelection(1)     # Select and view this notebook page.
                                    # Creates no events - method SetSelection does.
        
        self.Bind(wx.EVT_TOOLBOOK_PAGE_CHANGING, self.OnPageChanging)
        self.Bind(wx.EVT_TOOLBOOK_PAGE_CHANGED,  self.OnPageChanged)

    def OnPageChanging(self, event) :
        '''
            On page changing
        '''
        old = event.GetOldSelection()
        new = event.GetSelection()
        sel = self.GetSelection()

        print 'OnPageChanging{}: old: %d, new: %d, sel: %d' % (old, new, sel)
        event.Skip()

    def OnPageChanged( self, event ) :
        '''
            On page changed
        '''
        old = event.GetOldSelection()
        new = event.GetSelection()
        sel = self.GetSelection()
        
        print 'OnPageChanged{}: old: %d, new: %d, sel: %d' % (old, new, sel)
        event.Skip()


class Colours(wx.Dialog):
    def __init__(self, parent, id, title):
        '''
            Constructor
        '''
        wx.Dialog.__init__(self, parent, id, title, size=(416,420))        
        
        self.tbIcon = taskbar.CustomTaskBarIcon(self)

        panel = wx.Panel(self)

        notebook = ToolbookDemo( panel )

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(notebook, proportion=1, flag=wx.ALL|wx.EXPAND, border=5)
        panel.SetSizer(sizer)
        self.Layout()

        self.Bind(wx.EVT_ICONIZE, self.onMinimize)
        self.Bind(wx.EVT_CLOSE, self.onClose)

    def onClose(self, event):
        '''
            Destroy the taskbar icon and the frame
        '''
        self.tbIcon.RemoveIcon()
        self.tbIcon.Destroy()
        self.Destroy()
 
    def onMinimize(self, event):
        '''
            When minimizing, hide the frame so it "minimizes to tray"
        '''
        self.Hide()


def main():
    '''
        Squirrel Monkey
    '''
    app = wx.App(False)
    Colours(None, -1, 'Monkey Preferences')
    app.MainLoop()

if __name__ == "__main__":
    main()