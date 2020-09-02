#Autor >> AlfonzCS
import fitz # PyMuPDF
import io
from PIL import Image

def ClownLogo():
    from colorama import init, Fore
    import sys, random, time
    init()
    clear = "\x1b[0m"
    colors = [36, 32, 34, 35, 31, 37]

    x = """

        ____  ____  ______   ______     __                  __                ____               
       / __ \/ __ \/ ____/  / ____/  __/ /__________ ______/ /_____  _____   /  _/___ ___  ____ _
      / /_/ / / / / /_     / __/ | |/_/ __/ ___/ __ `/ ___/ __/ __ \/ ___/   / // __ `__ \/ __ `/
     / ____/ /_/ / __/    / /____>  </ /_/ /  / /_/ / /__/ /_/ /_/ / /     _/ // / / / / / /_/ / 
    /_/   /_____/_/      /_____/_/|_|\__/_/   \__,_/\___/\__/\____/_/     /___/_/ /_/ /_/\__, /  
                                                                                    /____/   
        CS! : PDF Extractor Img es un script que extrae todas las imagenes de un (pdf).       
    """
    for N, line in enumerate(x.split("\n")):
         sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
         time.sleep(0.05)

ClownLogo()

try:
    pdf_file = sys.argv[1]
except:
    print('[x] Error')

try:
    # file path you want to extract images from
    file = pdf_file
    # open the file
    pdf_file = fitz.open(file)
    # iterate over PDF pages
    for page_index in range(len(pdf_file)):
        # get the page itself
        page = pdf_file[page_index]
        image_list = page.getImageList()
        # printing number of images found in this page
        if image_list:
            print(f"[+] Found a total of {len(image_list)} images in page {page_index}")
        else:
            print("[!] No images found on page", page_index)
        for image_index, img in enumerate(page.getImageList(), start=1):
            # get the XREF of the image
            xref = img[0]
            # extract the image bytes
            base_image = pdf_file.extractImage(xref)
            image_bytes = base_image["image"]
            # get the image extension
            image_ext = base_image["ext"]
            # load it to PIL
            image = Image.open(io.BytesIO(image_bytes))
            # save it to local disk
            image.save(open(f"image{page_index+1}_{image_index}.{image_ext}", "wb"))
except:
    print('[-] PDF no encontrado')
