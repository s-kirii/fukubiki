ver.1.0
# box object
You can create instance of drawing box object who has some balls including win\_ball as name "box\(\)".
## methods
### \_\_init\_\_\(\)
This is constructor for object.
- arguments
	- number\_of\_balls  
	 Totsl nunber of balls in box as this argument. And default is 100. 
	- win  
	 Number of win\_balls. And default is 2.

### pick\_ball\(\)
You can take balls by this method. And results are stored in "pick\_ball.result" as list.
- arguments
	- times  
	Number of balls you pick.The default is 1.
	- preult  
	If it is True, this method prints results. And defalt is False.
	- wait  
	You can set interval time for picking balls by this argument. And default is 3.
