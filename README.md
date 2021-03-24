# Control Flow  
## If Statements  
### What are if statements?  
  ***If statements are statements that utilize boolean conditional statements to decide upon the flow of***  
  ***code.***  
* `if` - The first part of an if statement that defines a condition for a result.
* `elif` - The second part which defines an alternate condition for an alternate result.
* `else` - The last part which runs only when no condition has been met.
```python
if a == b:
    print("a is equal to b")
elif a > b:
    print("a is greater than b")
else:
    print("a is none of the above")
```
## Loops  
### What are for loops?  
 ***For loops are loops that are generally used to iterate through objects or collections of objects. They are***  
 ***also used when the number of times a loop should loop is known beforehand***
* For use iterating through an object
```python
example_list = ['item1', 'item2', 'ect']

for item in example_list:
    print(item)
```  
* To loop a certain number of times  
```python
# for current_number in range(start, stop, step)

for x in range(0, 10, 1):
    print("AA")
```

### What are while loops?  
  ***While loops are a form of loop that will continuously run whilst a condition remains True. The condition***  
  ***The condition is checked at the beginning of every loop***
```python
while condition:
    # Do something
```  

### Useful keywords  
* `break` - Used to exit / terminate a loop at any point.  
* `continue` - Skips all the remaining code in the loop body and proceeds to the next iteration of the loop.  
* `pass` - Used as a null statement to allow loops to do nothing as loops cannot be empty.  
