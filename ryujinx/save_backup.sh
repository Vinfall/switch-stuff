#!/bin/bash

# Ryujinx
PATH_SAVE="/path/to/ryujinx/portable/bis/user/save/0000000000000003/0"
tar czPf  ./save-$(date +'%Y%m%d-%H%M%S').tar.gz $PATH_SAVE/*
echo "Backup finished."
