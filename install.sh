#!/usr/bin/sh

echo -e "====================\nSetting Start!\n===================="


#Pythonライブラリ インストール
COMMANDS=(
    beautifulsoup4
    requests
    lxml
)

echo "### Library Install ###"
for cmd in ${COMMANDS[@]}
do
  pip install $cmd || { echo "${cmd} install failed!"; exit 1; }
done
echo "### Install Complete! ###"


#環境変数 設定
ENVIRON=(
    LINE_API_URL
    LINE_API_TOKEN
    TRAIN_URLS
)

echo "### ENVIRON Setting ###"
for env in ${ENVIRON[@]}
do
  read -p "${env}: " val
  while [ -z "$val" ]
  do    
    read -p "${env}: " val
  done
  export $env="$val"
done
echo "### ENVIRON Setting Complete! ###"


echo -e "====================\nSetting Finish!\n===================="
