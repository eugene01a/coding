from unittest import TestCase

import ddt

'''
You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots: '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'. The wheels can rotate freely and wrap around: for example we can turn '9' to be '0', or '0' to be '9'. Each move consists of turning one wheel one slot.

The lock initially starts at '0000', a string representing the state of the 4 wheels.

You are given a list of deadends dead ends, meaning if the lock displays any of these codes, the wheels of the lock will stop turning and you will be unable to open it.

Given a target representing the value of the wheels that will unlock the lock, return the minimum total number of turns required to open the lock, or -1 if it is impossible.

Example 1:
Input: deadends = ["0201","0101","0102","1212","2002"], target = "0202"
Output: 6
Explanation:
A sequence of valid moves would be "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202".
Note that a sequence like "0000" -> "0001" -> "0002" -> "0102" -> "0202" would be invalid,
because the wheels of the lock become stuck after the display becomes the dead end "0102".
Example 2:
Input: deadends = ["8888"], target = "0009"
Output: 1
Explanation:
We can turn the last wheel in reverse to move from "0000" -> "0009".
Example 3:
Input: deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"], target = "8888"
Output: -1
Explanation:
We can't reach the target without getting stuck.
Example 4:
Input: deadends = ["0000"], target = "8888"
Output: -1
Note:
The length of deadends will be in the range [1, 500].
target will not be in the list deadends.
Every string in deadends and the string target will be a string of 4 digits from the 10,000 possibilities '0000' to '9999'.
'''
from collections import deque


