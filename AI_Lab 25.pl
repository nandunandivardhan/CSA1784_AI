move(atdoor, atwindow).
move(atwindow, onbox).
move(onbox, banana).

get_banana :-
    move(atdoor, atwindow),
    move(atwindow, onbox),
    move(onbox, banana),
    write('Monkey got the banana').