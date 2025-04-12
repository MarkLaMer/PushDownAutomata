class PDA:
    def __init__(self):
        self.stack = []
        self.state = 'q1'
        self.input_str = ''
        self.index = 0

    def push(self, item):
        self.stack.append(item)

    def pop(self, char):
        if self.stack and self.stack[-1] == char:
            self.stack.pop()
            return True
        return False

    def read(self):
        if self.index >= len(self.input_str):
            return None  # End of input

        char = self.input_str[self.index]
        self.index += 1
        return char

    def q1(self):
        # Initial state: push bottom-of-stack marker
        self.push('$')
        self.state = 'q2'

    def q2(self):
        current = self.read()
        if current in ['0', '1']:
            self.push(current)  # Push characters of w onto stack
        elif current == 'c':
            self.state = 'q3'  # Transition to checking mirrored string
        else:
            self.state = 'reject'

    def q3(self):
        current = self.read()
        if current in ['0', '1']:
            if not self.pop(current):
                self.state = 'reject'  # Mismatch, not w^R
        elif current is None:  # End of input
            if self.pop('$'):
                self.state = 'accept'
            else:
                self.state = 'reject'
        else:
            self.state = 'reject'  # Invalid character

    def M2(self, input_str):
        self.input_str = input_str
        self.stack = []  # Reset stack for each new input
        self.index = 0   # Reset index for each new input
        self.state = 'q1'  # Reset to start state
        while True:
            if self.state == 'q1':
                self.q1()
            elif self.state == 'q2':
                self.q2()
            elif self.state == 'q3':
                self.q3()
            elif self.state == 'accept':
                return True
            elif self.state == 'reject':
                return False

def test_pda(input_str):
    pda = PDA()
    if pda.M2(input_str):
        print(f"Input '{input_str}' is ACCEPTED.")
    else:
        print(f"Input '{input_str}' is REJECTED.")

# Test cases
test_pda("")           # REJECTED (Empty string)
test_pda("0c0")        # ACCEPTED
test_pda("10c01")      # ACCEPTED
test_pda("111c111")    # ACCEPTED
test_pda("110c110")    # REJECTED (w != w^R)
test_pda("0c1")        # REJECTED (w != w^R)
test_pda("01c10")      # ACCEPTED
test_pda("01c11")      # REJECTED
