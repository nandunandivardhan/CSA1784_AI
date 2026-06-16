dob(ram,'10-01-2000').
dob(sita,'15-05-2001').
dob(ravi,'20-08-2002').
dob(anu,'12-12-2003').

show_dob(Name) :-
    dob(Name,DOB),
    write(Name),
    write(' was born on '),
    write(DOB).