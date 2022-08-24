# importing libs

import PIL.Image as pil
from PIL.ExifTags import TAGS


# finding metadata of the image
def findMetadata(img_path):
    img = pil.open(img_path)
    flag = 0
    res = ''
    try:
        info = img.getexif()
        flag=0
        for (tag, value) in info.items():
            if "Software" == TAGS.get(tag, tag):  # checking for software traces
                # print("Found Software Traces...")
                # print("Software Signature: ",value)
                flag = 1
                value.replace('(',' ')
                value.replace(')', ' ')
                res =res+ f"Found Software Traces...\nSoftware Signature: {value}\n"
                print(res)
        if flag == 0:
            res = res+"No Softare Signature Found. Seems like real image..."
            print(res)
            return res

    except Exception as e:
        res = res+f'Failed to load metadata, error : {e}'
        print(res)
        return res
    return res
