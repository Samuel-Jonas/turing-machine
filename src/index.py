# definição formal de AFD

# 5-tuple (Q, Σ, δ, q0, F)

# Q conjunto dos estados
# Σ alfabeto
# δ função de transição
# q0 estado inicial
# conjunto dos estados de aceitação

# Definição formal de uma MT
# M = (Q, Σ, Γ, δ, q0, qaceita, qrejeita)

# Q conjunto finito de estados
# Σ alfabeto finito de entrada
# Γ alfabeto finito da fita
# q0 ∈ Q estado inicial
# qaceita ∈ Q estado de aceitação
# qrejeita ∈ Q estado de rejeição
# δ : Q × Γ → Q × Γ × {L, R} função de transição

#{0^n1^n | n >= 0}

states = ["q1", "q2", "q3", "q4", "q_accept", "q_reject"]
alphabets_input = ["0", "1"]
alphabets_tape = ['0', '1', '⊔', 'X', 'Y']
start_state = "q1"
accept_state = "q_accept"
reject_state = "q_reject"
transition_map = {
    ('q1', '0'): ('q2', 'X', 'R'),
    ('q1', 'Y'): ('q4', 'Y', 'R'),
    ('q1', '⊔'): ('q_reject', '⊔', 'R'),
    ('q1', '1'): ('q_reject', '1', 'L'),
    ('q1', 'X'): ('q_reject', 'X', 'L'),
    ('q2', '0'): ('q2', '0', 'R'),
    ('q2', 'Y'): ('q2', 'Y', 'R'),
    ('q2', '1'): ('q3', 'Y', 'L'),
    ('q2', 'X'): ('q_reject', 'X', 'L'),
    ('q2', '⊔'): ('q_reject', '⊔', 'L'),
    ('q3', '0'): ('q3', '0', 'L'),
    ('q3', '1'): ('q_reject', '1', 'L'),
    ('q3', 'Y'): ('q3', 'Y', 'L'),
    ('q3', '⊔'): ('q_reject', '⊔', 'L'),
    ('q3', 'X'): ('q1', 'X', 'R'),
    ('q4', '0'): ('q_reject', '0', 'L'),
    ('q4', '1'): ('q_reject', '1', 'L'),
    ('q4', '⊔'): ('q_accept', '⊔', 'R'),
    ('q4', 'X'): ('q_reject', 'X', 'L'),
    ('q4', 'Y'): ('q4', 'Y', 'R'),
    ('q_accept', '0'): ('q_accept', '0', 'L'),
    ('q_accept', '1'): ('q_accept', '1', 'L'),
    ('q_accept', 'X'): ('q_accept', 'X', 'L'),
    ('q_accept', 'Y'): ('q_accept', 'Y', 'L'),
    ('q_accept', '⊔'): ('q_accept', '⊔', 'L'),
    ('q_reject', '0'): ('q_reject', '0', 'L'),
    ('q_reject', '1'): ('q_reject', '1', 'L'),
    ('q_reject', 'X'): ('q_reject', 'X', 'L'),
    ('q_reject', 'Y'): ('q_reject', 'Y', 'L'),
    ('q_reject', '⊔'): ('q_reject', '⊔', 'L')
}

def turing_machine(input_str):
    tape = list(input_str)
    tape_index = 0
    current_state = start_state

    print(tape)

    if len(tape) == 0 or tape[tape_index] == '⊔':
        current_state = accept_state

    while current_state != accept_state and current_state != reject_state:
        symbol_under_head = tape[tape_index]
        if (current_state, symbol_under_head) in transition_map:
            next_state, write_symbol, move_direction = transition_map[(current_state, symbol_under_head)]
            tape[tape_index] = write_symbol
            tape_index += 1 if move_direction == 'R' else -1
            current_state = next_state
        else:
            current_state = reject_state
        
        print(tape)

    if current_state == accept_state:
        print("Accepted")
    else:
        print("Rejected")

turing_machine("011⊔")