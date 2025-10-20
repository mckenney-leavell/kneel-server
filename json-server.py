from http.server import HTTPServer
from nss_handler import HandleRequests, status

from views import get_all_orders

class JSONServer(HandleRequests):

    def do_GET(self):

        response_body = ""
        url = self.parse_url(self.path)

        if url["requested_resource"] == "orders":
            response_body = get_all_orders()
            return self.response(response_body, status.HTTP_200_SUCCESS.value)
        
        return self.response(
            "Requested resource not found",
            status.HTTP_404_CLIENT_ERROR_RESOURCE_NOT_FOUND.value,
        )


def main():
    host = ""
    port = 8001
    HTTPServer((host, port), JSONServer).serve_forever()


if __name__ == "__main__":
    main()
