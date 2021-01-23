from functools import reduce

class Prep:
    def __init__(self, _): 
        def pauli(bit, base, q=[0]):
            """
            bit in 0,1 -> base in 1=X,2=Z,3=Y -> qubit in basis = base with value = bit
            Prepares a qubit in a Pauli eigenstate defined by a bit value (0 for +1 eigenvalue, 1 for -1 eigenvalue) and an integer 1,2,3 corresponding to the Pauli operator selected.
            """
            if base == 1: 
                if bit == 0 : q_out = _.H(_.PREP(q=q))
                elif bit == 1 : q_out = _.H(_.X(_.PREP(q=q)))
            elif base == 2: 
                if bit == 0 : q_out = _.PREP(q=q)
                elif bit == 1 : q_out = _.X(_.PREP(q=q))
            elif base == 3: 
                if bit == 0 : q_out = _.K(_.PREP(q=q))
                elif bit == 1 : q_out = _.K(_.X(_.PREP(q=q)))
            else: raise NameError(f"""Cannot prepare this state: basis must be 1=X, 2=Z or 3=Y. Currently:  {base}""")
            print(bit,base,q)
            return q_out

        def ghz(nb_target_nodes):
            """
            nb_target_nodes -> array of qubits
            Prepares an n-party GHZ state
            """
            def add_one_qubit(q, p):
                __, r = _.CNOT(q, _.PREP(p))
                return r

            q = _.H(_.PREP(0))

            return [q] + [add_one_qubit(q, p) for p in range(nb_target_nodes)]

        def equatorial(pi_over_4_multiple):
            """
            pi_over_4_multiple -> qubit
            Prepares a qubit in $Z(theta) \ket{+}$ where theta is a $\pi/4$ multiple
            """
            return reduce(lambda a, c: _.T(a), range(pi_over_4_multiple % 8), _.H(_.PREP())) 

        self.pauli = pauli
        self.equatorial = equatorial
        self.ghz = ghz
