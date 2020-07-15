#!/bin/sh

echo -e "====================\\nSetting Start!\\n===================="

# 仮想環境構築
python -m venv myenv && source myenv/bin/activate

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
)

echo "### ENVIRON Setting ###"
for env in ${ENVIRON[@]}
do
  read -p "${env}: " val
  export $env="$val"
done
echo "### ENVIRON Setting Complete! ###"


echo -e "====================\\nSetting Finish!\\n===================="
