from PIL import Image, ImageEnhance

class generator:
    def __init__(self, _base, _brightness):
        self.base = _base
        self.brightness = _brightness

        self.maxSize = 950, 950
        self.width = 1080
        self.height = 1920
        self.size = 1080, 1920

    def generate(self, img):
        combImg = Image.new("RGBA", self.size)
        combImg.paste(self.base)

        img.thumbnail(self.maxSize, Image.ANTIALIAS)
        width, height = img.size

        img = ImageEnhance.Brightness(img).enhance(self.brightness)

        combImg.paste(img, (
            round((1080 - width) / 2),
            round(1920 / 2) - round(height / 2)
        ))

        
        return combImg

