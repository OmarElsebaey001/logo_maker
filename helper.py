from PIL import Image, ImageDraw, ImageFont
def generate_image_simple_mode(w,h,txt,txt_color,bkground_color,font_file,size):
    font = ImageFont.truetype(font_file, size)
    im = Image.new("RGB", (w,h), bkground_color)
    d  = ImageDraw.Draw(im)
    d.text((w/2, h/2), txt , fill=txt_color, font=font, anchor="mm")
    return im 
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