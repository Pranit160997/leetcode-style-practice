from collections import Counter, deque
import heapq
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Write your solution here
        # use max heap to make the most freq task avl
        # use queue to process
        freq_dict = Counter(tasks)
        max_heap = [-freq for _, freq in freq_dict.items()]

        heapq.heapify(max_heap) #(-3, -3)
        q = deque()
        time = 0

        while max_heap or q:
            time += 1

            if max_heap:
                ct = heapq.heappop(max_heap)
                freq = 1 + ct
                if freq:
                    q.append([freq, time + n]) # ([-2, 3])

            if q:
                if q[0][1] == time:
                    freq, _ = q.popleft()
                    heapq.heappush(max_heap, freq)

        return time
        

def run_tests():
    solution = Solution()

    tests = [
        # Basic
        (["A","A","A","B","B","B"], 2, 8),

        # No cooldown
        (["A","A","A","B","B","B"], 0, 6),

        # Single task
        (["A"], 100, 1),

        # Only one task type
        (["A","A","A","A"], 2, 10),

        # All unique - cooldown irrelevant
        (["A","B","C","D","E"], 100, 5),

        # Dominant A, but enough fillers
        (["A","A","A","A","B","C","D","E"], 1, 8),

        # Dominant A, not enough fillers
        (["A","A","A","A","B","C"], 2, 10),

        # Multiple equally dominant tasks
        (["A","A","A","B","B","B","C","C","C"], 2, 9),

        # Several max-frequency tasks
        (["A","A","A","B","B","B","C","C","C","D","D","D"], 3, 12),

        # Large cooldown
        (["A","A","A","B","B","B"], 50, 104),

        # Two copies, huge cooldown
        (["A","A"], 100, 102),

        # Multiple tasks, large cooldown
        (["A","A","B","B","C","C"], 3, 7),

        # Earlier edge case
        (["B","C","D","A","A","A","A","G"], 1, 8),

        # Dominant frequency causes lots of idle
        (["A","A","A","A","A","B","C"], 2, 13),

        # Enough tasks to completely fill gaps
        (["A","A","A","B","B","B","C","C","D","D"], 2, 10),

        # Cooldown exactly filled by other types
        (["A","A","B","B"], 1, 4),

        # Cooldown larger than available filler
        (["A","A","B","B"], 3, 6),

        # One dominant + many unique fillers
        (["A","A","A","A","A","B","C","D","E","F","G","H","I"], 2, 13),

        # Many equal-frequency tasks, cooldown irrelevant
        (
            ["A","A","B","B","C","C","D","D","E","E"],
            2,
            10
        ),

        # Stress-style dominant task
        (
            ["A"] * 10 + ["B"] * 3 + ["C"] * 2,
            3,
            37
        ),
    ]

    passed = 0
    failed = 0

    for i, (tasks, n, expected) in enumerate(tests, 1):
        result = solution.leastInterval(tasks, n)

        if result == expected:
            passed += 1
            print(f"Test {i}: PASS")
        else:
            failed += 1
            print(
                f"Test {i}: FAIL | "
                f"tasks={tasks}, n={n} | "
                f"expected={expected} | got={result}"
            )

    print(f"\nResults: {passed}/{len(tests)} passed, {failed} failed")


if __name__ == "__main__":
    run_tests()