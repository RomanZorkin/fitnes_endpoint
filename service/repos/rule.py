from service.models import Endpoint


class EndpointRepo:

    def get_all(self) -> Endpoint:
        return Endpoint.query.all()

    def get_by_uid(self, uid: int) -> Endpoint:
        endpoint: Endpoint = Endpoint.query.filter_by(id=uid).first()
        if not endpoint:
            return False
        return endpoint