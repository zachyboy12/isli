# Isli
---
A CLI maker that is targeted for beginners.  
It is based on decorators. There is another module included called argerrors, to raise  
argument-related errors.  
Here is a simple example:  
```
import isli


def mycli():  # You don't have to do this, but it is cleaner


  isli.description = 'An example CLI using Isli'
  
  
  @isli.command('STR')  # Making the below function a command, and giving the type 'STR' to it
  def echo(next_arg):  # You can place the next_arg param optionally, if you want the next argument
    """A simple echo command that acts like the Unix echo command."""  # If you want a description of your command if you type -h or -help or nothing, you need to put a docstring
    print(next_arg)
    
    
  isli.start()
  
  
mycli()
    
```  
It's very simple, right? Unlike [argparse](https://docs.python.org/3/library/argparse.html), it is not hard to read.  
Thanks for looking at Isli!
