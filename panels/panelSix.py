#----------------------------------------------------------------------
# panelOne.py
#
# Created 11/26/2009
#
# Author : Mike Driscoll - mike@pythonlibrary.org
#
#----------------------------------------------------------------------

import wx

class TabPanel( wx.Panel ) :
    """ This will be [inserted into] the first notebook tab. """
    
    def __init__( self, parent ) :
        
        wx.Panel.__init__( self, parent=parent, id=wx.ID_ANY )
        
        sizer = wx.BoxSizer( wx.VERTICAL )
        txtOne = wx.TextCtrl( self, wx.ID_ANY, "sdsd" )
        txtTwo = wx.TextCtrl( self, wx.ID_ANY, "" )
        
        sizer = wx.BoxSizer( wx.VERTICAL )
        sizer.Add( txtOne, 0, wx.ALL, 5 )
        sizer.Add( txtTwo, 0, wx.ALL, 5 )
        
        self.SetSizer( sizer )
        
    #end __init__
        
#end class

#==============================================================================

if __name__ == "__main__" :
    
    class DemoFrame( wx.Frame ) :

        def __init__( self ) :

            wx.Frame.__init__( self, None, wx.ID_ANY, "Panel Tutorial" )
            panel = TabPanel( self )
        
    #end class
    
    #----------------------------------
    
    app = wx.App( redirect=False )
    appFrame = DemoFrame()
    appFrame.Show()
    app.MainLoop()

#end if