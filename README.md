# python brute force
This program is a brute force without the need for any external libraries

To use it simply download file and add action to the action definition
an example of this is if you want to print the genorated lines you would use a write this

```
def action(line):
  print(line)
```
  
  
and if you want to check for something do this
```
def action(line):
  if line == 'string':
    print(line)
```
    
to change the list of characters of this program simply change the variable called charList to something like this `['a', 'b', '2', '1']`
ensure all items in the list are strings.
this program also allows for the use of words in your charList.

i have set a maximum length for the strings to 100 characters/numbers.
if you wish to change the maximum length simply change the `maxLength` variable

and if you want to change the starting length of the string change the `startingLength` varuable
