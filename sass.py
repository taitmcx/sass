import os
import requests

api_url = "https://api.github.com/repos/sass/node-sass/releases"

download_dir = "node-sass-binaries"

if not os.path.exists(download_dir):
    os.makedirs(download_dir)

def download_file(url, filename):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        file_path = os.path.join(download_dir, filename)
        with open(file_path, 'wb') as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)
        print(f"{filename} indirildi.")
    else:
        print(f"İndirme başarısız: {url}")


response = requests.get(api_url)
if response.status_code == 200:
    releases = response.json()
    
    for release in releases:
        version = release['tag_name']
        print(f"Sürüm: {version}")
        

        for asset in release['assets']:
            asset_name = asset['name']
            download_url = asset['browser_download_url']
            print(f"İndiriliyor: {asset_name}")
            download_file(download_url, asset_name)
else:
    print(f"API isteği başarısız oldu: {response.status_code}")
