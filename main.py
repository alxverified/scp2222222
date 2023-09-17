import logging
from os import getenv
from dotenv import load_dotenv
from huepy import red
from telethon import TelegramClient, events
from funcs import get_cc, get_bin

load_dotenv()

API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

client = TelegramClient("scrapp", API_ID, API_HASH)

# You can add chats here as long as your telegram account is in it
chats = [
"@secretgroup01",
"@ScrapperLala",
"https://t.me/+rl8ChsLqzBdkNTYx",
"@TechzillaChkChat",
"@kurumichat",
"@ChatA2Assiad",
"@Venexchk",
"@JohnnySinsChat",
"@leonbinerss",
"@RemChatChk",
"@alterchkchat",
"@AssociatonBinners1",
"@dSnowChat",
"@cardesclubchat",
"@BinsHellChat",
"@BinSkillerChat",
"@RickPrimeChkFree",
"@savagegroupoficial",
"@CHECKEREstefany_bot",
"@GodsOfTheBins",
"@CuartelCardingGrupo",
"@botsakuraa",
"@ArthurChkGroup",
"@SkadiScrapper",
"@CCAUTH",
"@Ikaroscrapper"
]

# Chat to send ccs
send_chat = "@KarolGScrapper"
ccs_ac = []

PHOTO_PATH = "kg.jpg"

@client.on(events.NewMessage(chats=chats))
async def scrapper(e: events.NewMessage.Event):
    text = e.message.message
    ccs = get_cc(text)
    if not ccs:
        return

    cc = ccs[0]
    mes = ccs[1]
    ano = ccs[2]
    cvv = ccs[3]
    ccf = f"{cc}|{mes}|{ano}|{cvv}"

    if ccf in ccs_ac:
        return

    print(red(f"CC FIND: {ccf}"))

    # File where the ccs are stored
    with open("ccs.txt", "a") as f:
        f.write(ccf + "\n")

    ccs_ac.append(ccf)
    bin = cc[:6]
    extra = f"{cc[:12]}xxxx|{mes}|{ano}|rnd"
    bin_data = await get_bin(bin)

    if isinstance(bin_data, bool):
        return

    if len(mes) == 1:
        mes = "0" + mes

    if len(ano) == 2:
        ano = "20" + ano

    brand = bin_data["brand"]
    country = bin_data["country"]
    country_flag = bin_data["country_flag"]
    bank = bin_data["bank"]
    level = bin_data["level"]
    card_type = bin_data["type"]

    text_final = f""" 
    ♪ 𝙇𝙖 𝘽𝙞𝙘𝙝𝙤𝙩𝙖 𝙎𝙘𝙧𝙖𝙥𝙥𝙚𝙧 ♔
*ੈ✩‧₊˚*ੈ✩‧₊˚*ੈ✩‧₊˚*ੈ✩‧₊˚*ੈ✩‧₊˚*ੈ✩‧₊˚
    𝖈𝖆𝖗𝖉: <code>{ccf}</code>
    𝖇𝖆𝖓𝖐:  <b> {bank} </b>
    𝖎𝖓𝖋𝖔: <b> {brand} - {card_type} - {level} </b>
    𝕮𝖔𝖚𝖓𝖙𝖗𝖞: <b> {country} - {country_flag} </b>
*ੈ✩‧₊˚*ੈ✩‧₊˚*ੈ✩‧₊˚*ੈ✩‧₊˚*ੈ✩‧₊˚*ੈ✩‧₊˚
    𝕰𝖝𝖙𝖗𝖆: <code>{extra}</code>
    𝖉𝖊𝖛: @XYZAustin
    """

    await client.send_file(send_chat, PHOTO_PATH, caption=text_final, parse_mode="html")


if __name__ == "__main__":
    logging.basicConfig(
        format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s",
        level=logging.WARNING,
    )
    client.start()
    client.run_until_disconnected()
