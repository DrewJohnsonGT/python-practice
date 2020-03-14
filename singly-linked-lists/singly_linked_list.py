# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return f'{self.val} => {self.next}'

    def __key(self):
        return (self.val)

    def __hash__(self):
        return hash(self.__key())

    def __eq__(self, other):
        _self_node = self
        _other_node = other
        if type(_self_node) == type(None):
            if type(_other_node) == type(None):
                return True
            else:
                return False
        if type(_other_node) == type(None):
            return False
        if _self_node.val != _other_node.val:
            return False
        return _self_node.next == _other_node.next