from os import getenv
from dotenv import load_dotenv

load_dotenv()

class Config:
    def __init__(self):
        self.API_ID = int(getenv("API_ID", "24208695"))
        self.API_HASH = getenv("API_HASH", "fa96a7eb2dffe7f4cc8ba1399b68d24d")

        self.BOT_TOKEN = getenv("BOT_TOKEN", "7850675931:AAFVjBhaO9D2ZNdRZjbATkAsCqZAdvD2hNs")
        self.MONGO_URL = getenv("MONGO_URL", "mongodb+srv://LUSTIFYXMUSIC:Abhi77394@lustifymusic.evxnqby.mongodb.net/?retryWrites=true&w=majority&appName=LUSTIFYMUSIC")

        self.LOGGER_ID = int(getenv("LOGGER_ID", "-1003451226112"))
        self.OWNER_ID = int(getenv("OWNER_ID", "7603581459"))

        self.DURATION_LIMIT = int(getenv("DURATION_LIMIT", 60)) * 60
        self.QUEUE_LIMIT = int(getenv("QUEUE_LIMIT", 20))
        self.PLAYLIST_LIMIT = int(getenv("PLAYLIST_LIMIT", 20))

        self.SESSION1 = getenv("SESSION", "BQFZuDsAlI9PGTSv2KJ1V4LbUe7LBoNvQExsvz_7dpQnbm3Y0Hka65rjndUHb_2gD24FMaYTwiZXUzZDzyjCWMV5q0ADG6ki648XCgWOw52UIgTyRWR-PMrIQh9Um0uIJSP_EPgJ6LGAIUQ1gWMjYnAJqurqoaQqCyv_sGzKxOMGyvl6okB-kK2G5py4J7fpId6aBmYIvfH24UtU9HHz18dx2AkOKmDcffRD3yp2dkSyZW69MUGQc6vck2vlFU-tn9uRKflDAH7fAao9a97v2JLzZNPfqMjXkXUR4EjxY2rsrgwyjEZMcOlOHj04nfK1ZxCFj9P8nZ9EmOdPE_Y8NnBhMWRArAAAAAGMQVi8AA")
        self.SESSION2 = getenv("SESSION2", None)
        self.SESSION3 = getenv("SESSION3", None)

        self.SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/CodeSearchDev")
        self.SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/DebugAngels")

        self.AUTO_END: bool = getenv("AUTO_END", False)
        self.AUTO_LEAVE: bool = getenv("AUTO_LEAVE", False)
        self.VIDEO_PLAY: bool = getenv("VIDEO_PLAY", True)
        self.COOKIES_URL = [
            url for url in getenv("COOKIES_URL", "").split(" ")
            if url and "batbin.me" in url
        ]
        self.DEFAULT_THUMB = getenv("DEFAULT_THUMB", "https://te.legra.ph/file/3e40a408286d4eda24191.jpg")
        self.PING_IMG = getenv("PING_IMG", "https://files.catbox.moe/haagg2.png")
        self.START_IMG = getenv("START_IMG", "https://files.catbox.moe/zvziwk.jpg")

    def check(self):
        missing = [
            var
            for var in ["API_ID", "API_HASH", "BOT_TOKEN", "MONGO_URL", "LOGGER_ID", "OWNER_ID", "SESSION1"]
            if not getattr(self, var)
        ]
        if missing:
            raise SystemExit(f"Missing required environment variables: {', '.join(missing)}")
