import ctypes
import winreg

SPI_SETDESKWALLPAPER = 20

def change_wallpaper(image_path):
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path, 3)

def get_wallpaper_path():
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Control Panel\\Desktop")
        wallpaper_path = winreg.QueryValueEx(key, "Wallpaper")[0]
        return wallpaper_path
    except Exception as e:
        print("Error:", e)
        return None

if __name__ == "__main__":
    parent_path = "D:\python\Important\Change Wallpaper\\"
    current_wallpaper_path = get_wallpaper_path()

    image_path = "path" #change this into your desired wallpaper's path
    print("New wallpaper path:", image_path)
    change_wallpaper(image_path)
