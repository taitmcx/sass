import requests
import os


BINARY_DIR = "node-sass-binaries"

NEXUS_URL = "http://localhost:8081/repository/sassx/"
NEXUS_USER = "admin"
NEXUS_PASSWORD = "a0893344-0034-452f-82d7-f0d2d9f2cfa9"

def upload_to_nexus(file_path, file_name, version_folder):
    print(f"Uploading {file_name} to Nexus under {version_folder}")
    
    # Nexus'a dosyaları versiyon bazlı klasörlere yüklemek için URL'ye klasör adı ekle
    nexus_upload_url = os.path.join(NEXUS_URL, version_folder, file_name)

    with open(file_path, 'rb') as file_data:
        response = requests.put(
            nexus_upload_url,
            auth=(NEXUS_USER, NEXUS_PASSWORD),
            data=file_data
        )

    if response.status_code == 201 or response.status_code == 200:
        print(f"{file_name} successfully uploaded to Nexus in {version_folder}.")
    else:
        print(f"Failed to upload {file_name} to Nexus: {response.status_code} {response.text}")

def main():
    for root, dirs, files in os.walk(BINARY_DIR):
        # Her dosyanın bulunduğu klasörden versiyon bilgisi çıkar
        version_folder = os.path.relpath(root, BINARY_DIR)
        
        for file_name in files:
            file_path = os.path.join(root, file_name)
            print(f"Processing file: {file_path}")

            upload_to_nexus(file_path, file_name, version_folder)

if __name__ == "__main__":
    main()
