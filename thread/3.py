import time
from threading import *
import wx

ID_START = wx.NewId()
ID_STOP = wx.NewId()

EVT_RESULT_ID  = wx.NewId()

def EVT_RESULT(win,func):
	win.Connect(-1,-1,EVT_RESULT_ID ,func)

class ResultEvent(wx.pyEvent):
	def __init__(self,data):
		wx.pyEvent.__init__(self)
		self.SetEventType(EVT_RESULT_ID)
		self.data = data

class WorkerThread(Thread):
	def __init__(self,notify_window):
		Thread.__init__(self)
		self._notify_window = notify_window
		self._want_abort = 0
		self.start()
	def run(self):
		for i in range(10):
			time.sleep()
			if self._want_abort:
				wx.PostWvent(self._notify_window,ResultEvent(None))
				return
	def abort(self):
		self._want_abort = 1

class MainFrame(wx.Frame):
    """Class MainFrame."""
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'Thread Test')

        # Dumb sample frame with two buttons
        wx.Button(self, ID_START, 'Start', pos=(0,0))
        wx.Button(self, ID_STOP, 'Stop', pos=(0,50))
        self.status = wx.StaticText(self, -1, '', pos=(0,100))

        self.Bind(wx.EVT_BUTTON, self.OnStart, id=ID_START)
        self.Bind(wx.EVT_BUTTON, self.OnStop, id=ID_STOP)

        # Set up event handler for any worker thread results
        EVT_RESULT(self,self.OnResult)

        # And indicate we don't have a worker thread yet
        self.worker = None

    def OnStart(self, event):
        """Start Computation."""
        # Trigger the worker thread unless it's already busy
        if not self.worker:
            self.status.SetLabel('Starting computation')
            self.worker = WorkerThread(self)

    def OnStop(self, event):
        """Stop Computation."""
        # Flag the worker thread to stop if running
        if self.worker:
            self.status.SetLabel('Trying to abort computation')
            self.worker.abort()

    def OnResult(self, event):
        """Show Result status."""
        if event.data is None:
            # Thread aborted (using our convention of None return)
            self.status.SetLabel('Computation aborted')
        else:
            # Process results here
            self.status.SetLabel('Computation Result: %s' % event.data)
        # In either event, the worker is done
        self.worker = None

class MainApp(wx.App):
    """Class Main App."""
    def OnInit(self):
        """Init Main App."""
        self.frame = MainFrame(None, -1)
        self.frame.Show(True)
        self.SetTopWindow(self.frame)
        return True

if __name__ == '__main__':
    app = MainApp(0)
    app.MainLoop()

