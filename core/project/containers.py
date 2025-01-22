from functools import lru_cache

import punq

from core.apps.customers.services.auth import AuthService, BaseAuthService
from core.apps.customers.services.codes import (BaseCodeService,
                                                DjangoCacheCodeService)
from core.apps.customers.services.customers import (BaseCustomerService,
                                                    ORMCustomerService)
from core.apps.customers.services.sender import (BaseSenderService,
                                                 ConsoleSenderService)
from core.apps.products.services.products import (BaseProductService,
                                                  ORMProductService)


@lru_cache(1)
def get_container() -> punq.Container:
    return _initialize_container()
    
def _initialize_container() -> punq.Container:
    container: punq.Container = punq.Container()
    
    #init product service
    container.register(BaseProductService, ORMProductService)
    
    #init customer services
    container.register(BaseSenderService, ConsoleSenderService)
    container.register(BaseCodeService, DjangoCacheCodeService)
    container.register(BaseCustomerService, ORMCustomerService)
    container.register(BaseAuthService, AuthService)
    
    
    return container