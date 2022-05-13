from operator import methodcaller
from tkinter import font
from flask import make_response,Flask,render_template
from flask import request, jsonify
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
from jinja2 import Template
from flask import send_file
from script_helper import *
import io 
import  random 

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
        lg_border    = 2 
        lg_txt_color = lg_txt_color.strip()
        lg_text      = lg_text.strip()
        lg_bk_color  = lg_bk_color.strip()
        usable_per = (100-lg_margin)/100
        
        usable_w   = usable_per*lg_width
        usable_h   = usable_per*lg_height
        
        font_file  = lg_font_file
        
        img        = create_full_image(lg_width,lg_height,lg_margin,lg_text,font_file,lg_txt_color,lg_bk_color,lg_border)
        img_path      = f"static/p_{random.randint(0,2200000)}.jpg"
        img.save(img_path,dpi=(600,600))

        return render_template("processed.html",
        logo_width=lg_width,logo_height=lg_height,logo_text=lg_text,
        logo_margin=lg_margin,text_color=lg_txt_color,
        back_ground_color=lg_bk_color,font_file=lg_font_file,img_path=img_path)

    return render_template("index.html")
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080)
