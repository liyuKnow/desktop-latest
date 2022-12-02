import wx

from .panels import TopPanel, MiddlePanel, BottomPanel


# Conventions
# Classes => Pascal case
# variables  and files => snake case
# Methods => camel case
# wx arguments are user as a keyword argument (not positional)
# WIDGETS at the top and sizers at the bottom
# widget variables have descriptive short suffixes ( wx.Button => *_btn )


class MainWindow (wx.Frame):
    def __init__(self, parent, title):
        super(MainWindow, self).__init__(parent=parent, title=title)

        self.basicConfig()

        self.createWidgets()

    def basicConfig(self):

        # SET NON-RESIZABLE WINDOW SIZE
        self.SetMaxSize(wx.Size(830, 590))
        self.SetMinSize(wx.Size(830, 590))

        self.SetBackgroundColour(wx.Colour("#454545"))

        # SHOW CONFIRMATION POP Up ON EXIT
        self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)

    def createWidgets(self):
        # three section panels
        self.top_Panel = TopPanel(self)
        self.middle_Panel = MiddlePanel(self)
        self.bottom_Panel = BottomPanel(self)

        # One Container panel
        self.container = wx.BoxSizer(wx.VERTICAL)

        # 3 SECTION PANELS in a 1 GRID SIZER with LAYOUT (3 rows x 1 col)
        self.grid_sizer = wx.FlexGridSizer(rows=3, cols=1, vgap=10, hgap=10)

        # ADD WIDGETS TO SIZER
        self.grid_sizer.AddMany([
            self.top_Panel,
            self.middle_Panel,
            self.bottom_Panel
        ])

        # SET SIZER TO PANEL WITH A BOX SIZE WRAPPER
        self.container.Add(self.grid_sizer, proportion=1,
                           flag=wx.ALL | wx.EXPAND, border=10)
        self.SetSizer(self.container)

    def OnCloseWindow(self, event):
        dial = wx.MessageDialog(
            None,
            message="Are you sure you want to quit?",
            caption="Alert",
            style=wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION,
        )

        ret = dial.ShowModal()

        if ret == wx.ID_YES:
            self.Destroy()
        else:
            print(event)
