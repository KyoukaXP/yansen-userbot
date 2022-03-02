# Thanks Full To Team Ultroid
# Fiks By Kyy @IDnyaKosong


from telethon.tl import types
from telethon.tl.functions.channels import GetFullChannelRequest as getchat
from telethon.tl.functions.phone import CreateGroupCallRequest as startvc
from telethon.tl.functions.phone import DiscardGroupCallRequest as stopvc
from telethon.tl.functions.phone import GetGroupCallRequest as getvc
from telethon.tl.functions.phone import InviteToGroupCallRequest as invitetovc
from telethon.utils import get_display_name

from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP
from userbot.utils import lepin_cmd

NO_ADMIN = "`Maaf Kamu Bukan Admin 👮`"


def vcmention(user):
    full_name = get_display_name(user)
    if not isinstance(user, types.User):
        return full_name
    return f"[{full_name}](tg://user?id={user.id})"


async def get_call(lepin):
    lepin = await lepin.client(getchat(lepin.chat_id))
    await lepin.client(getvc(lepin.full_chat.call, limit=1))
    return hehe.call


def user_list(l, n):
    for i in range(0, len(l), n):
        yield l[i : i + n]


@lepin_cmd(pattern="startvc$")
async def start_voice(c):
    chat = await c.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    if not admin and not creator:
        await c.edit(f"**Maaf {ALIVE_NAME} Bukan Admin 👮**")
        return
    try:
        await c.client(startvc(c.chat_id))
        await c.edit("`Memulai Obrolan Suara`")
    except Exception as ex:
        await c.edit(f"**ERROR:** `{ex}`")


@lepin_cmd(pattern="stopvc$")
async def stop_voice(c):
    chat = await c.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    if not admin and not creator:
        await c.edit(f"**Maaf {ALIVE_NAME} Bukan Admin 👮**")
        return
    try:
        await c.client(stopvc(await get_call(c)))
        await c.edit("`Mematikan Obrolan Suara`")
    except Exception as ex:
        await c.edit(f"**ERROR:** `{ex}`")


@lepin_cmd(pattern="vcinvite")
async def _(lepin):
    await lepin.edit("`Sedang Menginvite Member...`")
    users = []
    z = 0
    async for x in lepin.client.iter_participants(kyy.chat_id):
        if not x.bot:
            users.append(x.id)
    hmm = list(user_list(users, 6))
    for p in hmm:
        try:
            await lepin.client(invitetovc(call=await get_call(kyy), users=p))
            z += 6
        except BaseException:
            pass
    await lepin.edit(f"`Menginvite {z} Member`")


CMD_HELP.update(
    {
        "vcg": f"𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}startvc`\
         \n↳ : Memulai Obrolan Suara dalam Group.\
         \n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}stopvc`\
         \n↳ : `Menghentikan Obrolan Suara Pada Group.`\
         \n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}vcinvite`\
         \n↳ : Invite semua member yang berada di group."
    }
)
