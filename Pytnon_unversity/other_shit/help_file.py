for i in range(1, 100):
    a = i ** 2
    a_ = str(a)
    a_reversed = reversed(a_)
    if a_ == a_reversed:
        print("hh")
    else:
        print("gg", type(a_))
