# Using Python Slim-Buster
FROM kyyex/kyy-userbot:busterv2
#━━━━━ Userbot Telegram ━━━━━
#━━━━━ By Yansen-Userbot ━━━━━

RUN apt-get update && apt-get upgrade -y
RUN apt-get install ffmpeg -y
RUN git clone -b Yansen-Userbot https://github.com/Yansensad/yansen-userbot /root/userbot
RUN mkdir /root/userbot/.bin
RUN pip install --upgrade pip setuptools
WORKDIR /root/userbot

#Install python requirements
RUN pip3 install -r https://raw.githubusercontent.com/Yansensad/yansen-userbot/Yansen-Userbot/requirements.txt

EXPOSE 80 443

# Finalization
CMD ["python3", "-m", "userbot"]
