from os import listdir, path
from shutil import move as moveDownloadedFileToDestinyFolder
from config.folders import FOLDERS_DIRECTORIES
from config.extensions_list import EXECUTABLE_EXTENSIONES, OFFICE_EXTENSIONS, IMG_EXTENSIONS


def getAllFilesInOSDownloadFolder():
    download_folder = FOLDERS_DIRECTORIES["os_downloads"]
    downloads = []

    for download in listdir(download_folder):
        downloads.append({"file_name": download, "ext": path.splitext(
            download)[-1], "path": path.join(download_folder, download)})

    return downloads


def sendDownloadedFileToCorrectFolder(downloaded_file_direction, destiny_folder_direction):
    moveDownloadedFileToDestinyFolder(
        downloaded_file_direction, destiny_folder_direction)


def clasificateAllFilesByTheExtension():
    downloads = getAllFilesInOSDownloadFolder()
    for download in downloads:
        if download["ext"] == "":
            print(
                f"Can't process file name: {download['file_name']}. No extension provided.")
            continue

        if download["ext"] == ".pdf":
            sendDownloadedFileToCorrectFolder(
                downloaded_file_direction=download["path"],
                destiny_folder_direction=FOLDERS_DIRECTORIES["pdf"]
            )
            continue

        if download["ext"] in IMG_EXTENSIONS:
            sendDownloadedFileToCorrectFolder(
                downloaded_file_direction=download["path"],
                destiny_folder_direction=FOLDERS_DIRECTORIES["imgs"]
            )
            continue

        if download["ext"] in OFFICE_EXTENSIONS:
            sendDownloadedFileToCorrectFolder(
                downloaded_file_direction=download["path"],
                destiny_folder_direction=FOLDERS_DIRECTORIES["office"]
            )
            continue

        if download["ext"] in EXECUTABLE_EXTENSIONES:
            sendDownloadedFileToCorrectFolder(
                downloaded_file_direction=download["path"],
                destiny_folder_direction=FOLDERS_DIRECTORIES["office"]
            )
            continue


def run():
    clasificateAllFilesByTheExtension()


if __name__ == "__main__":
    run()
