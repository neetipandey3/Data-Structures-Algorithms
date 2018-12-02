import numpy as np

def run_viterbi(emission_scores, trans_scores, start_scores, end_scores):
    """Run the Viterbi algorithm.

    N - number of tokens (length of sentence)
    L - number of labels

    As an input, you are given:
    - Emission scores, as an NxL array
    - Transition scores (Yp -> Yc), as an LxL array
    - Start transition scores (S -> Y), as an Lx1 array
    - End transition scores (Y -> E), as an Lx1 array

    You have to return a tuple (s,y), where:
    - s is the score of the best sequence
    - y is a size N array of integers representing the best sequence.
    """
    L = start_scores.shape[0]
    assert end_scores.shape[0] == L
    assert trans_scores.shape[0] == L
    assert trans_scores.shape[1] == L
    assert emission_scores.shape[1] == L
    N = emission_scores.shape[0]

    y = np.empty((N, ), dtype=np.int32)
    '''for i in xrange(N):
        # stupid sequence
        y.append(i % L)
    # score set to 0
    return (0.0, y)'''

    # initialize empty np arrays for Trellis
    T = np.empty((N+1, L))

    # initialize the dp table for the transition from start <s> using start_scores
    T[0, :] = emission_scores[0, :] + start_scores.T

    # initialize back_pointers array
    back_pointers = np.empty((N-1, L), dtype=np.int32)

    # recursrion: fill the dp table for all the words and labels, ref: slide#47
    for i in range(1, N):
        for j in range(L):
            T[i, j] = emission_scores[i, j] + np.max(T[i-1, :] + trans_scores[:, j])
            back_pointers[i-1, j] = np.argmax(T[i-1, :] + trans_scores[:, j])

    # Fill the end_scores
    T[N, :] = T[N-1, :] + end_scores.T
    #print T
    last_best_tag = np.argmax(T[-1, :])
    #print last_best_tag
    last_tag_ = last_best_tag

    # back track, iterating through the best sequence
    for i in xrange(N-2, -1, -1):
        last_best_tag = back_pointers[i, last_best_tag]
        y[i] = int(last_best_tag)

    y[N-1] = last_tag_

    # max score
    s = np.max(T[-1, :])

    #print s
    #print y
    return (s, y)


