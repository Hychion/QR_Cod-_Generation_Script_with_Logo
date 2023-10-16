#Guide for Using the QR Code Generation Script with Embedded Logo

##Description:


##Main Functions:

generation_qrCode(): This function generates the QR code from the provided data.
dimentionnement_logo(qr_img, logo): Computes and adjusts the size of the logo to fit well within the QR code.
supression_fond(qr_img): Removes the white background from the QR code image, making it transparent. This function is currently commented out and not in use.
placement_logo_in_Qr(logo, qr_img, logo_size, qr_box): Places the logo at the center of the QR code.
generate_qrcode_with_logo(data, logo_path, output_path): The main function that coordinates all steps for generating the QR code with the logo.

##How to Use the Script:

###Ensure you have installed the necessary libraries with
pip install qrcode[pil] Pillow

###Modify the values of the variables in the if __name__ == "__main__": section as per your requirements:

data: The URL or data you wish to encode in the QR code.
logo_path: The path to your logo. It's currently set to "img_3.png".
output_path: The path where you wish to save the final QR code. It's currently set to "qrcode_rootme.png".
Run the script. Upon execution, you'll find the generated QR code with the logo at the location specified by output_path

##Notes:

The function supression_fond(qr_img) that removes the white background from the QR code image is currently commented out. If you wish to make the background of the QR code transparent, uncomment the line #qr_img = supression_fond(qr_img).
The script supports logos that are in "RGB" or "RGBA" mode. If the logo is in "RGB", an alpha (transparency) channel will be added automatically.


[FR]
#Guide d'utilisation du script de génération de QR code avec un logo

##Description:

This Python script is designed to generate a QR code from a given URL and embed a logo at its center. The logo retains its original colors, and the QR code is generated with a white background and black patterns.

##Fonctions principales :

generation_qrCode(): Cette fonction génère le QR code à partir des données fournies.
dimentionnement_logo(qr_img, logo): Calcule et ajuste la taille du logo pour qu'il s'adapte bien à l'intérieur du QR code.
supression_fond(qr_img): Supprime le fond blanc de l'image du QR code, le rendant transparent. Cette fonction est actuellement commentée et n'est pas utilisée.
placement_logo_in_Qr(logo, qr_img, logo_size, qr_box): Place le logo au centre du QR code.
generate_qrcode_with_logo(data, logo_path, output_path): Fonction principale qui coordonne toutes les étapes de la génération du QR code avec le logo.


##Fonctions principales :

generation_qrCode(): Cette fonction génère le QR code à partir des données fournies.
dimentionnement_logo(qr_img, logo): Calcule et ajuste la taille du logo pour qu'il s'adapte bien à l'intérieur du QR code.
supression_fond(qr_img): Supprime le fond blanc de l'image du QR code, le rendant transparent. Cette fonction est actuellement commentée et n'est pas utilisée.
placement_logo_in_Qr(logo, qr_img, logo_size, qr_box): Place le logo au centre du QR code.
generate_qrcode_with_logo(data, logo_path, output_path): Fonction principale qui coordonne toutes les étapes de la génération du QR code avec le logo.

##Comment utiliser le script :

###Assurez-vous d'avoir installé les bibliothèques nécessaires avec :

pip install qrcode[pil] Pillow Pillow

###Modifiez les valeurs des variables dans la section if __name__ == "__main__": selon vos besoins :

data: L'URL ou les données que vous souhaitez encoder dans le QR code.
logo_path: Le chemin d'accès de votre logo. Actuellement, il est défini sur "img_3.png".
output_path: Le chemin d'accès où vous souhaitez enregistrer le QR code final. Actuellement, il est défini sur "qrcode_rootme.png".
Exécutez le script. Après l'exécution, vous trouverez le QR code généré avec le logo à l'emplacement spécifié par output_path.


##Remarques :

La fonction supression_fond(qr_img) qui supprime le fond blanc de l'image du QR code est actuellement commentée. Si vous souhaitez rendre le fond du QR code transparent, décommentez la ligne #qr_img = supression_fond(qr_img).
Le script prend en charge les logos qui sont en mode "RGB" ou "RGBA". Si le logo est en "RGB", un canal alpha (transparence) sera ajouté automatiquement.

