from PIL import Image


INPUT_FILE_1 = '../images/woman.png'
INPUT_FILE_2 = '../images/sunset.png'
OUTPUT_FILE = 'output.png'


def main():

    alpha = 0.3

    def transform():
        r1, g1, b1 = in_pix_1[x, y]
        r2, g2, b2 = in_pix_2[x, y]
        return (int(r1 * alpha + r2 * (1 - alpha)),
                int(g1 * alpha + g2 * (1 - alpha)),
                int(b1 * alpha + b2 * (1 - alpha)))

    with Image.open(INPUT_FILE_1) as img_file_1, \
         Image.open(INPUT_FILE_2) as img_file_2:
        in_img_1  = img_file_1.convert('RGB')
        in_img_2  = img_file_2.convert('RGB')
        assert in_img_1.size == in_img_2.size
        in_pix_1  = in_img_1.load()
        in_pix_2  = in_img_2.load()
        size    = in_img_1.size
        out_img = Image.new('RGB', size)
        out_pix = out_img.load()
        width, height = size
        for y in range(height):
            for x in range(width):
                out_pix[x, y] = transform()
        out_img.save(OUTPUT_FILE)


if __name__ == '__main__':
    main()
