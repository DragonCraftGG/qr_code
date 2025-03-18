import qrcode

def generate_youtube_qr(url):
    # Проверяем, что ссылка ведет на YouTube
    if "youtube.com" not in url and "youtu.be" not in url:
        print("Ошибка: Ссылка должна быть с YouTube.")
        return

    # Создаем QR-код
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=2,
        border=2,
    )
    qr.add_data(url)
    qr.make(fit=True)

    # Выводим QR-код в виде ASCII-арта
    qr_ascii = qr.get_matrix()
    for row in qr_ascii:
        print("".join(["██" if cell else "  " for cell in row]))

if __name__ == "__main__":
    # Запрашиваем ссылку у пользователя
    youtube_url = input("Введите ссылку на YouTube видео: ")
    generate_youtube_qr(youtube_url)