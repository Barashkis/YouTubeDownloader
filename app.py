import sys

import yt_dlp


def get_info(url):
    try:
        options = {
            "simulate": True,
            "quiet": True
        }
        video = yt_dlp.YoutubeDL(options)
        video_data_json = video.extract_info(url)
    except Exception:
        return "Пожалуйста, проверьте URL!"

    title = video_data_json["title"]
    formats = video_data_json["formats"]

    available_formats = {}
    count = 0
    for format in formats:
        if format["vcodec"] != "none" and format["acodec"] != "none" and format["video_ext"] == "mp4":
            count += 1
            available_formats[count] = [format["format_id"], format["format_note"]]

    return title, available_formats


def download(format_id, url):
    options = {
        "format": format_id,
        "quiet": True
    }
    yt_dlp.YoutubeDL(options).download(url)


def main():
    url = input("Введите URL: ")
    url = url.strip()
    extract_result = get_info(url)

    try:
        title, formats = extract_result
    except ValueError:
        error_message = extract_result
        print(error_message)

        sys.exit()

    print("Выберете желаемый формат видео. Для этого введите число. Например, 1:")

    for k, v in formats.items():
        print(f"{k} - {v[1]}")

    chosen_format = int(input("Введите число: "))
    format_id = formats[chosen_format][0]

    download(format_id, url)


if __name__ == '__main__':
    main()
