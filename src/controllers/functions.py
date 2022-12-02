# with variable type hinting [ color is in hexadecimal so a string ]
def setFeedBack(self, message: str, color: tuple):
    self.conn_feedback_sTxt.SetLabel(message)
    self.conn_feedback_sTxt.SetForegroundColour(color)
