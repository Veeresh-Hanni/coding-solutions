class SQL:

    def __init__(self, names: list[str], columns: list[int]):
        self.tables = {}      # Stores table data: name -> {rowId: [values]}
        self.col_counts = {}  # Stores expected columns: name -> column count
        self.next_id = {}     # Stores next rowId for each table, starting at 1
        
        for name, col_count in zip(names, columns):
            self.col_counts[name] = col_count
            self.tables[name] = {}
            self.next_id[name] = 1

    def ins(self, name: str, row: list[str]) -> bool:
        # Check if table is valid and row length matches expected columns
        if name not in self.col_counts:
            return False
        if len(row) != self.col_counts[name]:
            return False
        
        row_id = self.next_id[name]
        self.next_id[name] += 1
        
        self.tables[name][row_id] = row
        return True
        
    def rmv(self, name: str, rowId: int) -> None:
        if name in self.tables and rowId in self.tables[name]:
            del self.tables[name][rowId]

    def sel(self, name: str, rowId: int, columnId: int) -> str:
        if name not in self.tables:
            return "<null>"
        if rowId not in self.tables[name]:
            return "<null>"
        
        row = self.tables[name][rowId]
        if columnId < 1 or columnId > len(row):
            return "<null>"
            
        return row[columnId - 1]

    def exp(self, name: str) -> list[str]:
        if name not in self.tables:
            return []
            
        result = []
        # Sort by rowId to maintain proper order
        for row_id in sorted(self.tables[name].keys()):
            row_vals = [str(row_id)] + self.tables[name][row_id]
            result.append(",".join(row_vals))
            
        return result