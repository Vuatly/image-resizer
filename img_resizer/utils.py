import shutil

import cv2
import requests
import imghdr

from .models import Image


def resize_image(obj_pk, new_width, new_height):
    """Изменяет размер изображения по ширине и высоте"""
    img_obj = Image.objects.get(pk=obj_pk)
    image = cv2.imread(img_obj.file.path)
    height, width = image.shape[:2]

    if not new_width:
        scaling_percent = int(new_height) / float(height)
        dim = (int(width * scaling_percent), int(new_height))
    elif not new_height:
        scaling_percent = int(new_width) / float(width)
        dim = (int(new_width), int(height * scaling_percent))
    else:
        dim = (int(new_width), int(new_height))

    resized_img = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
    cv2.imwrite(f'media/{img_obj.name}', resized_img)
    img_obj.resized = str(img_obj.name)
    img_obj.save()


def get_image_from_link(img_link):
    """Получает изображение по ссылке и возвращает путь до изображения"""
    filename = img_link.split('/')[-1]
    request = requests.get(img_link, stream=True)
    if request.status_code == 200:
        request.raw.decode_content = True
        save_path = f'media/{filename}'
        with open(save_path, 'wb') as file:
            shutil.copyfileobj(request.raw, file)
            if imghdr.what(save_path) is None:
                raise TypeError('Invalid image file type or broken image')
            return filename
