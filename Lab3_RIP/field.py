def field(items, *args):
    assert len(args) > 0 
    for item2 in items:
        for item in args:
            yield(item2.get(item))
