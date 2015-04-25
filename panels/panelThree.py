#----------------------------------------------------------------------
# panelThree.py
#
# Created 11/26/2009
#
# Author : Mike Driscoll - mike@pythonlibrary.org
#
# Note : The TreeListCtrl code was taken from the Official wxPython Demo
#
#----------------------------------------------------------------------

import wx
import wx.gizmos as gizmos

#------------------------------------------------------------------------------
#==============================================================================
#------------------------------------------------------------------------------

class TabPanel( wx.Panel ) :
    """ This will be [ inserted into ] the first notebook tab. """
    
    def __init__( self, parent ) :
        
        wx.Panel.__init__( self, parent=parent, id=wx.ID_ANY )
        
        self.Bind( wx.EVT_SIZE, self.OnSize )
        
        self.tree = gizmos.TreeListCtrl( self, -1, 
                            style=wx.TR_DEFAULT_STYLE | wx.TR_FULL_ROW_HIGHLIGHT )
        
        isz = (16, 16)      # All button icon sizes.
        imgList = wx.ImageList( *isz )
        fldridx     = imgList.Add( wx.ArtProvider_GetBitmap( wx.ART_FOLDER,      wx.ART_OTHER, isz ) )
        fldropenidx = imgList.Add( wx.ArtProvider_GetBitmap( wx.ART_FILE_OPEN,   wx.ART_OTHER, isz ) )
        fileidx     = imgList.Add( wx.ArtProvider_GetBitmap( wx.ART_NORMAL_FILE, wx.ART_OTHER, isz ) )
        bulbidx     = imgList.Add( wx.ArtProvider_GetBitmap( wx.ART_TIP,         wx.ART_OTHER, isz ) )
        
        self.tree.SetImageList( imgList )
        self.imgList = imgList
        
        # create some columns
        self.tree.AddColumn( "Main column" )
        self.tree.AddColumn( "Column 1" )
        self.tree.AddColumn( "Column 2" )
        self.tree.SetMainColumn( 0 ) # the one with the tree in it...
        self.tree.SetColumnWidth( 0, 175 )
        
        # 
        self.root = self.tree.AddRoot( "The Root Item" )
        self.tree.SetItemText( self.root, "col 1 root", 1 )
        self.tree.SetItemText( self.root, "col 2 root", 2 )
        self.tree.SetItemImage( self.root, fldridx, which = wx.TreeItemIcon_Normal )
        self.tree.SetItemImage( self.root, fldropenidx, which = wx.TreeItemIcon_Expanded )
        
        # 
        for x in range( 15 ) :      # ??? "Magic Number" ???
            
            txt = "Item %d" % x
            child = self.tree.AppendItem( self.root, txt )
            self.tree.SetItemText( child, txt + "( c1 )", 1 )
            self.tree.SetItemText( child, txt + "( c2 )", 2 )
            self.tree.SetItemImage( child, fldridx, which = wx.TreeItemIcon_Normal )
            self.tree.SetItemImage( child, fldropenidx, which = wx.TreeItemIcon_Expanded )
            
            for y in range( 5 ) :   # ??? "Magic Number" ???
                
                txt = "item %d-%s" % ( x, chr( ord( "a" )+y ) )
                last = self.tree.AppendItem( child, txt )
                self.tree.SetItemText( last, txt + "( c1 )", 1 )
                self.tree.SetItemText( last, txt + "( c2 )", 2 )
                self.tree.SetItemImage( last, fldridx, which = wx.TreeItemIcon_Normal )
                self.tree.SetItemImage( last, fldropenidx, which = wx.TreeItemIcon_Expanded )
                
                for z in range( 5 ) :   # ??? "Magic Number" ???
                    
                    txt = "item %d-%s-%d" % ( x, chr( ord( "a" )+y ), z )
                    item = self.tree.AppendItem( last,  txt )
                    self.tree.SetItemText( item, txt + "( c1 )", 1 )
                    self.tree.SetItemText( item, txt + "( c2 )", 2 )
                    self.tree.SetItemImage( item, fileidx, which = wx.TreeItemIcon_Normal )
                    self.tree.SetItemImage( item, bulbidx, which = wx.TreeItemIcon_Selected )
                    
                #end for
            #end for
        #end for
        
        self.tree.Expand( self.root )
        
        # ?
        self.tree.GetMainWindow().Bind( wx.EVT_RIGHT_UP, self.OnRightUp )
        self.tree.Bind( wx.EVT_TREE_ITEM_ACTIVATED, self.OnActivate )
        
    #end __init__
    
    #----------------------------------
    
    def OnActivate( self, evt ) :
        print 'OnActivate : %s' % self.tree.GetItemText( evt.GetItem() )
    
    #----------------------------------
    
    def OnRightUp( self, evt ) :
        pos = evt.GetPosition()
        item, flags, col = self.tree.HitTest( pos )
        if item :
            print 'Flags : %s, Col :%s, Text : %s' % ( flags, col, 
                                                   self.tree.GetItemText( item, col ) )
    
    #----------------------------------
    
    def OnSize( self, evt ) :
        self.tree.SetSize( self.GetSize() )
    
#end TabPanel class
#------------------------------------------------------------------------------
#==============================================================================
#------------------------------------------------------------------------------

class DemoFrame( wx.Frame ) :
    
    def __init__( self ) :
       
        wx.Frame.__init__( self, None, wx.ID_ANY, "Panel Tutorial" )
        panel = TabPanel( self )
        
#end class

#==============================================================================

if __name__ == "__main__" :
    
    app = wx.App( redirect=False)
    appFrame = DemoFrame()
    appFrame.Show()
    app.MainLoop()

#end if