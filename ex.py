

class Foo():

    def bar(self):
        print "nooo"

    def __getattr__(self, bar):
        print bar

    def __setattr__(self, attr, val):
        print attr, val

    def __str__(self):
        return "Returned string"

    def __repr__(self):
        return "I'm foo"

foo = Foo()

foo.bar()
foo.baz
foo.foobar

print str(foo)

print brepr(fooo)

foo.bar = "foo"

def test():
    
    def test2(a):
        print a
        
    return test2

test()("test2")

