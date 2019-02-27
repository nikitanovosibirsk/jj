from typing import Union, Tuple, Dict, List

from .attribute_matchers import AttributeMatcher, EqualMatcher, RouteMatcher, MultiDictMatcher
from .resolvable_matcher import ResolvableMatcher
from ..resolvers import Resolver
from ..requests import Request


__all__ = ("RequestMatcher", "MethodMatcher", "PathMatcher",
           "HeaderMatcher", "ParamMatcher")


StrOrAttrMatcher = Union[
    str,
    AttributeMatcher
]
DictOrTupleListOrAttrMatcher = Union[
    Dict[str, StrOrAttrMatcher],
    List[Tuple[str, StrOrAttrMatcher]],
    AttributeMatcher,
]


class RequestMatcher(ResolvableMatcher):
    pass


class MethodMatcher(RequestMatcher):
    def __init__(self, resolver: Resolver, method: StrOrAttrMatcher) -> None:
        super().__init__(resolver)
        self._matcher = method if isinstance(method, AttributeMatcher) else EqualMatcher(method)

    async def match(self, request: Request) -> bool:
        return self._matcher.match("*") or self._matcher.match(request.method)


class PathMatcher(RequestMatcher):
    def __init__(self, resolver: Resolver, path: StrOrAttrMatcher) -> None:
        super().__init__(resolver)
        self._matcher = path if isinstance(path, AttributeMatcher) else RouteMatcher(path)

    async def match(self, request: Request) -> bool:
        return self._matcher.match(request.path)


class ParamMatcher(RequestMatcher):
    def __init__(self, resolver: Resolver, params: DictOrTupleListOrAttrMatcher) -> None:
        super().__init__(resolver)
        if isinstance(params, AttributeMatcher):
            self._matcher = params
        else:
            self._matcher = MultiDictMatcher(params)

    async def match(self, request: Request) -> bool:
        return self._matcher.match(request.query)


class HeaderMatcher(RequestMatcher):
    def __init__(self, resolver: Resolver, headers: DictOrTupleListOrAttrMatcher) -> None:
        super().__init__(resolver)
        if isinstance(headers, AttributeMatcher):
            self._matcher = headers
        else:
            self._matcher = MultiDictMatcher(headers)

    async def match(self, request: Request) -> bool:
        return self._matcher.match(request.headers)
