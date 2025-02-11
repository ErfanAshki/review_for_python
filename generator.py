def something():
    def say_hello(name):
        return f"Hello {name}"

    def say_gn():
        print('Gn')

    say_gn()
    return say_hello('erfan')
        
print(something())
print(say_hello('erfan'))
