"""
Paginator
"""

__NAME__ = "Paginator"
__version__ = "0.1.1"
__license__ = "MIT"
__author__ = "Mardix"
__copyright__ = "(c) 2015 Mardix"

from math import ceil
from six import string_types


class Paginator(object):
    PER_PAGE = 10
    showing = 0
    total_pages = 0
    total_items = 0

    def __init__(self, query, page=1, per_page=PER_PAGE, total=None,
                 padding=0, on_error=None):
        """

        :param query: Iterable to paginate. Can be a query object, list or any iterables
        :param page: current page
        :param per_page: max number of items per page
        :param total: Max number of items. If not provided, it will use the query to count
        :param padding: Number of elements of the next page to show
        :param on_error: Used if the page number is too big for the total number
        of items. Raised if it's an exception, called otherwise.
        ``None`` by default.
        :return:
        """

        self.query = query

        if not isinstance(per_page, int) or per_page < 1:
            raise TypeError('`per_page` must be a positive integer')
        self.per_page = per_page

        if not total:
            try:
                total = query.count()
            except (TypeError, AttributeError):
                total = len(query)
        self.total_items = total

        if page == "last":
            page == self.total_pages
        elif page == "first":
            page = 1
        self.page = self._sanitize_page_number(page)

        if self.total_items > self.per_page * self.page:
            showing = self.per_page
        else:
            showing = total - per_page * (page - 1)
        self.showing = showing

        self.padding = padding

        if self.showing == 0 and on_error:
            if isinstance(on_error, Exception):
                raise on_error

    def _sanitize_page_number(self, page):
        if page == 'last':
            return page
        if isinstance(page, string_types) and page.isdigit():
            page = int(page)
        if isinstance(page, int) and (page > 0):
            return page
        return 1

    @property
    def total_pages(self):
        """The total number of pages."""
        return int(ceil(self.total_items / float(self.per_page)))

    @property
    def has_prev(self):
        """True if a previous page exists."""
        return self.page > 1

    @property
    def has_next(self):
        """True if a next page exists."""
        return self.page < self.total_pages

    @property
    def next_page_number(self):
        """Number of the next page."""
        return self.page + 1

    @property
    def prev_page_number(self):
        """Number of the previous page."""
        return self.page - 1

    @property
    def pages_range(self):
        start = (self.page - 1) * self.per_page
        end = start + self.per_page - 1
        return start, min(end, self.total_items - 1)

    @property
    def items(self):
        offset = (self.page - 1) * self.per_page
        offset = max(offset - self.padding, 0)
        limit = self.per_page + self.padding
        if self.page > 1:
            limit = limit + self.padding

        if hasattr(self.query, 'limit') and hasattr(self.query, 'offset'):
            return self.query.limit(limit).offset(offset)
        return self.query[offset:offset + limit]

    def __iter__(self):
        for i in self.items:
            yield i

    @property
    def pages(self):
        """Iterates over the page numbers in the pagination."""
        return self.iter_pages()

    def iter_pages(self, left_edge=2, left_current=3, right_current=4, right_edge=2):
        last = 0
        for num in xrange(1, self.total_pages + 1):
            is_active_page = (
                num <= left_edge
                or (
                    (num >= self.page - left_current) and
                    (num < self.page + right_current)
                )
                or (
                    (num > self.total_pages - right_edge)
                )
            )
            if is_active_page:
                if last + 1 != num:
                    yield None
                yield num
                last = num
