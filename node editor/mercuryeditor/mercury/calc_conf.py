LISTBOX_MIMETYPE = "application/x-item"

OP_NODE_INPUT = 1
OP_NODE_OUTPUT = 9
OP_NODE_PRINT = 10
OP_NODE_ADD = 5
OP_NODE_SUB = 6
OP_NODE_MUL = 7
OP_NODE_DIV = 8

OP_NODE_INPUTSTR = 2
OP_NODE_INPUTHEX = 3
OP_NODE_INPUTFLOAT = 4

OP_NODE_APPEND = 11
OP_NODE_PROCESSHANDLE = 12
OP_NODE_GETMODULE = 13
OP_NODE_WRITEINT = 14
OP_NODE_READINT = 15

OP_NODE_WRITEFLOAT = 16
OP_NODE_READFLOAT = 17

OP_NODE_GETPOINTERADDRESS = 18


OP_NODE_LIST1 = 19
OP_NODE_LIST2 = 20
OP_NODE_LIST3 = 21
OP_NODE_LIST4 = 22
OP_NODE_LIST5 = 23


CALC_NODES = {
}


class ConfException(Exception): pass
class InvalidNodeRegistration(ConfException): pass
class OpCodeNotRegistered(ConfException): pass


def register_node_now(op_code, class_reference):
    if op_code in CALC_NODES:
        raise InvalidNodeRegistration("Duplicate node registration of '%s'. There is already %s" %(
            op_code, CALC_NODES[op_code]
        ))
    CALC_NODES[op_code] = class_reference


def register_node(op_code):
    def decorator(original_class):
        register_node_now(op_code, original_class)
        return original_class
    return decorator

def get_class_from_opcode(op_code):
    if op_code not in CALC_NODES: raise OpCodeNotRegistered("OpCode '%d' is not registered" % op_code)
    return CALC_NODES[op_code]



# import all nodes and register them
from mercuryeditor.mercury.nodes import *