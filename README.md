# PushDownAutomata
PDA Simulator for Palindrome Language (wcwᴿ)

Overview
--------
This project implements a Pushdown Automaton (PDA) simulator in Python that recognizes palindromes of the specific form:

L = { wcwᴿ | w ∈ {0, 1}* }

This means the automaton accepts strings composed of any sequence of 0s and 1s (w), followed by a special character c, and then followed by the reverse of that same sequence (wᴿ).

Examples of accepted strings:
- 0c0
- 10c01
- 111c111

Examples of rejected strings:
- 110c110 (since 110 reversed is 011, not 110)
- 0c1

How it Works
------------
The PDA simulator uses a stack-based approach to validate input strings:

1. It begins by pushing a special marker ($) onto the stack.
2. It reads and pushes characters (0 or 1) from the input string onto the stack until the special character c is encountered.
3. After reading the c, the PDA starts comparing the next characters against those popped from the stack.
4. If the stack character matches the input character, the PDA continues; otherwise, it rejects the string.
5. If the input finishes precisely when the bottom-of-stack marker ($) is encountered, the input is accepted.

Usage
-----
To run the PDA simulator:
python pda_simulator.py

To test specific strings, modify or add calls to the test_pda(input_str) function at the end of pda_simulator.py.

Requirements
------------
- Python 3.x

Author
------
MarkLaMer

