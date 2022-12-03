import wx
import os
import subprocess


class BottomPanel (wx.Panel):
    def __init__(self, parent):
        super().__init__(parent, size=(790, 180))

        self.basicConfig()

        self.createWidgets()

    def basicConfig(self):

        self.SetBackgroundColour(wx.Colour("#bfbfbf"))

    def createAttributes(self):
        self.user_directory = ""

    def createWidgets(self):
        # ^ WIDGETS
        self.left_panel = wx.Panel(self, size=(350, 160))
        self.left_panel.SetBackgroundColour("transparent")

        self.right_panel = wx.Panel(self, size=(410, 160))
        self.right_panel.SetBackgroundColour("transparent")

        self.get_file_btn = wx.Button(
            self.left_panel, label="Get File", size=(186, 50), style=wx.BORDER_NONE)
        self.get_file_btn.Bind(wx.EVT_BUTTON, self.onGetFile)

        self.get_file_feedback_sTxt = wx.StaticText(self.left_panel,
                                                    size=(120, 60),
                                                    label="",)
        self.get_file_feedback_sTxt.SetFont(
            wx.Font(12, wx.DECORATIVE,  wx.NORMAL, wx.NORMAL, ))

        image_path = "./src/assets/images/excel_64_x_40.png"
        # open image from disk
        bmp = wx.Bitmap(image_path, wx.BITMAP_TYPE_ANY)
        # create image button using BitMapButton constructor
        self.open_file_btn = wx.BitmapButton(
            self.right_panel, id=wx.ID_ANY, bitmap=bmp, size=(
                84, 80)
        )
        self.open_file_btn.Bind(wx.EVT_BUTTON, self.onOpenExcel)
        self.open_file_btn.Disable()

        # ^ SIZERS
        # * 1 CONTAINER PANEL
        self.container_v_box = wx.BoxSizer(wx.VERTICAL)

        self.grid_sizer = wx.FlexGridSizer(rows=1, cols=2, vgap=5, hgap=5)

        # * LEFT PANEL SIZER
        self.left_panel_v_box = wx.BoxSizer(wx.VERTICAL)
        self.left_panel_v_box.Add(self.get_file_btn, 0, wx.ALL, 5)
        self.left_panel_v_box.Add(
            self.get_file_feedback_sTxt, 1, wx.EXPAND | wx.ALL, 5)
        self.left_panel.SetSizer(self.left_panel_v_box)

        # * RIGHT PANEL SIZER
        self.right_panel_v_box = wx.BoxSizer(wx.VERTICAL)
        self.right_panel_v_box.Add(self.open_file_btn, 1,
                                   wx.ALIGN_RIGHT | wx.ALL, border=40)
        self.right_panel.SetSizer(self.right_panel_v_box)

        # * PUT ALL INTO THE GRID SIZER
        self.grid_sizer.AddMany([self.left_panel, self.right_panel])

        self.container_v_box.Add(
            self.grid_sizer, proportion=1, flag=wx.ALL | wx.EXPAND, border=10)
        self.SetSizer(self.container_v_box)

    def onFileReceived(self):
        self.open_file_btn.Enable()

    def onOpenExcel(self, event):
        print("there it is")

    def setFeedBack(self, message: str = "", feed_type: str = ""):
        if (feed_type == 'success'):
            color = (108, 174, 80)
        elif (feed_type == 'error'):
            color = (199, 93, 85)
        elif (feed_type == 'info'):
            color = (54, 173, 207)
        elif (feed_type == ''):
            color = (0, 0, 0)

        self.get_file_feedback_sTxt.SetLabel(message)
        self.get_file_feedback_sTxt.SetForegroundColour(color)

    def onGetFile(self, event):
        # TODO : COLLECT REPEATED ADB CODES INTO ONE FUNCTION
        # gives us our application root directory (where app.py is at)
        current_working_dir = os.getcwd()

        # ^ NEW ADB SOURCE
        adb_source = f"{current_working_dir}/adb/adb.exe"

        user_directory = os.path.expanduser("~")

        pull_excel_command = f"{adb_source} pull /storage/emulated/0/Download/NewCounter.txt {user_directory}\Desktop"

        device_command = f"{adb_source} devices"

        with subprocess.Popen(
            device_command, stdout=subprocess.PIPE, stderr=None, shell=True
        ) as process:
            #  CHECK IF DEVICE AVAILABLE
            output = process.communicate()[0].decode("utf-8")

            device_list_res = " ".join(str(output.split(" ")[3]).split())

            device_list = device_list_res.split(" ")

            if (output != None and "device" in output):
                # SANITIZE THE TABS AND NEW LINES IN THE OUTPUT AND REMOVE HEADER
                device_list_res = " ".join(str(output.split(" ")[3]).split())

                device_list = device_list_res.split(" ")

                # WE CAN CHECK IF DEVICE NAME IS AVAILABLE
                if len(device_list) == 3:
                    # DEVICE FOUND AND READY TO GET FILE
                    device_name = device_list[1]

                    excel_output = subprocess.Popen(
                        pull_excel_command, stdout=subprocess.PIPE, stderr=None, shell=True
                    )

                    # new_output = process.communicate()[0].decode("utf-8")

                    # TODO :  MAYBE CHECK THE OUT PUT IF THERE IS AN ERROR TO HANDLE MAYBE A SECOND SUB PROCESS IS NEEDED
                    self.setFeedBack(
                        message="File was Received successfully", feed_type="success")

                    self.onFileReceived()

                elif len(device_list) > 3:
                    self.setFeedBack(
                        message="More Than One Device Found, Connect only one device and try again", feed_type="error")

                else:
                    self.setFeedBack(
                        message="No Device Found, Connect a device and Try Again!", feed_type="error")
            else:
                self.setFeedBack(
                    message="Device not ready or is disconnected", feed_type="error")
