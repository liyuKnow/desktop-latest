import os
import wx
import subprocess


class TopPanel (wx.Panel):
    def __init__(self, parent):
        super().__init__(parent=parent, size=(790, 100))

        self.basicConfig()

        self.createWidgets()

    def basicConfig(self):
        self.SetBackgroundColour(wx.Colour("#454545"))

    def createWidgets(self):
        # WIDGETS
        # 1 BUTTON, 1 STATIC TEXT (label)

        self.test_conn_btn = wx.Button(
            self, label="Test Connection", size=(120, 40), style=wx.BORDER_NONE
        )
        self.test_conn_btn.Bind(wx.EVT_BUTTON, self.onTestConnection)

        self.conn_feedback_sTxt = wx.StaticText(
            self,
            size=(120, 60),
            label="",
        )
        # ^ DEV
        self.conn_feedback_sTxt.SetFont(
            wx.Font(12, wx.DECORATIVE,  wx.NORMAL, wx.NORMAL, ))

        # SIZERS

        # 1 HORIZONTAL BOX SIZER, 1 FLEXIBLE GRID SIZER, 1 VERTICAL BOX SIZER

        self.container_h_box = wx.BoxSizer(wx.HORIZONTAL)

        # MAKE LAYOUT (1 rows x 2 cols)
        self.grid_sizer = wx.FlexGridSizer(rows=1, cols=2, vgap=10, hgap=10)

        self.text_container_h_box = wx.BoxSizer(wx.HORIZONTAL)
        # CENTER ALIGN FEEDBACK WITH BUTTON
        self.text_container_h_box.Add(
            self.conn_feedback_sTxt, proportion=1, flag=wx.TOP | wx.ALIGN_CENTER, border=10)

        # ADD WIDGETS TO SIZER
        self.grid_sizer.AddMany(
            [
                (self.test_conn_btn),
                (self.text_container_h_box, 0,  wx.EXPAND),
            ]
        )

        self.grid_sizer.AddGrowableCol(1, 1)

        # SET SIZER TO PANEL WITH A BOX SIZE WRAPPER
        self.container_h_box.Add(
            self.grid_sizer, proportion=1, flag=wx.ALL | wx.EXPAND, border=10)

        self.SetSizer(self.container_h_box)

    def onTestConnection(self, event):
        # TODO : CHECK IF THIS WORKS AS AN EXECUTABLE
        # gives us our apps directory (where app.py is at)
        current_working_dir = os.getcwd()

        device_name = ""
        device_list = []

        # user_directory = os.path.expanduser("~")  # dynamic user root folder
        # adb_source = f"{user_directory}/Desktop/REPORT/latest/adb/adb.exe" # STATIC

        # ^ NEW ADB SOURCE
        adb_source = f"{current_working_dir}/adb/adb.exe"  # STATIC

        # ^ ADB COMMAND
        devices_command = f"{adb_source} devices"

        with subprocess.Popen(
            devices_command, stdout=subprocess.PIPE, stderr=None, shell=True
        ) as process:
            output = process.communicate()[0].decode("utf-8")

            if (output != None and "device" in output):
                # SANITIZE THE TABS AND NEW LINES IN THE OUTPUT AND REMOVE HEADER
                device_list_res = " ".join(str(output.split(" ")[3]).split())

                device_list = device_list_res.split(" ")

                # WE CAN CHECK IF DEVICE NAME IS AVAILABLE
                if len(device_list) == 3:
                    # DEVICE FOUND
                    device_name = device_list[1]

                    self.setFeedBack("One Device Found", "success")

                elif len(device_list) > 3:
                    self.setFeedBack(
                        message="More Than One Device Found, Connect only one device and try again", feed_type="error")

                else:
                    self.setFeedBack(
                        message="No Device Found, Connect a device and Try Again!", feed_type="error")
            else:
                self.setFeedBack(
                    message="There is an issue with the adb driver or path", feed_type="error")

    # with variable type hinting

    def setFeedBack(self, message: str = "", feed_type: str = ""):
        if (feed_type == 'success'):
            color = (108, 174, 80)
        elif (feed_type == 'error'):
            color = (199, 93, 85)
        elif (feed_type == 'error'):
            color = (0, 0, 0)

        self.conn_feedback_sTxt.SetLabel(message)
        self.conn_feedback_sTxt.SetForegroundColour(color)
