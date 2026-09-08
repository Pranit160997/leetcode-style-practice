import heapq
from typing import Counter, List


class Solution:
    def mostActiveDevices(self, events: List[int], k: int) -> List[int]:
        # Write your solution here
        # return top k active devices
        # create a dict of frequency
        # heapify this dict on highest frequency
        # pop until k
        # return res
        freq_dict = {}
        for e in events:
            if e in freq_dict:
                freq_dict[e] += 1
            else:
                freq_dict[e] = 1

        heap = []
        res = []

        for element in freq_dict.items():
            event, freq = element
            heapq.heappush(heap, (freq, event))

            if len(heap) > k:
                heapq.heappop(heap)

        while heap:
            freq, event = heapq.heappop(heap)
            res.append(event)

        return res

def run_tests():
    solution = Solution()

    tests = [
        # (events, k, expected_as_set)
        ([4, 1, 2, 2, 3, 3, 3, 4, 4, 4], 2, {4, 3}),
        ([7], 1, {7}),
        ([5, 5, 8, 8, 8, 2, 2, 2, 2], 2, {2, 8}),
        ([1, 1, 1, 2, 2, 3], 1, {1}),
        ([9, 9, 8, 8, 7, 7, 7], 2, {7, 9}),  # 9 and 8 tie; this test is intentionally avoided below
        ([1, 2, 3, 4], 4, {1, 2, 3, 4}),
        ([6, 6, 6, 6], 1, {6}),
        ([10, 10, 20, 20, 20, 30], 2, {10, 20}),
    ]

    # Remove the ambiguous tie case from strict testing.
    tests = [t for i, t in enumerate(tests) if i != 4]

    passed = 0
    failed = 0

    for i, (events, k, expected) in enumerate(tests, 1):
        result = solution.mostActiveDevices(events, k)

        if len(result) == k and set(result) == expected:
            passed += 1
            print(f"Test {i}: PASS")
        else:
            failed += 1
            print(
                f"Test {i}: FAIL | "
                f"events={events}, k={k} | "
                f"expected={expected} | "
                f"got={result}"
            )

    print(f"\nResults: {passed}/{len(tests)} passed, {failed} failed")


if __name__ == "__main__":
    run_tests()