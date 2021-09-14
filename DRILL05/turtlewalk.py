import turtle as t

 
def turn_right():
    t.setheading(0)
    t.forward(50)
    t.stamp()
           
    
def turn_up():                    
    t.setheading(90)
    t.forward(50)
    t.stamp()
   
 

def turn_left():                 
    t.setheading(180)
    t.forward(50)
    t.stamp()
   
 

def turn_down():                  
    t.setheading(270)
    t.forward(50)
    t.stamp()
  

def restart():                      
    t.reset()

    
t.shape("turtle")                
t.speed(0)                        
t.onkeypress(turn_right, "d")
t.shape("turtle")
t.onkeypress(turn_up, "w")
t.shape("turtle")
t.onkeypress(turn_left, "a")
t.shape("turtle")
t.onkeypress(turn_down, "s")
t.shape("turtle")
t.onkeypress(restart, "Escape")     
t.listen()                        