class Solution(object):

    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """

        def helper(comb, idx):
            if comb[idx] == '0':
                rv = '9'
            else:
                rv = str(int(comb[idx]) - 1)

            if comb[idx] == '9':
                fv = '0'
            else:
                fv = str(int(comb[idx]) + 1)

            rev = '%s%s%s' % (comb[:idx], rv, comb[idx + 1:])
            fwd = '%s%s%s' % (comb[:idx], fv, comb[idx + 1:])
            return fwd, rev

        visited = set(deadends)
        queue = deque()
        if '0000' not in visited:
            queue.append(('0000', 0))
        while queue:
            c, steps = queue.popleft()
            for i in range(4):
                for b in helper(c, i):
                    if b == target:
                        return steps + 1
                    if b in visited:
                        continue
                    else:
                        visited.add(b)
                        queue.append((b, steps + 1))
        return -1


@ddt.ddt
class LeetCodeTest(TestCase):

    def setUp(self):
        self.solution = Solution()

    @ddt.unpack
    @ddt.data(
        ([["0201", "0101", "0102", "1212", "2002"], "0202"], 6),
        ([["8887", "8889", "8878", "8898", "8788", "8988", "7888", "9888"], "8888"], -1),
        ([["8888"], "0009"], 1),
        ([["0000"], "8888"], -1),
        ([["6687", "6766", "7776", "6886", "6768", "8877", "6878", "7876", "6866", "6876", "7687", "7787", "8878",
           "7866", "6677", "6667", "8887", "7867", "8678", "6677", "8866", "8788", "7688", "7667", "8786", "8767",
           "6788", "8876", "7868", "8778", "8687", "6768", "6876", "7887", "7767", "7686", "7887", "6668", "6686",
           "6668", "6766", "6886", "6777", "6867", "8887", "7666", "8676", "7868", "6767", "8866", "7686", "7868",
           "7866", "7866", "7778", "6668", "8676", "8668", "8868", "7666", "6788", "7778", "8667", "7778", "6678",
           "6887", "7867", "6686", "7678", "8666", "8886", "8666", "6878", "7778", "7786", "8786", "8666", "8866",
           "6687", "8767", "6766", "6668", "7786", "7887", "6686", "8767", "7766", "7676", "8668", "8786", "8866",
           "6668", "6666", "6886", "6788", "8687", "6866", "6687", "6768", "6776", "7776", "8766", "7887", "6678",
           "6878", "8787", "8687", "6887", "8788", "8886", "8887", "7767", "8888", "8688", "8767", "8787", "7867",
           "7677", "7686", "6887", "7778", "8788", "7778", "6688", "6668", "7867", "8876", "6877", "6886", "8678",
           "8787", "7678", "8888", "8866", "6877", "6868", "7688", "7688", "6888", "8687", "6668", "6688", "7887",
           "6886", "6766", "8877", "8877", "7676", "7778", "8687", "6677", "6768", "8678", "6867", "7787", "7778",
           "6676", "7686", "7778", "8768", "8668", "7867", "6886", "8877", "6887", "8768", "6768", "6687", "8867",
           "7877", "8778", "7867", "8688", "6688", "6767", "7886", "6888", "8876", "7677", "7887", "8876", "8866",
           "7668", "8766", "6887", "8678", "6776", "8786", "6886", "8788", "7867", "7868", "7666", "7878", "7878",
           "6886", "7667", "6878", "8887", "7776", "7776", "8887", "7878", "8688", "7787", "8677", "8878", "8887",
           "8768", "8877", "8678", "8768", "7688", "6866", "8787", "7887", "6877", "6867", "7887", "7868", "8776",
           "6866", "7767", "6666", "6868", "8688", "7666", "7786", "8776", "8686", "6678", "6878", "7768", "6878",
           "6687", "7786", "6668", "7688", "7887", "6886", "8788", "6787", "7766", "6878", "6687", "8868", "6868",
           "7666", "6788", "8786", "8676", "8777", "7766", "8677", "7667", "6777", "7777", "8877", "8878", "8887",
           "7878", "6768", "7666", "7887", "8687", "8667", "8878", "8678", "7688", "6688", "8778", "7876", "8778",
           "8778", "6677", "6767", "8868", "6676", "8687", "7686", "7767", "6766", "7888", "6678", "8787", "8878",
           "6768", "7877", "8868", "6676", "6666", "6668", "8868", "7777", "6888", "7787", "6887", "8677", "7768",
           "7766", "8887", "6887", "7668", "8787", "8888", "6668", "6777", "7666", "7666", "6687", "8686", "6668",
           "6676", "8787", "6666", "8876", "7876", "7787", "7688", "6788", "7887", "8778", "6866", "8768", "7788",
           "8766", "6678", "6766", "8788", "8888", "7878", "8768", "6887", "8886", "8876", "7788", "6777", "8767",
           "7788", "6787", "6668", "6666", "7688", "8678", "6878", "8676", "6768", "7666", "7867", "7676", "6687",
           "8688", "8768", "6868", "6666", "8687", "6768", "8687", "7877", "6777", "7878", "8867", "8867", "7866",
           "6677", "7667", "8676", "7668", "7768", "7788", "7687", "7878", "7766", "7868", "8766", "6888", "6886",
           "7786", "8678", "8676", "8668", "7778", "8878", "7678", "7687", "8668", "7767", "7886", "6667", "7867",
           "7776", "6786", "7778", "7886", "8787", "6668", "7786", "8776", "6867", "6878", "7867", "8778", "7767",
           "7878", "8876", "7867", "7686", "8776", "6768", "8788", "8666", "8867", "8687", "7788", "6878", "7886",
           "8688", "8866", "8686", "6788", "8886", "6676", "8778", "8676", "6787", "6777", "7688", "6668", "6877",
           "6686", "7876", "7778", "8667", "7887", "6787", "8778", "6777", "6676", "7688", "6678", "7668", "7768",
           "7688", "7778", "8867", "6787", "6867", "7767", "7767", "7688", "8778", "6767", "8877", "6678", "6886",
           "6877", "6686", "7667", "6786", "8666", "6786", "7687", "7666", "8767", "6786", "7888", "6886", "8678",
           "7886", "7767", "8777", "7676", "7686", "6867", "6668", "6677", "6766", "8788", "7868", "6876", "6686",
           "8787", "6877", "8876", "8776", "6878", "8676", "7667", "6776", "6886", "7766", "7676", "6886", "8687",
           "6887", "8687", "8777", "6687", "8866", "8886"], "6778"], 12),
    )
    def test_solution(self, args, output):
        response = self.solution.openLock(*args)
        self.assertEqual(output, response, "\n\nexpected: {} \n actual: {}\n".format(output, response))
