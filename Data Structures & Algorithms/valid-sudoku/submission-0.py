from math import sqrt


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Each horizontal, vertical, and box is a hashmap, taking shape:
        #
        #  row_id -> set(nums)
        #  col_id -> set(nums)
        #  box_id -> set(nums)
        #
        # We build these three maps simultaneously, iterating in one O(n^2)
        # pass over each matrix cell. On each iteration, we also check validity
        # before we insert into the hashmaps, short-circuiting `False` if
        # we see a duplicate value in any of our hashmaps.
        #
        # It follows that checking board validity is implicit. If we made it
        # to the end of the full board scan and never found a duplicate, we
        # know the board must be valid.

        rows: dict[int, set[str]] = dict()  # row index -> set of nums in row
        cols: dict[int, set[str]] = dict()  # col index -> set of nums in col

        # Box identifer is a downsampled 2-tuple, which is immutable
        # and works as a stable hash key.
        boxes: dict[tuple[int, int], set[str]] = dict()  # box index -> set of nums in box

        # Making the assumption that board length is a perfect square
        box_len = int(sqrt(len(board)))

        for row_idx, row in enumerate(board):
            for col_idx, cell in enumerate(row):
                if cell == ".":  # Ignore empty "." cells
                    continue

                # 0. Compute box identifier
                box_id = (row_idx // box_len, col_idx // box_len)

                # 1. Check if we have duplicates in any of the maps
                try:
                    if cell in rows[row_idx]:
                        return False
                except KeyError:
                    pass  # Ignore
                try:
                    if cell in cols[col_idx]:
                        return False
                except KeyError:
                    pass  # Ignore
                try:
                    if cell in boxes[box_id]:
                        return False
                except KeyError:
                    pass  # Ignore

                # 2. Insert into the maps

                if row_idx not in rows:
                    rows[row_idx] = {cell}
                else:
                    rows[row_idx].add(cell)

                if col_idx not in cols:
                    cols[col_idx] = {cell}
                else:
                    cols[col_idx].add(cell)

                if box_id not in boxes:
                    boxes[box_id] = {cell}
                else:
                    boxes[box_id].add(cell)

        return True
