Overview
========

This library provides atomic functions implementations for easing the
development of quantum networking protocols. The library provides
functions in a simulation backend agnostic way thanks to a thin wrapping
of their basic functionalities. The various atomic function
implementations are dispatched in several submodules depending on their
anticipated use. The surrent submodules classification is:

-  ``mapping`` (the thing wrapper around a simulation backend)
-  ``gate`` (everything that applies a fixed quantum unitary over 1 or 2
   qubits)
-  ``prep`` (operations related to prepare given sets of quantum states)
-  ``meas`` (operations related to measure quantum subsystems according
   to some fixed POVM)
-  ``test`` (operations related to testing that one or several quantum
   subsystems have a given property)
-  ``util`` (useful operations that might not be directly related to a
   specific quantum operation but which are good to have)
-  ``tran`` (transport layer protocols which might not be readily
   available for all backends or which would need to include more robust
   implementations)

Functionality tests are being developed for the atomic functions relying
on the ``hypothesis`` package. The test tend to follow the cryptographic
approach of "correctness". The "security" part is usually not performed
as this most of the times involves checking indistinguishability of
probability distributions…

Status
======

Implemented atomic functions and planning

======================================================== ============== ========== ==== ================== =================================================================================
Name                                                     Implementation Doc string Test Submodule          Comment
======================================================== ============== ========== ==== ================== =================================================================================
Sending qubit (given by simulation backend)              DNE            OK         NA   simulaqron mapping
Receive qubit (given by simulation backend)              DNE            OK         NA   simulaqron mapping
Local Clifford Gates (CNOT, H, Pauli's)                  DNE            OK         NA   simulaqron mapping
Local non-Clifford Gates (T, Tinv)                       DNE            OK         NA   simulaqron mapping
CZ gate                                                  DNE            OK         TDO  gate               self inverse, and corresponds to classically controlled Z for comp. basis control
CSWAP gate                                               DNE            OK         TDO  gate              
Creation Pauli eigenstates                               DNE            OK         DNE  prep              
Creation and broadcast of n-party GHZ state              DNE            OK         DNE  prep              
Single qubit equatorial plane preparation                DNE            OK         TDO  prep              
Creation and broadcast of n-party stabilizer states      NXT                            prep              
QFactory                                                 LTR                            prep              
Projections onto Pauli eigenstates                       DNE            OK         OK   meas              
Single qubit equatorial plane measurement                TDO                            meas              
Multi qubit POVM                                         LTR                            meas              
Quantum One-Time-Pad encode / decode                     DNE            OK         OK   pres              
BB84 encode / decode is a subset of QOTP encode / decode NA             NA         NA   NA                
Collective BB84 encoding                                 DNG                            pres              
Swap Test                                                DNE            OK         TDO  test              
Verification of stabilizer state                                                        test              
Quantum RNG                                              DNE            Check      TDO  util              
Information reconciliation                               LTR                            util              
Classical error correction                               LTR                            util              
Quantum error correction                                 LTR                            util              
Privacy amplification                                    LTR                            util              
Quantum one-way function                                 NXT                            util              
Weak string erasure                                      NXT                                              
Teleportation send                                       TDO                            tran              
Teleportation receive                                    TDO                            tran              
Quantum authenticated channel                            LTR                                              
Secure classical broadcast channel                       LTR                                              
Classical authenticated channel                          LTR                                              
======================================================== ============== ========== ==== ================== =================================================================================

Design principles
=================

There exist many different quantum computing backends. The idea with
this library was to abstract them away so that code running written
using the library could be run on other backends, provided that the rest
of the code not composed of functions defined by the library is not
backend specific.

To do this, we instantiate the library by giving it a mapping and a
node. The mapping is the translation of the backend specific way of
calling elementary quantum operations, while the node is the actual
quantum registers that are available to perform the computation. The
node usually contains also some additional functions such as sending
qubits to other nodes, receiving and sending entanglement etc. The
differences have been abstracted away with the mappings for
``simulaqron`` and ``qunetsim`` . Other mappings have been considered
and used but not yet made available most notably for ``Netsquid``.

Feel free to add functions, or code new mappings by forking and
pull-requesting insertion of your additions. Please keep us updated with
your work so that we inform you of changes that could be breaking
things.

Usage
=====

Look at the ``examples/examples.py`` file. The library is instantiated
for each node (as if the nodes were independent computers, each loading
its version of the library).

Other sources of inspirations are the tests defined in the ``tests``
directory

New atomic functions will be added following the list established by
extracting atomic functions from the Quantum Protocol Zoo.

Testing
=======

Tests can be run using ``python setup.py test`` at the root of the
repository.

The repository includes a tests directory that contains the file
``test_qpz_atomics.py`` which gathers all the tests implemented. It is
using the ``pytest`` package to launch the tests and gather statistics,
while being based on ``hypothesis`` for generating examples.

For the tests to run, you need to have a quatum network simulator
available and running. We have chosen to implement the tests using
``simulaqron`` as a backend, hence requiring a running
`simulaqron <https://pypi.org/project/simulaqron/>`__ instance. This can
be done typing the following:

.. code:: bash

   simulaqron set max-qubits 100
   simulaqron start

Other backends could be used provided the tests are rewritten and the
required backend is available and properly mapped in the library.

Acknowledgments
===============

This project is part of Laboratoire d'Informatique Paris 6 - Sorbonne
Université / CNRS - Quantum Information Team. It is funded and is part
of the Quantum Internet Alliance European Project.
