import qrcode
from PIL import Image


def dimentionnement_logo(qr_img,logo):
    qr_box = qr_img.getbbox()
    logo_size = min(qr_box[2], qr_box[3]) // 3
    logo = logo.resize((logo_size, logo_size))
    return logo , logo_size ,qr_box

def supression_fond(qr_img):
    datas = qr_img.getdata()

    new_datas = []
    for item in datas:
        # change all white (also shades of whites)
        # pixels to transparent
        if item[0] > 220 and item[1] > 220 and item[2] > 220:
            new_datas.append((255, 255, 255, 0))
        else:
            new_datas.append(item)

    return qr_img.putdata(new_datas)


def placement_logo_in_Qr(logo,qr_img,logo_size,qr_box):
    position = ((qr_box[2] - logo_size) // 2, (qr_box[3] - logo_size) // 2)
    qr_img.paste(logo, position, logo)
    return qr_img


def generation_qrCode():
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

def generate_qrcode_with_logo(data, logo_path, output_path):
    # Générer le QR code
    qr_img = generation_qrCode()

    # Ouvrir le logo
    logo = Image.open(logo_path)

    # Convertir le logo en RGBA s'il est en RGB
    if logo.mode == 'RGB':
        r, g, b = logo.split()
        alpha = Image.new('L', logo.size, 255)  # Crée un canal alpha (complètement opaque)
        logo.putalpha(alpha)  # Ajoute le canal alpha au logo

    # Calculer les dimensions pour le logo
    logo, logo_size,qr_box = dimentionnement_logo(qr_img, logo)

    # Coller le logo au centre du QR code

    qr_img = placement_logo_in_Qr(logo,qr_img,logo_size,qr_box)

    #qr_img = supression_fond(qr_img)

    # Enregistrer le résultat
    qr_img.save(output_path)


if __name__ == "__main__":
    data = "https://www.linkedin.com/in/quentin-libert-1596a2214/"
    logo_path = "img_3.png"
    output_path = "qrcode_rootme.png"
    generate_qrcode_with_logo(data, logo_path, output_path)



