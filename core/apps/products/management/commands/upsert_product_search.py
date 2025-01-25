from django.core.management import BaseCommand
from django.core.management.base import CommandParser
from typing import Any
from core.apps.products.use_cases.search.upsert_search_data import UpsertSearchDataUseCase
from core.project.containers import get_container
from punq import Container


class Command(BaseCommand):
    
    def handle(self, *args: Any, **options: Any) -> str | None:
        container: Container = get_container()
        
        use_case: UpsertSearchDataUseCase = container.resolve(UpsertSearchDataUseCase)
        use_case.execute()
