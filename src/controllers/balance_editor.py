from src.models.interfaces.user_repository import UserRepositoryInterface
class BalanceEditor:
    def __init__(self, user_repository: UserRepositoryInterface):
        self.__user_repository = user_repository
        
    def edit(self,user_id:int,balance:float) -> dict:
        self.__user_repository.update_balance(user_id,balance)
        return {
            "type": "User",
            "count": 1,
            "new_balance": balance
        }