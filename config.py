# yooo guiz Herox 
import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "BAAkcO4N6bBz4buGS1A7xDRoS7L3-L9KuNzXBIB_Fr7lqb2LyFE1I2lBtMcO9aRQOJroutYTqhj5QdpyDzjp4sE-FkstbsPb-clB8_DYH3NVgVr3l7fMiWFJ6G0VhnnOnSYyUaVtEFZKqeCcdUv0abbx5GQupXzn0dVPckfdENJCdrZv2mIFnMCko_GyDSfQDGeecm3VVqMvXLO5YeptHQCsDops_vokxoi4wCikVeP9sfAIiMT5CpWSibY_sAEReFzJTdRehBDf4jKE6WwOmVZluOsNwHhLKi-Wn_shMgEwHd0UxfKzKDwPf_YTbdgjCBJi7PX6fJsrBwYJU0232tVvAAAAATTDl_YA")
BOT_TOKEN = getenv("BOT_TOKEN", "5253002724:AAHvqxxpWE-fvmQe5F8DBvRE7OQC_6J5Um0")
BOT_NAME = getenv("BOT_NAME", "Osmani-Music")
API_ID = int(getenv("API_ID", "15499461"))
API_HASH = getenv("API_HASH", "ff93948d3b7c3091e8d573275a4ed80f")
OWNER_NAME = getenv("OWNER_NAME", "ribajosmani")
ALIVE_NAME = getenv("ALIVE_NAME", "Ribaj Osmani")
BOT_USERNAME = getenv("BOT_USERNAME", "TrickyAbhi_Music_Bot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "ribajassistant2")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "osmanigroupbot")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "teamosmani")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1008271006").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/a44453181ceccc246cffd.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "7000"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/Ribaj")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/d6f92c979ad96b2031cba.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/af674fcfde30dab8680b2.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/be5f551acb116292d15ec.png")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/92e8c83e9148c6fea5f3b.png")
IMG_6 = getenv("IMG_6", "https://telegra.ph/file/92e8c83e9148c6fea5f3b.png")
