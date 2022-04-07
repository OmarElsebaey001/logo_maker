from operator import methodcaller
from flask import make_response,Flask,render_template
from flask import request, jsonify
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
from jinja2 import Template
from flask import send_file
from helper import generate_image_simple_mode
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
            lg_width  = request.args.get("logo_width",type=int)
            lg_height = request.args.get("logo_height",type=int)
            lg_margin = request.args.get("logo_margin",type=int)
            lg_text = request.args.get("logo_text",type=str)
            lg_txt_color = request.args.get("text_color",type=str)
            lg_bk_color = request.args.get("back_ground_color",type=str)
            lg_font_file = request.args.get("font_file",type=str)
            lg_font_size = request.args.get("font_size",type=int)
            
            lg_txt_color = lg_txt_color.strip()
            lg_bk_color = lg_bk_color.strip()
            
            generate_image_simple_mode(lg_width,lg_height,lg_margin,lg_text,
            lg_txt_color,lg_bk_color,lg_font_file,lg_font_size)

            return render_template("processed.html",
            logo_width=lg_width,logo_height=lg_height,logo_text=lg_text,
            logo_margin=lg_margin,text_color=lg_txt_color,
            back_ground_color=lg_bk_color,font_file=lg_font_file,
            font_size=lg_font_size,
            )
        return render_template("index.html")
    if __name__ == "__main__":
        app.run()
    return app 
