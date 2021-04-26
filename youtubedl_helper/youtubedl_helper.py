from __future__ import unicode_literals
from youtubedl_helper.YTDLLogger import YTDLLogger
from youtubedl_helper.YTDLThread import YDTLThread
import youtube_dl

# number of threads you would like to concurrently run of youtube dl
YTDL_THREADS = 4
# youtube dl options
YTDL_OPTS = {
    "format": "(bestvideo+bestaudio/best)[format_id*=en-US]",
    "logger": YTDLLogger(),
}


def main():
    pass


if __name__ == "__main__":
    main()
