# -*- coding: utf-8 -*-
import os
import eyed3  # eyed3==0.8.0
from PIL import Image
from flask import url_for


def decode_to_gb18030(string):
    new_string = string.decode("gb18030")
    # print new_string
    return new_string


def scan_data(str_type, num):
    dir_static = os.path.join(os.path.abspath('.'), "static")
    dir_music = os.path.join(dir_static, "music", str_type)
    dir_images = os.path.join(dir_static, "images", str_type)
    dir_description = os.path.join(dir_static, "description", str_type)
    i = 0
    data = []
    while i + 1 <= num:
        data.append({"order": i + 1})
        file_name = "0" * (3 - len(str(i + 1))) + str(i + 1)
        # Process .txt
        with open(os.path.join(dir_description, file_name + ".txt"), "r") as f:
            song_name = f.readline().decode("gb18030")
            data[i]["songname"] = song_name
            # lines = f.readlines()
            # description = []
            # for line in lines:
            #     description
            description = map(decode_to_gb18030, f.readlines())
            # print description
            # data[i - 1]["description"] = "啊俄方额外"
            data[i]["description"] = "\n".join(description)
            data[i]["summary"] = ("\n".join(description))[0:60]
            if len(data[i]["description"]) > 60:
                data[i]["summary"] = ("\n".join(description))[0:60] + "..."
            else:
                data[i]["summary"] = data[i]["description"]
        # Process .jpg
        cover = Image.open(os.path.join(dir_images, file_name + ".jpg"))
        cover_width, cover_height = cover.size
        data[i]["coverpath"] = url_for('static', filename="images/" + str_type + "/" + file_name + ".jpg")
        data[i]["coverwidth"] = cover_width
        data[i]["coverheight"] = cover_height
        data[i]["coverformat"] = "JPG"
        # Process .mp3
        try:
            song = eyed3.load(os.path.join(dir_music, file_name + ".mp3"))
            data[i]["songlength"] = song.info.time_secs
            data[i]["songsamplefrequency"] = song.info.sample_freq
            data[i]["songbitrate"] = song.info.bit_rate[1]
            # print '\n'.join(['%s:%s' % item for item in song.info.__dict__.items()])
        except:
            data[i]["songlength"] = "Unknown"
            data[i]["songsamplefrequency"] = "Unknown"
            data[i]["songbitrate"] = "Unknown"
        finally:
            # data[i]["songpath"] = "music\\" + str_type + "\\" + file_name + ".mp3"
            data[i]["songpath"] = url_for('static', filename="music/" + str_type + "/" + file_name + ".mp3")
        i += 1
    # print data
    return data


# scan_data("a", 5)
