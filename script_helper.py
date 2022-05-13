from PIL import Image, ImageDraw, ImageFont
from PIL import Image, ImageOps , ImageColor
import numpy as np

def get_max_font(w, h, font_file, text):
    usable_font = 0 
    i = 1
    while True:
        font = ImageFont.truetype(font_file, i)
        text_size = get_text_size_from_font(text,font)
        if (text_size[0] < w) and (text_size[1] < h):
            usable_font = i 
        else:
            break 
        i += 1 
    return usable_font 


def generate_image_simple_mode(w, h, txt, txt_color, background_color, font_file, size):
    font = ImageFont.truetype(font_file, size)
    t_h = font.getsize(txt)[1]
    im = Image.new("RGB", (w, h), background_color)
    d = ImageDraw.Draw(im)
    w_shift = w/2 
    h_shift = (h)/2    
    d.text((w_shift, h_shift), txt , fill=txt_color, font=font, anchor="mm")
    return im 

def generate_image_multi_mode(w, h, txt, txt_color, background_color, font_file, size,align):
    font = ImageFont.truetype(font_file, size)
    t_h = font.getsize(txt)[1]
    im = Image.new("RGB", (w, h), background_color)
    d = ImageDraw.Draw(im)
    w_shift = w/2 
    h_shift = (h)/2    

    d.text((w_shift, h_shift), txt , fill=txt_color, font=font, anchor="mm", align=align)
    return im 

def create_full_image(lg_width, lg_height, margin, lg_text, font_file, lg_txt_color, lg_bk_color,lg_border):
    multi_line = True if ("<brc>" in lg_text or "<brc>" in lg_text ) else False
    align      = "left" if "<brl>" in lg_text else "center"
    lg_text    = lg_text.replace("<brc>","\n")
    lg_text    = lg_text.replace("<brl>","\n")
    usable_per = (100-margin)/100
    usable_w   = int(usable_per*lg_width)
    usable_h   = int(usable_per*lg_height)
    font_size  = get_max_font(usable_w, usable_h, font_file, lg_text)
    if (not multi_line):
        img        = generate_image_simple_mode(lg_width, lg_height, lg_text, lg_txt_color, lg_bk_color, font_file, font_size)
    else:
        img        = generate_image_multi_mode(lg_width, lg_height, lg_text, lg_txt_color, lg_bk_color, font_file, font_size,align)
    before, after = get_before_and_after_counts(img,lg_bk_color)
    img        = adjust_image(img,before,after,lg_bk_color)
    img        = add_border_to_image(img,lg_border,'black')
    return img

def add_border_to_image(img,thick,color):
    return ImageOps.expand(img,border=thick,fill=color)

def get_text_size_from_font(text,fnt):
    im = Image.new(mode="RGB", size=(1,1))
    draw = ImageDraw.Draw(im)
    if("\n" in text):
        size = draw.multiline_textsize(text, font=fnt)
    else:
        size = draw.textsize(text, font=fnt)
    return size
def add_row_at_n(im,n,color):
    arr = np.array(im)
    l = [color for i in range(arr.shape[1])]
    row = np.array([l])
    arr = np.insert(arr,n,[l],axis= 0)
    return Image.fromarray(arr,'RGB')
def delete_row_at_n(im,n):
    arr = np.array(im)
    arr = np.delete(arr, n, 0)
    return Image.fromarray(arr,'RGB')

def get_before_and_after_counts(im, color) : 
    color = list(ImageColor.getcolor( color, "RGB"))
    arr  = np.array(im)
    rows = arr.shape[0]
    cols = arr.shape[1]
    alist = []
    for i in range(rows) :
        white_counter = 0
        for j in range(cols):
            p = arr[i][j]
            comparison = p == np.array(color)
            equal_arrays = comparison.all()
            if(equal_arrays):
                white_counter += 1
        alist.append(white_counter)
    m = cols
    before = 0 
    for i in alist:
        if (i==m):
            before +=1
        else:
            break
    alist.reverse()
    after = 0 
    for i in alist:
        if (i==m):
            after +=1
        else:
            break
    return before,after

def adjust_image(im,before,after,color):
    color = list(ImageColor.getcolor( color, "RGB"))
    diff = (before - after)
    if (abs(diff) not in  [0,1] ) : 
        shift = int((diff-1)/2)
        first = -1 
        second = 0
        if (shift < 0 ) : 
            first  = 0
            second = -1
        for i in range((abs(shift))):
            im = add_row_at_n(im,first,color)
            im = delete_row_at_n(im,second)
    return im 