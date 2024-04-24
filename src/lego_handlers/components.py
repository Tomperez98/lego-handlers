"""Lego handlers components."""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Generic, TypeVar

from result import Result


class DomainError(Exception):
    """Raised when business rule has been violated."""


@dataclass(frozen=True)
class ResponseComponent:
    """Handler response data."""


@dataclass(frozen=True)
class DomainEvent(ABC):
    """Domain Event."""

    @abstractmethod
    async def publish(self) -> None:
        """Publish event."""


DE = TypeVar("DE", bound=DomainEvent)
R = TypeVar("R", bound=ResponseComponent)
E = TypeVar("E", bound=DomainError)


@dataclass(frozen=True)
class AsyncCommandComponent(ABC, Generic[DE, E, R]):
    """Handler async command."""

    @abstractmethod
    async def run(self, events: list[DE]) -> Result[R, E]:
        """Async execute command."""


@dataclass(frozen=True)
class CommandComponent(ABC, Generic[DE, E, R]):
    """Handler command."""

    @abstractmethod
    def run(self, events: list[DE]) -> Result[R, E]:
        """Execute command."""
