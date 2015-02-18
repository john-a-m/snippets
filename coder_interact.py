import code

def function():
    n = 1
    code.interact(local=dict(locals().items() + globals().items()))
  
function() #you can now type run `print n` and it will print `1`
