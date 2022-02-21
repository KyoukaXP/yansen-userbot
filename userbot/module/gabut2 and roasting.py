# ReCode by @yansesad
# FROM yansen-userbot <https://github.com/Yansesad/yansen-userbot>
# KONTOLLLLLLL

from platform import uname
from userbot import ALIVE_NAME, CMD_HELP, WEATHER_DEFCITY
from userbot.events import register

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern=r"^\.galau(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit(
       "**HAY KAMU GALAU YA? JANGAN GALAU LAGI YA SEMANGAT KONTOL**")


@register(outgoing=True, pattern="^\.prenjon(?: |$)(.*)")
async def typewritter(typew):
    typew.pattern_match.group(1)
    await typew.edit(
       "**HAHAHA KASIAN UDAH PRENJON GAMON LAGI DARI PADA GAMONIN DIA MENDING JADIAN SAMA AKU DI JAMIN BAHAGIA HEHE.**")

@register(outgoing=True, pattern="^\.sikntl(?: |$)(.*)")
async def typewriter(typew):
   typew.pattern_match.group(1)
   await typew.edit(
       "**KONTOL BUAT KAMU YANG UDAH DI JAGA TAPI MALAH DIA YANG KAMU BANGGAIN, INTINYA KAMU KONTOL**")


@register(outgoing=True, pattern="^\.badut(?: |$)(.*)")
async def typewriter(typew):
   typew.pattern_match.group(1)
   await typew.edit(
      "**KAMU GALAU YA? YAUDA SEBENTAR AKU PAKE TOPENG BADUT AKU DULU. NAH UDAH, YUK CERITA KAMU KENAPA**")

@register(outgoing=True, pattern="^\.roas1(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit(
       "**YAILAH BADUT BADUT AMPAS KAYA LO MAU LAWAN GUE? KALO MAU NGELUCU JANGAN DI DEPAN GUE BEGO. GA PANTES SEORANG BADUT NGELAWAN PESULAP YANG MENJADI TUHANNYA PARA BADUT, BUAT LO NI BADUT CECUNGUK BAU TAI MENDING MAIN CIRCUS AJA GAUSA MAIN TELE ROASTINGAN KO KAYA ROASTINGAN TAHUN MAJAPAHIT YANG KUNO GITU. UDAH BIKIN ROASTINGAN DI ULANG ULANH CERITANYA OTAK LO KERJANYA LAMBAT YA JADI GABISA BERFIKIR KATA KATA SENDIRI, KASIAN ORTU LO NYEKOLAHIN LO SAMPE JUAL DIRI GATAUNYA LO BEGO JADI BABU TELE YANG NYARI VCS GRATIS.**")

@register(outgoing=True, pattern="^\.roas2(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit(
       "**UDAH SEGITU DOANG KOSA KATA LO YANG GAADA BOBOT ITU? UDAH? HAHAHA GAADA RASA TOLOL KALO BUAT KOSA KATA YAMG BERBOBOT DIKIT APA, BIAR GA KELIATAN TOLOLNYA ELO ITU. APA PERLU LO GUE KASIH LUDAH GUE YANG SUCI INI SUPAYA DIRI LO YANG HINA ITU JADI SUCI? CIUM DULU SINI KAKI GUE BIAR BABI KAYA LO DAPET LUDAH GUE DAN JADI SUCI LAGI GA HINA BEGITU. SEKOLAH DULU YANG BENER DECK BARU LAWAN GUE YANG DEWA, BALIK LAGI KALO LEVEL LO UDEH JADI DEWA YA ADICK BIAR GA MALU LAWAN GUE**")


CMD_HELP.update(
    {
            "gabut2": "**modules** - `gabut2 and roasting`\
            \n\n cmd : `.galau`\
            \nUsage : Lihat Sendiri\
            \n\n cmd : `.prenjon`\
            \nUsage : Lihat Sendiri\
            \n\n cmd : `.badut`\
            \nUsage : Lihat Sendiri\
            \n\n cmd : `.roas1`\
            \nUsage : Lihat Sendiri\
            \n\n cmd : `.roas2`\
            \nUsage : Lihat Sendiri\
    "
     }
)
