import wx
from src.views import MainWindow


class MyApp(wx.App):
    def OnInit(self):
        self.mainWindow = MainWindow(None, title="Report Helper App")
        self.SetTopWindow(self.mainWindow)
        self.mainWindow.Show()
        self.mainWindow.Center()
        return True  # This is not changed


if __name__ == "__main__":
    app = MyApp(0)
    app.MainLoop()
