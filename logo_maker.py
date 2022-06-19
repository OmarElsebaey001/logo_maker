from script_helper import * 
import sys 
import pandas as pd 
input_file = sys.argv[1]
main_df = pd.read_csv(input_file)
for i in range(main_df.shape[0]):
    t     = main_df['text'][i]
    w     = main_df['width'][i]
    h     = main_df['height'][i]
    m     = main_df['margin'][i]
    f     = main_df['font_file'][i]
    bc    = main_df['back_color'][i]
    fc    = main_df['front_color'][i]
    bord  = main_df['border'][i]
    o     = main_df['output_name'][i] +'.png' 
    image = create_full_image(w,h,m,t,f,bc,fc,bord)
    image.save(o)
