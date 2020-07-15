ver.1.0
# box object
You create drawing box object who has some balls including win_ball as name box.
## methods
### __init__()
This is constructor for object.
- arguments
	- number_of_balls
	Totsl nunber of balls in box as this argument. And default is 100. 
	- win
	Number of win_balls. And default is 2.
### pick_ball()
You can take balls by this method. And results are stored in "pick_ball.result".
- arguments
	- times
	Number of balls you pick.The default is 1.
	- preult
	If it is True, this method prints results. And defalt is False.
	- wait
	You can set interval time for picking balls by this argument. And default is 3.
