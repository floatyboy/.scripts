# ..
# /bin/bash
#

export NEWT_COLORS="
root=,blue
window=,black
shadow=,blue
border=blue,black
title=blue,black
textbox=blue,black
radiolist=black,black
label=black,blue
checkbox=black,blue
compactbutton=black,blue
button=black,red"

max() {
    echo -e "$1\n$2" | sort -n | tail -1
}

getbiggestword() {
    echo "$@" | sed "s/ /\n/g" | wc -L
}

replicate() {
    local n="$1"
    local c="$2"
    local str

    for _ in $(seq 1 "$n"); do
        str="$str$x"
    done
    echo "$str"
}

programchoices() {
    choices=()
    local maxlen; maxlen="$(getbiggestword "${!checkboxes[@]}")"
    linesize="$(max "$maxlen" 42)"
    local spacer; spacer="$(replicate "$((linesize - maxlen))" " ")"

    for key in "${!checkboxes[@]}"; do
        if ! command -v "${checkboxes[$key]}" &>/dev/null; then
            choices+=("$key" "$spacer" "OFF")
        else
            choices+=("$key" "$spacer" "ON")
        fi
    done
}

selectedprograms() {
    result=$(
        whiptail --title "$title"
        --checklist



