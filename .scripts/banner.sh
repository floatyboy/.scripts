# !/bin/bash
# ============================ #
#    ~/.scripts/banner.sh      #
# ---------------------------- #
# A script to display a banner #
# ---------------------------- #
#   Floatyboy  -  02.04.2023   #
# ---------------------------- #
#         h@skaare.cc          #
# ---------------------------- #
#   github.com/floatyboy       #
# ============================ #





getwidth() {
    MAX=0
    while IFS=read line; do
        if [ ${#line} -gt $MAX ]; then
            MAX=${#line}
        fi
    done <<< "$1"
    echo $MAX
}


center() {
    PAGEWIDTH=$1
    TEXT=$3
    TEXTWIDTH=$([[ "$2" -eq "0" ]] && echo $(getwidth "$TEXT") || echo $2)
    PADDING=$(((PAGEWIDTH - TEXTWIDTH) / 2))
    while IFS= read -r line; do
        printf "%*s" $(((PAGEWIDTH - TEXTWIDTH) / 2))
        echo "$line"
    done <<< "$TEXT"
}




while getopts "a:n:" opt; do
    case $opt in
        a)
            ASCIIFILE=$OPTARG
            ;;
        n)
            NAME=$OPTARG
            ;;
    esac
done


generate() {
    if [ -e "$ASCIIFILE" ]; then
        center 64 0 "$(cat $ASCIIFILE)"
    fi
    center 64 0 "($figlet "$NAME")"
}

mkdir -p ./etc
echo > ./etc/banner
generate >> ./etc/banner

output=$(generate)
escaped=${output//\\/\\\\}

echo "\n.\1" > /etc/issue
echo >> /etc/issue
echo >> /etc/issue
echo >> /etc/issue
echo >> /etc/issue
echo >> /etc/issue  
echo "$escaped" >> /etc/issue
echo >> /etc/issue


