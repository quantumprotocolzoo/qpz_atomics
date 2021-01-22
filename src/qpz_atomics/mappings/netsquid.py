import netsquid.components.instructions as instr

def X(q, node, *args, **kwargs):
    """
    (q, *args, **kwargs) -> qubit
    Applies X to qubit and returns the qubit to be used for having a functional like programming, but not necessary as the qubit is modified in place.
    """
    def apply_instr(): 
        node.node.qmemory.execute_instruction(instr.INSTR_X, q);
        print('X')
        yield node.await_program(node.node.qmemory)
    apply_instr()
    return q

def Z(q, node, *args, **kwargs):
    """
    (q, *args, **kwargs) -> qubit
    Applies Z to qubit and returns the qubit to be used for having a functional like programming, but not necessary as the qubit is modified in place.
    """
    def apply_instr():
        node.node.qmemory.execute_instruction(instr.INSTR_Z, q);
        print('Z')
        yield node.await_program(node.node.qmemory)
    apply_instr()
    return q
    
def H(q, node, *args, **kwargs):
    """
    (q, *args, **kwargs) -> qubit
    Applies H (Hadamard) to qubit and returns the qubit to be used for having a functional like programming, but not necessary as the qubit is modified in place.
    """
    def apply_instr():
        node.node.qmemory.execute_instruction(instr.INSTR_H, q);
        print('H')
        yield node.await_program(node.node.qmemory)
    apply_instr()
    return q

def PREP(q, node, *args, **kwargs):
    def apply_instr():
        node.node.qmemory.execute_instruction(instr.INSTR_INIT, q);
        print('INIT')
        yield node.await_program(node.node.qmemory)
    apply_instr()
    return q
        
def MEAS(q, node, *args, **kwargs):
    def apply_instr():
        node.node.qmemory.execute_instruction(instr.INSTR_MEASURE, q, output_key="M");
        yield node.await_program(node.node.qmemory)
    apply_instr()
    return res[0]['M'][0]


mapping = {
    "X": X,
    "Y": None,
    "Z": Z,
    "H": H,
    
    "K": None,
    "T": None,
    "Tinv":None,

    "CNOT": None,

    "PREP": PREP,
    "MEAS": MEAS,
    "DISP": None,
    "QID": None,
    
    "EPR": None,
    "SEND": None,
    "RECV": None,
    "TELE": None
    }
