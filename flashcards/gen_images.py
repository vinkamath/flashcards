import os
from include.texttoimage import textToImage
MAX_IMAGES = 5

output_dir = "generated_images"
current_dir = os.path.dirname(os.path.abspath(__file__))

image_cnt = 0
dalle3 = textToImage()
namelist_file = os.path.join(current_dir, 'flashcard.txt')

with open(namelist_file) as f:
    for line in f:
        line = line.strip()
        
        if not line:
            continue            
        if line.startswith('#'):
            category = line[1:].strip().lower().replace(" ", "_")
            continue
        else:
            object = line         
            filename = object.lower().replace(" ","_") + ".png"
            
            image_dir = os.path.join(output_dir, category)
            reject_dir = os.path.join(output_dir, "reject")
            if not os.path.exists(image_dir):
                os.makedirs(image_dir)
            if not os.path.exists(reject_dir):
                os.makedirs(reject_dir)
            filepath = os.path.join(image_dir, filename)

            if not os.path.exists(filepath):
                print(category + ": " + object) 
                prompt = object + " logo in original colors on a light background, flat image" 
                #res = t2i_pipe(prompt)            
                #res[0].save(filename, 'png')
                #res[0]
                dalle3.gen_image_from_prompt(category, object, prompt)

        image_cnt += 1
        if image_cnt >= MAX_IMAGES:
            break

                
