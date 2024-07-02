import qrcode
from PIL import Image


def generation_qrCode(data):
    """
    Generate a QR code image from the provided data.

    :return: PIL.Image.Image: Generated QR code image in RGBA mode.
    """
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="black", back_color="white").convert('RGBA')
    return qr_img


def dimentionnement_logo(qr_img, logo) -> tuple:
    """
    Compute and adjust the size of the logo to fit within the QR code.

    :param qr_img : QR code image.
    :param logo : Logo image.

    :return:tuple: Resized logo, size of the logo, and bounding box of the QR code.
    """
    qr_box = qr_img.getbbox()
    logo_size = min(qr_box[2], qr_box[3]) // 3
    logo = logo.resize((logo_size, logo_size))
    return logo, logo_size, qr_box


def supression_fond(qr_img):
    """
    Remove the white background from the QR code image, making it transparent.
    :param qr_img: QR code image.
    :return: PIL.Image.Image: QR code image with a transparent background.
    """
    datas = qr_img.getdata()
    new_datas = []
    for item in datas:
        # change all white (also shades of whites)
        # pixels to transparent
        if item[0] > 220 and item[1] > 220 and item[2] > 220:
            new_datas.append((255, 255, 255, 0))
        else:
            new_datas.append(item)

    qr_img.putdata(new_datas)
    return qr_img


def placement_logo_in_Qr(logo, qr_img, logo_size:int, qr_box :tuple):
    """
    Place the logo at the center of the QR code.

    :param logo (PIL.Image.Image): Logo image.
    :param qr_img (PIL.Image.Image): QR code image.
    :param logo_size (int): Size of the logo.
    :param qr_box (tuple): Bounding box of the QR code.

    :return: PIL.Image.Image: QR code image with the logo placed at the center.
    """
    position = ((qr_box[2] - logo_size) // 2, (qr_box[3] - logo_size) // 2)
    qr_img.paste(logo, position, logo)
    return qr_img


def generate_qrcode_with_logo(data, logo_path, output_path):
    """
        Just the main execution to build your QR code
    :param data: Url
    :param logo_path: path of your logo
    :param output_path: name of your new QR Code
    :return:
    """
    # Générer le QR code
    qr_img = generation_qrCode(data)

    # Ouvrir le logo
    logo = Image.open(logo_path)

    # Convertir le logo en RGBA s'il est en RGB
    if logo.mode == 'RGB':
        r, g, b = logo.split()
        alpha = Image.new('L', logo.size, 255)  # Crée un canal alpha (complètement opaque)
        logo.putalpha(alpha)  # Ajoute le canal alpha au logo

    # Calculer les dimensions pour le logo
    logo, logo_size, qr_box = dimentionnement_logo(qr_img, logo)

    # Coller le logo au centre du QR code
    qr_img = placement_logo_in_Qr(logo, qr_img, logo_size, qr_box)

    # Supprimer le fond du QR code
    qr_img = supression_fond(qr_img)

    # Enregistrer le résultat
    qr_img.save(output_path)

if __name__ == "__main__":
    data = "https://www.root-me.org/Hychion_"
    logo_path = "img_3.png"
    output_path = "new_qrcode.png"
    generate_qrcode_with_logo(data, logo_path, output_path)
