from PIL import Image


INPUT_FILE = '../images/woman.png'
OUTPUT_FILE = 'output.png'


def main():

    def transform():
        r, g, b = in_pix[x, y]
        return (r, g, b)

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
