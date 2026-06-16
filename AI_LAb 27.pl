edge(0,1,1).
edge(0,2,4).
edge(1,3,2).
edge(2,8,1).
edge(8,9,1).

bestfs(Node) :-
    write(Node), write(' '),
    edge(Node, Next, _),
    bestfs(Next).

bestfs(_).