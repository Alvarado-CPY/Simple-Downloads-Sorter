from os import mkdir, path

# If you want to create your own personalized folder
# Add a function, follow the pattern, give it a name to the folder and done. Easy, right?
# Don't forget to add it at the end in the FOLDER dictionary.
# that's where they are imported to use


def getDesktopDirectory():
    if path.exists(path.expanduser(path.join("~", "Desktop"))):
        return path.expanduser(path.join("~", "Desktop"))

    return path.expanduser(path.join("~", "Escritorio"))


def getOSDownloadsDirectory():
    if path.exists(path.expanduser(path.join("~", "Downloads"))):
        return path.expanduser(path.join("~", "Downloads"))

    return path.expanduser(path.join("~", "Descargas"))


def joinFolderDirectoryWithContainerFolder(children_folder):
    if path.exists(path.join(getDesktopDirectory(), "OrdenedDesktop")):
        return path.join(getDesktopDirectory(), "OrdenedDesktop", children_folder)

    mkdir(path.join(getDesktopDirectory(), "OrdenedDesktop"))
    return path.join(getDesktopDirectory(), "OrdenedDesktop", children_folder)


def getDownloadedFolderDirectory(folder):
    if path.exists(path.join(getDesktopDirectory(), folder)):
        return path.join(getDesktopDirectory(), folder)

    mkdir(path.join(getDesktopDirectory(), folder))
    return path.join(getDesktopDirectory(), folder)


def getDownloadedExecutablesDirectory():
    return getDownloadedFolderDirectory(joinFolderDirectoryWithContainerFolder("Executables"))


def getDownloadedImgsDirectory():
    return getDownloadedFolderDirectory(joinFolderDirectoryWithContainerFolder("Imgs"))


def getDownloadedOfficeDirectory():
    return getDownloadedFolderDirectory(joinFolderDirectoryWithContainerFolder("Office"))


def getDownloadedPDFDirectory():
    return getDownloadedFolderDirectory(joinFolderDirectoryWithContainerFolder("PDF"))


FOLDERS_DIRECTORIES = {
    "desktop": getDesktopDirectory(),
    "os_downloads": getOSDownloadsDirectory(),
    "executables": getDownloadedExecutablesDirectory(),
    "imgs": getDownloadedImgsDirectory(),
    "office": getDownloadedOfficeDirectory(),
    "pdf": getDownloadedPDFDirectory()
}
