import os

def download_youtube_media(url, file_name, format_type):
    """
    Pakua video au sauti kutoka YouTube na ihifadhi kwenye folder la Downloads.
    :param url: URL ya video ya YouTube
    :param file_name: Jina la faili bila njia kamili
    :param format_type: Aina ya media ('video' au 'audio')
    """
    # Pata directory ya Downloads kwa kutumia njia ya mfumo
    downloads_dir = os.path.join(os.path.expanduser("~"), "Downloads")
    destination = os.path.join(downloads_dir, file_name)

    if format_type == "video":
        # Pakua video ya ubora wa kati (720p max), kisha iunganishe
        os.system(f"yt-dlp -f 'bv[height<=720]+ba/b' --merge-output-format mp4 -o '{destination}' {url}")
    elif format_type == "audio":
        # Pakua sauti ya ubora mzuri na ukubwa mdogo
        os.system(f"yt-dlp -f bestaudio --extract-audio --audio-format mp3 --audio-quality 5 -o '{destination}' {url}")
    else:
        print("[ERROR] Aina ya faili batili.")

    print(f"Faili imepakuliwa na kuhifadhiwa kwenye: {destination}")

if __name__ == "__main__":
    url = input("Ingiza URL ya video ya YouTube: ")
    file_name = input("Ingiza jina la faili la kuhifadhi (mfano: video.mp4 au audio.mp3): ")
    format_type = input("Unataka kupakua nini? ('video' au 'audio'): ")
    download_youtube_media(url, file_name, format_type)
