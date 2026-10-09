from PIL import Image


INPUT_FILE = '../images/snake.png'
OUTPUT_FILE = 'output1.png'


def main():

    def transform():
        r, g, b = in_pix[x, y]
        avg = (r + g + b) // 3
        # avg = int(0.299 * r + 0.587 * g + 0.114 * b)
        return (avg, avg, avg)

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
