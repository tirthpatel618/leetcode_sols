class Spreadsheet:

    def __init__(self, rows: int):
        self.cols = 26
        self.sheet = [[None]] * self.cols
        self.rows = rows
          
    def setCell(self, cell: str, value: int) -> None:
        r = int(cell[1:]) - 1
        c = ord(cell[0]) - ord('A')
        if r >= self.rows or c >= self.cols:
            return
        self.sheet[r][c] = value
    def resetCell(self, cell: str) -> None:
        r = int(cell[1:]) - 1
        c = ord(cell[0]) - ord('A')
        if r >= self.rows or c >= self.cols:
            return
        self.sheet[r][c] = None
'''
    def setCell(self, cell: str, value: int) -> None:
        

    def resetCell(self, cell: str) -> None:
        

    def getValue(self, formula: str) -> int:
'''




# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)