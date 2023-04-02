#! /usr/bin/env bash
#
languages='echo "python golang lua cpp c javascript typescript html css" | tr ' ' '\n''
core_utils='echo "xargs find mv cp sed awk cat touch" | tr ' ' '\n''

selected='printf "$languages\n$core_utils" | fzf'
read -p "query: " query

if printf $languages | grep -qs $selected; then
	curl cheat.sh/$selected/`echo $query | tr ' ' '+'`
else
	curl cheat.sh/$selected~$query
fi

