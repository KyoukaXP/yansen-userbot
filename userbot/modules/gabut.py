from platform import uname
from time import sleep

from userbot import ALIVE_NAME
from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP, WEATHER_DEFCITY
from userbot.utils import lepin_cmd

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@lepin_cmd(pattern="g(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit(f"**JAKA SEMBUNG BAWA GOLOK**")
    sleep(3)
    await typew.edit("**NIMBRUNG LAH GOBLOKK!!!**")


# Pantun


@lepin_cmd(pattern="p(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Salam Dulu Biar Sopan...`")
    sleep(2)
    await typew.edit("`السَّلاَمُ عَلَيْكُمْ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ`")


# Salam


@lepin_cmd(pattern="l(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Kalo Orang Salam Itu Dijawab...`")
    sleep(2)
    await typew.edit("`وَعَلَيْكُمْ السَّلاَمُ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ`")


# Menjawab Salam


@lepin_cmd(pattern="kenalin(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("☑️ `Kenzhu wibu`")
    sleep(2)
    await typew.edit("✅ `Kenzhu wibu`")
    sleep(1)
    await typew.edit("☑️ `Oura stres`")
    sleep(2)
    await typew.edit("✅ `Oura stres`")
    sleep(1)
    await typew.edit("☑️ `Lynx Gajelas`")
    sleep(2)
    await typew.edit("✅ `Lynx Gajelas`")
    sleep(1)
    await typew.edit("☑️ `Dappa Wibu Sangean`")
    sleep(2)
    await typew.edit("✅ `Dappa Wibu Sangean`")
    sleep(1)
    await typew.edit("☑️ `Ehan Autis`")
    sleep(2)
    await typew.edit("✅ `Ehan Autis`")
    sleep(1)
    await typew.edit(
        "`⚡ Cuma lepin Yang Paling Waras, Baik Hati, Dan Tidak Sombong :v`"
    )


# King Userbot Support


@lepin_cmd(pattern="istigfar(?: |$)(.*)")
async def perkenalan(event):
    event.pattern_match.group(1)
    await event.edit(f"`Heh Kamu Gaboleh Begitu...`")
    sleep(2)
    await event.edit("`اَسْتَغْفِرُاللهَ الْعَظِيْم`")


# Istigfar


@lepin_cmd(pattern="virtual(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**OOOO**")
    sleep(1.5)
    await typew.edit("**INI YANG VIRTUAL**")
    sleep(1.5)
    await typew.edit("**YANG KATANYA SAYANG BANGET**")
    sleep(1.5)
    await typew.edit("**TAPI TETEP AJA DI TINGGAL**")
    sleep(1.5)
    await typew.edit("**NI INGET**")
    sleep(1.5)
    await typew.edit("**TANGANNYA AJA GA BISA DI PEGANG**")
    sleep(1.5)
    await typew.edit("**APALAGI OMONGANNYA**")
    sleep(1.5)
    await typew.edit("**BHAHAHAHA**")
    sleep(1.5)
    await typew.edit("**KASIAN MANA MASIH MUDA**")


@lepin_cmd(pattern="perkenalkan(?: |$)(.*)")
async def perkenalan(event):
    event.pattern_match.group(1)
    await event.edit(f"`Hai Guys , Perkenalkan Nama Gw {DEFAULTUSER}`")
    sleep(2)
    await event.edit(f"`Gw Tinggal Di {WEATHER_DEFCITY}`")
    sleep(2)
    await event.edit("`Salam Kenal...`")
    sleep(2)
    await event.edit("`Udah Gitu Aja :v`")


# Perkenalan


CMD_HELP.update(
    {
        "gabut": f"**Modules** - `Gabut`\
        \n\n Cmd : `{cmd}l`\
        \nUsage : Untuk Menjawab Salam\
        \n\n Cmd : `{cmd}perkenalkan`\
        \nUsage : Memperkenalkan Diri\
        \n\n Cmd : `{cmd}virtual`\
        \nUsage : ngeledek orang yang virtual\
        \n\n Cmd : `{cmd}g`\
        \nUsage : Member Goblok\
        \n\n Cmd : `{cmd}kenalin`\
        \nUsage : Awokwok\
        \n\n Cmd : `{cmd}p`\
        \nUsage : Untuk Memberi Salam\
    "
    }
)
