#!/bin/bash

# prepare the download URL
GITHUB_URL=$(curl --silent --location https://api.github.com/repos/yuzu-emu/yuzu-mainline/releases/latest | jq --raw-output ".assets[].browser_download_url" | grep --extended-regexp "yuzu-windows-msvc-.*?.7z")

# install/update the local binary
wget --hsts-file="$XDG_CACHE_HOME/wget-hsts" --quiet $GITHUB_URL
# Variables do not work
unar -quiet -no-directory -force-overwrite yuzu-windows-msvc-*.7z && rm yuzu-windows-msvc-*.7z
rm ./yuzu-windows-msvc/yuzu-windows-msvc-source-*.tar.xz
echo 'Done.'
