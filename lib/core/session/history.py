class History(list):
    """Commands history.

    This class is a specialisation of the list() obj, designed
    to store line command strings only.

    It maintains a `size` property which gives the full size (in bytes)
    of all strings in array.

    To do it, the class operates overriding append(), pop() and clear()
    methods to maintain the current size.

    """

    size = 0;

    def append(self, string):
        if not isinstance(string, str):
            raise ValueError("Only strings could be added to history");
        self.size += len(string)
        super().append(string)


    def pop(self, index=-1):
        try:
            self.size -= len(self[index]);
        except:
            pass
        super().pop(index)


    def clear(self):
        self.size = 0
        super().clear()
