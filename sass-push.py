import requests
import os


BINARY_DIR = "node-sass-binaries"

NEXUS_URL = "http://localhost:8081/repository/node-sass/"
NEXUS_USER = "admin"
NEXUS_PASSWORD = ""

def upload_to_nexus(file_path, file_name):
    print(f"Uploading {file_name} to Nexus")
    nexus_upload_url = os.path.join(NEXUS_URL, file_name)

    with open(file_path, 'rb') as file_data:
        response = requests.put(
            nexus_upload_url,
            auth=(NEXUS_USER, NEXUS_PASSWORD),
            data=file_data
        )

    if response.status_code == 201 or response.status_code == 200:
        print(f"{file_name} successfully uploaded to Nexus.")
    else:
        print(f"Failed to upload {file_name} to Nexus: {response.status_code} {response.text}")

def main():
    for root, dirs, files in os.walk(BINARY_DIR):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            print(f"Processing file: {file_path}")

            upload_to_nexus(file_path, file_name)

if __name__ == "__main__":
    main()
