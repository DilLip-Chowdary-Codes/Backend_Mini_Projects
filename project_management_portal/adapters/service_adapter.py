# from ib_common.service_adapter_utils.base_adapter_class import BaseAdapterClass

class ServiceAdapter:
    
    @property
    def user_service(self):
        from .user_service import UserService
        return UserService()

def get_service_adapter():
    return ServiceAdapter()
