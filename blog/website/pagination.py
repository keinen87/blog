class Pagination():
    LIMIT = 2
    def get_data(self, qs, page):
        if page == 0 or page == 1:
            return qs[:self.LIMIT]
        elif page > 1:
            page = page - 1
            offset = self.LIMIT * page
            return qs[offset: offset + self.LIMIT]

