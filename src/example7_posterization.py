from PIL import Image


INPUT_FILE = '../images/woman.png'
OUTPUT_FILE = 'output.png'


def main():

    def transform():
        r, g, b = in_pix[x, y]
        avg = (r + g + b) // 3
        if avg < 50:
            return (120, 41, 15)   # Brandy
        elif avg < 130:
            return (255, 125, 0)   # Harvest Orange
        else:
            return (255, 236, 209) # Papaya Whip

    with Image.open(INPUT_FILE) as img_file:
        in_img  = img_file.convert('RGB')
        in_pix  = in_img.load()
        size    = in_img.size
        out_img = Image.new('RGB', size)
        out_pix = out_img.load()
        width, height = size
        for y in range(height):
            for x in range(width):
                out_pix[x, y] = transform()
        out_img.save(OUTPUT_FILE)


if __name__ == '__main__':
    main()
