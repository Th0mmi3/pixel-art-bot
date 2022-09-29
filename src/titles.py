import random

prompts = []
title_format_list = []

# Get Prompts
with open("prompts.txt", 'r') as pts:
    for line in pts.readlines():
        prompts.append(line.strip())

# Get title formats
with open("titles.txt", 'r') as titles:
    for line in titles.readlines():
        title_format_list.append(line.strip())

class titler:
    def create(self, vid_path):
        title = ""
        subject = ""
        title_format = random.choice(title_format_list)

        for prompt in prompts:
            if prompt in vid_path:
                subject = prompt
                print(subject + " " + prompt + " " + vid_path)

        subject_index = title_format.find("<>")

        title = title_format[:subject_index] + subject.capitalize() + title_format[subject_index:]
        title = title.replace('<>', '')

        title = title.replace('[]', '\U0001F60D ')

        return(title)

#title = titler()
#title.create("C:\\Progr\\pixelArt\\src\\upload\\cow-000005final.mp4")


        