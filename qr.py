import qrcode
from pathlib import Path

QR_CODES = {
    "burger_2019": "https://doi.org/10.1145/3297663.3309670",
    "wiedner_2022": "https://doi.org/10.1109/INFOCOMWKSHPS54753.2022.9798351",
    "handigol_2012": "https://doi.org/10.1145/2413176.2413206",
    "bachelor": "https://github.com/Lars0300/Bachelor"
}

OUT_DIR = Path("qr_codes")
OUT_DIR.mkdir(exist_ok=True)

for name, url in QR_CODES.items():
    qr = qrcode.QRCode(
        version=2,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=2,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(OUT_DIR / f"{name}.png")

print(f"Created {len(QR_CODES)} QR codes in {OUT_DIR}/")