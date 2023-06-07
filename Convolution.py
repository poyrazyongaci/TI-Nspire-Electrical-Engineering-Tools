import re

def conSeq(seq1, seq2):
    # Replace occurrences of number followed by 'U' with the corresponding number of '1's
    seq1 = re.sub(r'(\d+)U', lambda match: '1' * int(match.group(1)), seq1)
    seq2 = re.sub(r'(\d+)U', lambda match: '1' * int(match.group(1)), seq2)

    # Calculate the length of the resulting sequence
    length = len(seq1) + len(seq2) - 1

    # Initialize the resulting sequence with zeros
    result = [0] * length

    # Perform convolution
    for i in range(len(seq1)):
        for j in range(len(seq2)):
            result[i+j] += int(seq1[i]) * int(seq2[j])

    return result

# Test the code
sequence1 = '1'
sequence2 = '1 2'
result = conSeq(sequence1, sequence2)
print(result)
