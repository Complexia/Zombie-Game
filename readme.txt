To run the program, type 
>>>python3 main.py 
in the terminal, (omitting the >>>), or run main.py in an IDE.
Inside main.py world is initialized with the data stored inside zombieData.json
To change parameters, edit zombieData.json accordingly

World has a method to visualize the grid before and after the zombie rampage.
call printGrid() from main.py in order to pring grid to console. It is commented
out in main.py, to call it uncomment it

Design thoughts:
    The reason why the json file is read in main.py rather than world.py is to allow
    easy edit to facilitate a different kind of input, such as a text file, user input,
    or simply hardcoding the values. Hence, World does not care about the input method, 
    as long as correct values are received. Their correctness is verified in main.py

    zombieMove method iterates through the list of moves, and per each one, checks
    and updates the grid at that coordinate. The complexity of checking the grid is 
    O(1) as the grid is stored as a 2D array. If it was stored as a 2D list, one could
    keep the pointer of the list per each move in memory, and keep the O(1) complexity per
    each move.

    run method iterates through the list of zombies, which grows as each new zombie is added,
    and calls zombieMove method for each zombie from the list.

    Overall, the complexity of run is as follows:
        Let n be the number of zombies on the list (which can grow, so worst case the number
        of initial zombie + all civillians), and let k be the number of moves. Therefore, 
        the program will take n * k moves before terminating, i.e. total number of zombies multiplied by
        total number of moves. Therefore, complexity of O(n * k)

    An algorithm can be designed to calculate the optimal set of moves given the size
    of the grid to increase the probability of maximum amount of victims. This is something
    I can do for fun, if you are interested. Let me know. 


