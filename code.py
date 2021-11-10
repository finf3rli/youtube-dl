import io
import sys
import youtube_dl

class YoutubeDownloader():
    def __init__(self):
        self.yt = youtube_dl.YoutubeDL()
        self.yt.params = {"listformats": None,
                          "skip_download": None,
                          "format:": None,
                          "forcetitle": None
                         }

    def get_video_name(self, URL):
        self.yt.params.__setitem__("listformats", False)
        self.yt.params.__setitem__("skip_download", True)
        self.yt.params.__setitem__("forcetitle", True)

        old_stdout = sys.stdout  # Swaps from STDOUT to a variable
        new_stdout = io.StringIO()
        sys.stdout = new_stdout

        with youtube_dl.YoutubeDL(self.yt.params) as ydl:
            ydl.download([URL])

        sys.stdout = old_stdout
        return new_stdout.getvalue()

    def list_formats(self, URL):
        self.yt.params.__setitem__("listformats", True)
        self.yt.params.__setitem__("skip_download", True)
        self.yt.params.__setitem__("format", None)

        old_stdout = sys.stdout                             # Swaps from STDOUT to a variable
        new_stdout = io.StringIO()
        sys.stdout = new_stdout

        with youtube_dl.YoutubeDL(self.yt.params) as ydl:
            ydl.download([URL])

        sys.stdout = old_stdout                             # Restores STDOUT

        return new_stdout.getvalue()                        # Output of STDOUT


    def download(self, id, URL):
        self.yt.params.__setitem__("listformats", False)
        self.yt.params.__setitem__("skip_download", False)
        self.yt.params.__setitem__("format", id)

        with youtube_dl.YoutubeDL(self.yt.params) as ydl:
            ydl.download([URL])