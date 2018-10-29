if [ $1 = "goals" ];
    then
    export DISPLAY=:0 && xdg-open https://leetcode.com/problemset/algorithms/?difficulty=Easy&listId=wpwgkgt 
    xdg-open https://inforlms.certpointsystems.com/lms/basicportal/eap/en-US/
    xdg-open https://raw.githubusercontent.com/princessguerrero/testprojects/master/myscriptproj/goals.txt
fi

notify-send "Goals!!!" ; sleep 5 ; killall notify-osd

# if [ $1 = "leet" ];
#     then export DISPLAY=:0 && xdg-open https://leetcode.com/problemset/algorithms/?difficulty=Easy&listId=wpwgkgt 
# elif [ $1 = "lms" ];
#     then export DISPLAY=:0 && xdg-open https://inforlms.certpointsystems.com/lms/basicportal/eap/en-US/
# fi
