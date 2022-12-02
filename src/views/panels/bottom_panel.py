import wx


class BottomPanel (wx.Panel):
    def __init__(self, parent):
        super().__init__(parent, size=(790, 180))

        self.basicConfig()

        # self.createWidgets()

    def basicConfig(self):

        # SET SIZE
        self.SetSize(wx.Size(790, 100))

        self.SetBackgroundColour(wx.Colour("#e2e2e2"))

    def createAttributes(self):
        self.user_directory = ""

    def createWidgets(self):
        # One Container panel
        self.container = wx.BoxSizer(wx.VERTICAL)

    def onEvent(self, event):
        pass
