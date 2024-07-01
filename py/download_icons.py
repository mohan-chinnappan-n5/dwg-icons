# download_icons.py

from urllib.request import urlretrieve

def download_icons():
    icons = {
        "sf": "https://raw.githubusercontent.com/mohan-chinnappan-n5/dwg-icons/main/sf/sf.svg.png",
        "mulesoft": "https://raw.githubusercontent.com/mohan-chinnappan-n5/dwg-icons/main/sf/mulesoft.svg.png"
    }
    
    for name, url in icons.items():
        filename = f"{name}.svg.png"
        urlretrieve(url, filename)
        print(f"Downloaded {filename}")

if __name__ == "__main__":
    download_icons()
