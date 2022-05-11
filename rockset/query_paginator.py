from rockset import RocksetClient
from rockset.exceptions import RocksetException
from rockset.models import QueryResponse


class QueryPaginator:
    def __init__(self, client: RocksetClient, query_response: QueryResponse):
        self._client = client
        if hasattr(query_response, "query_errors") and query_response.query_errors:
            raise RocksetException(f"Provided query has errors: {query_response.query_errors}")
        if not hasattr(query_response, "query_id"):
            raise RocksetException("Provided query did not include the query_id field.")

        self._query_response = query_response
        self._query_id = query_response.query_id
        self._num_docs = len(query_response.results)
        self._current_results = query_response.results

        if hasattr(query_response, "pagination") and hasattr(query_response.pagination, "next_cursor") and query_response.pagination:
            self._next_cursor = query_response.pagination.next_cursor
        else:
            self._next_cursor = None

    def __iter__(self):
        return self

    def __next__(self):
        if not self._current_results:
            raise StopIteration

        current_results = self._current_results

        if self._next_cursor:
            next_query = self._client.Queries.get_query_results(query_id=self._query_id, cursor=self._next_cursor, docs=self._num_docs)
            self._current_results = next_query.results
            self._next_cursor = next_query.pagination.next_cursor if hasattr(next_query.pagination, "next_cursor") else None
        else:
            self._current_results = None

        return current_results
        
    def current_results(self):
        return self._current_results

    def initial_query_response(self):
        return self._query_response
        