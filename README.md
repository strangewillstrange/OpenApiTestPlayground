# OpenApiTestPlayground
Creating a restAPI/OpenAPI test playground, with the objective of having functional rest endpoints that I can write both manual and automated scripts.

Hoping to use Python.....

### Token:
  - GET `/orders/token`
      - Response: Token
  - DEL `/orders/token`
      - Response: Success

### Order Inquiry:
  -  GET `/order/details`
      - Expect: Limited order variables.
      - Response: Complete order details.

### Order Data:
  - POST `orders/`
      - Expect: json payload
      - Response: order number
  - PATCH `orders/{orderNumber}`
      - Expect: json payload
      - Response: Order # 
  - DEL `orders/{orders}`
      - Response: success
   

Current resources:
- https://www.youtube.com/playlist?list=PLTCFnfWaEOP2OgHq7qoe2PENmFDZ0sqBa

- https://learn.openapis.org/
- https://dredd.org/en/latest/
- https://schemathesis.readthedocs.io/en/stable/
- https://docs.tracecov.sh/
- https://upptime.js.org/
- https://k6.io/
- https://www.karatelabs.io/
