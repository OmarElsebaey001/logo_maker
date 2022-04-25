from PIL import Image, ImageDraw, ImageFont


def get_max_font(w, h, font_file, text):
    usable_font = 0 
    i = 1
    while True:
        font = ImageFont.truetype(font_file, i)
        text_size = get_text_size_from_font(text,font)
        if (text_size[0] < w) and (text_size[1] < h):
            usable_font = i 
        else:
            print("Breaking with size: ", text_size)
            print("Breaking with font: ", usable_font)
            break 
        i += 1 
    return usable_font 


def generate_image_simple_mode(w, h, txt, txt_color, background_color, font_file, size):
    print("Writing in usable: " , w , h )
    font = ImageFont.truetype(font_file, size)
    t_h = font.getsize(txt)[1]
    im = Image.new("RGB", (w, h), background_color)
    d = ImageDraw.Draw(im)
    w_shift = w/2 
    h_shift = (h)/2
    #h_shift = (h+t_h/4)/2
    
    print("Shifting: " , w_shift)
    print("Shifting: " , h_shift)
    d.text((w_shift, h_shift), txt , fill=txt_color, font=font, anchor="mm")
    return im 


def create_full_image(lg_width, lg_height, margin, lg_text, font_file, lg_txt_color, lg_bk_color):
    lg_text = lg_text.replace("<br>","\n")
    usable_per = (100-margin)/100
    usable_w = int(usable_per*lg_width)
    usable_h = int(usable_per*lg_height)
    font_size = get_max_font(usable_w, usable_h, font_file, lg_text)
    img = generate_image_simple_mode(lg_width, lg_height, lg_text, lg_txt_color, lg_bk_color, font_file, font_size)
    return img


def get_text_size_from_font(text,fnt):

    im = Image.new(mode="RGB", size=(1,1))
    draw = ImageDraw.Draw(im)
    if("\n" in text):
        size = draw.multiline_textsize(text, font=fnt)
    else:
        size = draw.textsize(text, font=fnt)
    return size