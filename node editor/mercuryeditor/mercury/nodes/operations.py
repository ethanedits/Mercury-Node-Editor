from PyQt5.QtCore import *
from mercuryeditor.mercury.calc_conf import *
from mercuryeditor.mercury.calc_node_base import *
from nodeeditor.utils import dumpException
import pymem
import pymem.process

@register_node(OP_NODE_PROCESSHANDLE)
class CalcNode_ProcessHandle(CalcNode2):
    icon = "icons/processhandle.png"
    op_code = OP_NODE_PROCESSHANDLE
    op_title = "Process Handle"
    content_label = "P"
    content_label_objname = "calc_node_bg"

    def evalOperation(self, input1):
        process = pymem.Pymem(input1)
        return process

@register_node(OP_NODE_LIST5)
class CalcNode_List5(CalcNode5):
    icon = "icons/list.png"
    op_code = OP_NODE_LIST5
    op_title = "List5 (HEX)"
    content_label = "L"
    content_label_objname = "calc_node_bg"

    def evalOperation(self, input1,input2,input3,input4,input5):
        list = []
        in1 = int(input1, 16)
        in2 = int(input2, 16)
        in3 = int(input3, 16)
        in4 = int(input4, 16)
        in5 = int(input5, 16)

        list.append(in1)
        list.append(in2)
        list.append(in3)
        list.append(in4)
        list.append(in5)

        return list

@register_node(OP_NODE_LIST4)
class CalcNode_List4(CalcNode4):
    icon = "icons/list.png"
    op_code = OP_NODE_LIST4
    op_title = "List4 (HEX)"
    content_label = "L"
    content_label_objname = "calc_node_bg"

    def evalOperation(self, input1,input2,input3,input4):
        list = []
        in1 = int(input1, 16)
        in2 = int(input2, 16)
        in3 = int(input3, 16)
        in4 = int(input4, 16)

        list.append(in1)
        list.append(in2)
        list.append(in3)
        list.append(in4)

        return list

@register_node(OP_NODE_LIST3)
class CalcNode_List3(CalcNode3):
    icon = "icons/list.png"
    op_code = OP_NODE_LIST3
    op_title = "List3 (HEX)"
    content_label = "L"
    content_label_objname = "calc_node_bg"

    def evalOperation(self, input1,input2,input3):
        list = []
        in1 = int(input1, 16)
        in2 = int(input2, 16)
        in3 = int(input3, 16)

        list.append(in1)
        list.append(in2)
        list.append(in3)

        return list

@register_node(OP_NODE_LIST2)
class CalcNode_List2(CalcNode):
    icon = "icons/list.png"
    op_code = OP_NODE_LIST2
    op_title = "List2 (HEX)"
    content_label = "L"
    content_label_objname = "calc_node_bg"

    def evalOperation(self, input1,input2):
        list = []
        in1 = int(input1, 16)
        in2 = int(input2, 16)

        list.append(in1)
        list.append(in2)

        return list

@register_node(OP_NODE_WRITEINT)
class CalcNode_WriteInt(CalcNode3):
    icon = "icons/wpm.png"
    op_code = OP_NODE_WRITEINT
    op_title = "Writing Memory (INT)"
    content_label = "W"
    content_label_objname = "calc_node_bg"

    def evalOperation(self, input1, input2, input3):
        process = input1
        address = input2
        valToWrite = int(input3)
        process.write_int(address, valToWrite)

        return "WPM Successful"

@register_node(OP_NODE_READINT)
class CalcNode_ReadInt(CalcNode):
    icon = "icons/rpm.png"
    op_code = OP_NODE_READINT
    op_title = "Reading Memory (INT)"
    content_label = "R"
    content_label_objname = "calc_node_bg"

    def evalOperation(self, input1, input2):
        process = input1
        address = input2
        rpm = process.read_int(address)
        print(rpm)
        return rpm

def GetPtrAddr(base, offsets, process):
    addr = process.read_int(base)
    for i in offsets:
        if i != offsets[-1]:
            addr = process.read_int(addr + i)
    return addr + offsets[-1]

@register_node(OP_NODE_GETPOINTERADDRESS)
class CalcNode_GetPointerAddress(CalcNode4):
    icon = "icons/getpointeraddress.png"
    op_code = OP_NODE_GETPOINTERADDRESS
    op_title = "Get Pointer Address"
    content_label = "P"
    content_label_objname = "calc_node_bg"

    def evalOperation(self, input1, input2, input3, input4):
        process = input1
        module = input2
        address = int(input3, 16)
        offsets = input4
        
        PointerAddress = GetPtrAddr(module + address, offsets, process)
        return PointerAddress

@register_node(OP_NODE_GETMODULE)
class CalcNode_GetModule(CalcNode):
    icon = "icons/module.png"
    op_code = OP_NODE_GETMODULE
    op_title = "Get Module"
    content_label = "M"
    content_label_objname = "calc_node_bg"

    def evalOperation(self, input1, input2):
        proc = input1
        module = pymem.process.module_from_name(proc.process_handle, input2).lpBaseOfDll
        print(int(module))
        return int(module)

@register_node(OP_NODE_ADD)
class CalcNode_Add(CalcNode):
    icon = "icons/add.png"
    op_code = OP_NODE_ADD
    op_title = "Add"
    content_label = "+"
    content_label_objname = "calc_node_bg"

    def evalOperation(self, input1, input2):
        return input1 + input2

#Append String
@register_node(OP_NODE_APPEND)
class CalcNode_Append(CalcNode):
    icon = "icons/append.png"
    op_code = OP_NODE_APPEND
    op_title = "Append"
    content_label = "+"
    content_label_objname = "calc_node_bg"

    def evalOperation(self, input1, input2):
        print(str(input1) + " " + str(input2))
        return str(input1) + " " + str(input2)

@register_node(OP_NODE_SUB)
class CalcNode_Sub(CalcNode):
    icon = "icons/sub.png"
    op_code = OP_NODE_SUB
    op_title = "Substract"
    content_label = "-"
    content_label_objname = "calc_node_bg"

    def evalOperation(self, input1, input2):
        return input1 - input2

@register_node(OP_NODE_MUL)
class CalcNode_Mul(CalcNode):
    icon = "icons/mul.png"
    op_code = OP_NODE_MUL
    op_title = "Multiply"
    content_label = "*"
    content_label_objname = "calc_node_mul"

    def evalOperation(self, input1, input2):
        print('foo')
        return input1 * input2

@register_node(OP_NODE_DIV)
class CalcNode_Div(CalcNode):
    icon = "icons/divide.png"
    op_code = OP_NODE_DIV
    op_title = "Divide"
    content_label = "/"
    content_label_objname = "calc_node_div"

    def evalOperation(self, input1, input2):
        return input1 / input2

# way how to register by function call
# register_node_now(OP_NODE_ADD, CalcNode_Add)