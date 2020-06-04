"""
Created on June 2, 2020

@author: Hayk Stepanyan
"""

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    sequence_copy = sequence
    final_list = []
    if len(sequence) == 1:
        final_list.append(sequence)
        return final_list
    else:
        sequence_copy = sequence_copy[1: len(sequence_copy)]
        option_list = get_permutations(sequence_copy)
        for i in range(len(option_list)):
            word_list = [sequence[0]]
            for j in range(len(option_list[i])):
                word_list.append(option_list[i][j])
            final_list.append("".join(word_list))
            for index in range(len(option_list[i])):
                (word_list[index], word_list[index + 1]) = (word_list[index + 1], word_list[index])
                final_list.append("".join(word_list))
            for index in range(len(word_list)):
                del word_list[0]
        return final_list
if __name__ == '__main__':
    #TESTCASE1
    example_input = 'abc'
    print('Input:', example_input)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(example_input))
    print()

    #TESTCASE2
    example_input = 'ab'
    print('Input:', example_input)
    print('Expected Output:', ['ab', 'ba'])
    print('Actual Output:', get_permutations(example_input))
    print()

    #TESTCASE3
    example_input = "qwe"
    print('Input:', example_input)
    print('Expected Output:', ['qwe', 'wqe', 'weq', 'qew', 'eqw', 'ewq'])
    print('Actual Output:', get_permutations(example_input))
    print()
