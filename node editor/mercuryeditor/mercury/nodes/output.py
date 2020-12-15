from PyQt5.QtCore import *
from mercuryeditor.mercury.calc_conf import *
from mercuryeditor.mercury.calc_node_base import *
from nodeeditor.utils import dumpException


class CalcOutputContent(QDMNodeContentWidget):
    def initUI(self):
        self.lbl = QLabel("output", self)
        self.lbl.setAlignment(Qt.AlignLeft)
        self.lbl.setObjectName(self.node.content_label_objname)


@register_node(OP_NODE_OUTPUT)
class CalcNode_Output(CalcNode):
    icon = "icons/out.png"
    op_code = OP_NODE_OUTPUT
    op_title = "Output"
    content_label_objname = "calc_node_output"

    def __init__(self, scene):
        super().__init__(scene, inputs=[1], outputs=[])

    def initInnerClasses(self):
        self.content = CalcOutputContent(self)
        self.grNode = CalcGraphicsNode(self)

    def evalImplementation(self):
        input_node = self.getInput(0)
        if not input_node:
            self.grNode.setToolTip("Input is not connected")
            self.markInvalid()
            return

        val = input_node.eval()

        if val is None:
            self.grNode.setToolTip("Input is NaN")
            self.markInvalid()
            return

        self.content.lbl.setText("%d" % val)
        self.markInvalid(False)
        self.markDirty(False)
        self.grNode.setToolTip("")

        return val

@register_node(OP_NODE_PRINT)
class CalcNode_Print(CalcNode):
    icon = "icons/out.png"
    op_code = OP_NODE_PRINT
    op_title = "Print"
    content_label_objname = "calc_node_output" #content_label_objname = "calc_node_print"

    def __init__(self, scene):
        super().__init__(scene, inputs=[1], outputs=[])

    def initInnerClasses(self):
        self.content = CalcOutputContent(self)
        self.grNode = CalcGraphicsNode(self)

    def evalImplementation(self):
        input_node = self.getInput(0)
        if not input_node:
            self.grNode.setToolTip("Input is not connected")
            self.markInvalid()
            return

        val = input_node.eval()
        if val is None:
            self.grNode.setToolTip("Input is NaN")
            self.markInvalid()
            return

        self.content.lbl.setText(val)
        self.markInvalid(False)
        self.markDirty(False)
        self.grNode.setToolTip("")

        return val
