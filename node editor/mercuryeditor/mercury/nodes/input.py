from PyQt5.QtCore import *
from mercuryeditor.mercury.calc_conf import *
from mercuryeditor.mercury.calc_node_base import *
from nodeeditor.utils import dumpException
import pymem
import pymem.process


class CalcInputContent(QDMNodeContentWidget):
    def initUI(self):
        self.edit = QLineEdit("1", self)
        self.edit.setAlignment(Qt.AlignRight)
        self.edit.setObjectName(self.node.content_label_objname)

    def serialize(self):
        res = super().serialize()
        res['value'] = self.edit.text()
        return res

    def deserialize(self, data, hashmap={}):
        res = super().deserialize(data, hashmap)
        try:
            value = data['value']
            self.edit.setText(value)
            return True & res
        except Exception as e:
            dumpException(e)
        return res

@register_node(OP_NODE_INPUT)
class CalcNode_Input(CalcNode):
    icon = ".icons\\in.png"
    op_code = OP_NODE_INPUT
    op_title = "Input (Int)"
    content_label_objname = "calc_node_input"

    def __init__(self, scene):
        super().__init__(scene, inputs=[], outputs=[3])
        self.eval()

    def initInnerClasses(self):
        self.content = CalcInputContent(self)
        self.grNode = CalcGraphicsNode(self)
        self.content.edit.textChanged.connect(self.onInputChanged)

    def evalImplementation(self):
        u_value = self.content.edit.text()
        s_value = int(u_value)
        self.value = s_value
        self.markDirty(False)
        self.markInvalid(False)

        self.markDescendantsInvalid(False)
        self.markDescendantsDirty()

        self.grNode.setToolTip("Integer Input")

        self.evalChildren()

        return self.value

class CalcInputFloatContent(QDMNodeContentWidget):
    def initUI(self):
        self.edit = QLineEdit("1.0", self)
        self.edit.setAlignment(Qt.AlignRight)
        self.edit.setObjectName(self.node.content_label_objname)

    def serialize(self):
        res = super().serialize()
        res['value'] = self.edit.text()
        return res

    def deserialize(self, data, hashmap={}):
        res = super().deserialize(data, hashmap)
        try:
            value = data['value']
            self.edit.setText(value)
            return True & res
        except Exception as e:
            dumpException(e)
        return res

@register_node(OP_NODE_INPUTFLOAT)
class CalcNode_InputFloat(CalcNode):
    icon = ".icons\\in.png"
    op_code = OP_NODE_INPUTFLOAT
    op_title = "Input (Float)"
    content_label_objname = "calc_node_input" #content_label_objname = "calc_node_inputfloat"

    def __init__(self, scene):
        super().__init__(scene, inputs=[], outputs=[3])
        self.eval()

    def initInnerClasses(self):
        self.content = CalcInputFloatContent(self)
        self.grNode = CalcGraphicsNode(self)
        self.content.edit.textChanged.connect(self.onInputChanged)

    def evalImplementation(self):
        u_value = self.content.edit.text()
        s_value = float(u_value)
        self.value = s_value
        self.markDirty(False)
        self.markInvalid(False)

        self.markDescendantsInvalid(False)
        self.markDescendantsDirty()

        self.grNode.setToolTip("Float Input")

        self.evalChildren()

        return self.value


class CalcInputStrContent(QDMNodeContentWidget):
    def initUI(self):
        self.edit = QLineEdit("string", self)
        self.edit.setAlignment(Qt.AlignRight)
        self.edit.setObjectName(self.node.content_label_objname)

    def serialize(self):
        res = super().serialize()
        res['value'] = self.edit.text()
        return res

    def deserialize(self, data, hashmap={}):
        res = super().deserialize(data, hashmap)
        try:
            value = data['value']
            self.edit.setText(value)
            return True & res
        except Exception as e:
            dumpException(e)
        return res

@register_node(OP_NODE_INPUTSTR)
class CalcNode_InputStr(CalcNode):
    icon = ".icons\\in.png"
    op_code = OP_NODE_INPUTSTR
    op_title = "Input (String)"
    content_label_objname = "calc_node_input" #content_label_objname = "calc_node_inputstr"

    def __init__(self, scene):
        super().__init__(scene, inputs=[], outputs=[3])
        self.eval()

    def initInnerClasses(self):
        self.content = CalcInputStrContent(self)
        self.grNode = CalcGraphicsNode(self)
        self.content.edit.textChanged.connect(self.onInputChanged)

    def evalImplementation(self):
        u_value = self.content.edit.text()
        s_value = str(u_value)
        self.value = s_value
        self.markDirty(False)
        self.markInvalid(False)

        self.markDescendantsInvalid(False)
        self.markDescendantsDirty()

        self.grNode.setToolTip("String Input")

        self.evalChildren()

        return self.value

@register_node(OP_NODE_GETVARIABLE)
class CalcNode_GetVariable(CalcNode):
    icon = ".icons\\in.png"
    op_code = OP_NODE_GETVARIABLE
    op_title = "Get Variable"
    content_label_objname = "calc_node_input" #content_label_objname = "calc_node_inputstr"

    def __init__(self, scene):
        super().__init__(scene, inputs=[], outputs=[3])
        self.eval()

    def initInnerClasses(self):
        self.content = CalcInputStrContent(self)
        self.grNode = CalcGraphicsNode(self)
        self.content.edit.textChanged.connect(self.onInputChanged)

    def evalImplementation(self):
        u_value = self.content.edit.text()
        s_value = str(u_value)
        #self.value = s_value

        self.value = CUSTOMVARIABLES.get(s_value)

        self.markDirty(False)
        self.markInvalid(False)

        self.markDescendantsInvalid(False)
        self.markDescendantsDirty()

        self.grNode.setToolTip("Gets a variable with its name")

        self.evalChildren()

        return self.value

#HEX INPUT

class CalcInputHexContent(QDMNodeContentWidget):
    def initUI(self):
        self.edit = QLineEdit("0x45", self)
        self.edit.setAlignment(Qt.AlignRight)
        self.edit.setObjectName(self.node.content_label_objname)

    def serialize(self):
        res = super().serialize()
        res['value'] = self.edit.text()
        return res

    def deserialize(self, data, hashmap={}):
        res = super().deserialize(data, hashmap)
        try:
            value = data['value']
            self.edit.setText(value)
            return True & res
        except Exception as e:
            dumpException(e)
        return res

@register_node(OP_NODE_INPUTHEX)
class CalcNode_InputHex(CalcNode):
    icon = ".icons\\in.png"
    op_code = OP_NODE_INPUTHEX
    op_title = "Input (HEX)"
    content_label_objname = "calc_node_input" #content_label_objname = "calc_node_inputHex"

    def __init__(self, scene):
        super().__init__(scene, inputs=[], outputs=[3])
        self.eval()

    def initInnerClasses(self):
        self.content = CalcInputHexContent(self)
        self.grNode = CalcGraphicsNode(self)
        self.content.edit.textChanged.connect(self.onInputChanged)

    def evalImplementation(self):
        u_value = self.content.edit.text()
        int_value = int(u_value, 0)
        f_value = int(u_value, 16)
        s_value = hex(f_value)
        self.value = int_value
        self.markDirty(False)
        self.markInvalid(False)

        self.markDescendantsInvalid(False)
        self.markDescendantsDirty()

        self.grNode.setToolTip("Hex Input")

        self.evalChildren()
        print(int_value)
        print(type(int_value))
        return int_value
