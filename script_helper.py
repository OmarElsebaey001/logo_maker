from PIL import Image, ImageDraw, ImageFont
import pandas as pd 
import sys

def get_max_font(w,h,font_file,text):
    usable_font = 0 
    i = 1 
    while(True):
        font = ImageFont.truetype(font_file, i)
        text_size = font.getsize(text)
        if (text_size[0] < w and text_size[1] < h ) : 
            usable_font = i 
        else:
            break 
        i += 1 
    return usable_font 


def generate_image_simple_mode(w,h,txt,txt_color,bkground_color,font_file,size):
    font = ImageFont.truetype(font_file, size)
    im = Image.new("RGB", (w,h), bkground_color)
    d  = ImageDraw.Draw(im)
    d.text((w/2, h/2), txt , fill=txt_color, font=font, anchor="mm")
    return im 


def create_full_image(lg_width,lg_height,margin,lg_text,font_file,lg_txt_color,lg_bk_color):
    usable_per = (100-margin)/100
    usable_w   = usable_per*lg_width
    usable_h   = usable_per*lg_height
    font_size  = get_max_font(usable_w,usable_h,font_file,lg_text)
    img = generate_image_simple_mode(lg_width,lg_height,lg_text,lg_txt_color,lg_bk_color,font_file,font_size)
    return img