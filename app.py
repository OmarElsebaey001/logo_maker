from operator import methodcaller
from tkinter import font
from flask import make_response,Flask,render_template
from flask import request, jsonify
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
from jinja2 import Template
from flask import send_file
from helper import *
import io 
from random import randint

def create_app() : 
    app = Flask(__name__)
    @app.route("/",methods=['GET','POST'])
    def show():
        if(request.method == "GET"):
            lg_text = request.args.get("logo_text")
            if ( lg_text == None) : 
                return render_template("index.html")
            lg_width     = request.args.get("logo_width",type=int)
            lg_height    = request.args.get("logo_height",type=int)
            lg_margin    = request.args.get("logo_margin",type=int)
            lg_text      = request.args.get("logo_text",type=str)
            lg_txt_color = request.args.get("text_color",type=str)
            lg_bk_color  = request.args.get("back_ground_color",type=str)
            lg_font_file = request.args.get("font_file",type=str)
            
            lg_txt_color = lg_txt_color.strip()
            lg_text      = lg_text.strip()
            lg_bk_color  = lg_bk_color.strip()
            
            usable_per = (100-lg_margin)/100
            
            usable_w   = usable_per*lg_width
            usable_h   = usable_per*lg_height
            print("Usable: H" , usable_h)
            print("Usable: W" , usable_w)
            
            font_file  = lg_font_file
            font_size  = get_max_font(usable_w,usable_h,font_file,lg_text)
            print("Max Font size: " , font_size)
            img = generate_image_simple_mode(lg_width,lg_height,lg_text,lg_txt_color,lg_bk_color,font_file,font_size)
            print(img.size)
            img.save("static/processed_image.png")

            return render_template("processed.html",
            logo_width=lg_width,logo_height=lg_height,logo_text=lg_text,
            logo_margin=lg_margin,text_color=lg_txt_color,
            back_ground_color=lg_bk_color,font_file=lg_font_file)

        return render_template("index.html")
    if __name__ == "__main__":
        app.run()
    return app