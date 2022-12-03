import wx


class MiddlePanel (wx.Panel):
    def __init__(self, parent):
        super().__init__(parent, size=(790, 230))

        self.basicConfig()

        self.createWidgets()

    def basicConfig(self):

        # SET SIZE
        self.SetSize(wx.Size(790, 100))

        self.SetBackgroundColour(wx.Colour("#e2e2e2"))

    def createAttributes(self):
        self.user_directory = ""

    def createWidgets(self):
        # ^ WIDGETS
        self.left_panel = wx.Panel(self, size=(350, 200))
        self.left_panel.SetBackgroundColour("#0000ff")

        self.right_panel = wx.Panel(self, size=(410, 200))
        self.right_panel.SetBackgroundColour("#0000ff")

        self.send_file_btn = wx.Button(
            self.left_panel, label="Send File", size=(186, 50), style=wx.BORDER_NONE)
        self.send_file_btn.Bind(wx.EVT_BUTTON, self.onSendFile)

        self.send_file_feedback_sTxt = wx.StaticText(self.left_panel,
                                                     size=(120, 60),
                                                     label="",)
        self.send_file_feedback_sTxt.SetFont(
            wx.Font(12, wx.DECORATIVE,  wx.NORMAL, wx.NORMAL, ))

        # ^ SIZERS
        # # * 1 CONTAINER PANEL
        self.container_v_box = wx.BoxSizer(wx.VERTICAL)

        self.grid_sizer = wx.FlexGridSizer(rows=1, cols=2, vgap=5, hgap=5)

        # # * LEFT PANEL SIZER
        self.left_panel_h_box = wx.BoxSizer(wx.HORIZONTAL)

        # self.left_panel_v_box = wx.BoxSizer(wx.VERTICAL)
        # self.left_panel_v_box.Add(self.get_file_btn, 0, wx.ALL, 5)
        # self.left_panel_v_box.Add(
        #     self.get_file_feedback_sTxt, 1, wx.EXPAND | wx.ALL, 5)
        # self.left_panel.SetSizer(self.left_panel_v_box)

        # # * RIGHT PANEL SIZER
        # self.right_panel_v_box = wx.BoxSizer(wx.VERTICAL)
        # self.right_panel_v_box.Add(self.open_file_btn, 1,
        #                            wx.ALIGN_RIGHT | wx.ALL, border=40)
        # self.right_panel.SetSizer(self.right_panel_v_box)

        # * PUT ALL INTO THE GRID SIZER
        self.grid_sizer.AddMany([self.left_panel, self.right_panel])

        self.container_v_box.Add(
            self.grid_sizer, proportion=1, flag=wx.ALL | wx.EXPAND, border=10)
        self.SetSizer(self.container_v_box)

    def onSendFile(self, event):
        print("Hello")
