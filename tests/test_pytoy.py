from pytoy import teddy

def test_teddy():
    out = teddy(False)
    assert(out.find('jgs'))
    assert (len(out) == 575)
