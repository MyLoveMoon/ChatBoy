import os
API_ID :int = int(os.environ.get("API_ID", None))
API_HASH :str = os.environ.get("API_HASH", "")
BOT_TOKEN :str= os.environ.get("BOT_TOKEN", "")
UPDATE_CHNL :str = os.environ.get("UPDATE_CHNL", "DarkLightFederation")
SUPPORT_GRP :str = os.environ.get("SUPPORT_GRP", "DarkLightFederation")
START_IMG :str = os.environ.get(
    "START_IMG", "https://graph.org/file/9343555f5c4f395d86533.jpg"
)

MONGO_DB_URI :str = os.environ.get(
    "MONGO_DB_URI",
    "",
)
OWNER_ID :int= os.environ.get("OWNER_ID", 5056205033)

