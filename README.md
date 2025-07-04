## OpenApiTestPlayground
Creating a restAPI/OpenAPI test playground, with the objective of having functional rest endpoints that I can write both manual and automated scripts.

Hoping to use Python.....

#### Token: (Not implemented)
  - GET `/orders/token`
      - Response: Token
  - DEL `/orders/token`
      - Response: Success

#### Order Inquiry:
  -  GET `/order/query`
      - Expect: json payload with limited order variables.
      - Response: Complete order details.

#### Order Data:
  - POST `orders/upload`
      - Expect: json payload
      - Response: order number
  - GET  `orders/{orderId}`
      - Response: Order payload
  - PATCH `orders/{orderId}`
      - Expect: json payload
      - Response: Order # 
  - DEL `orders/{orders}`
      - Response: success
   
OpenAPI doc: https://www.apicur.io/studio/getting-started/

Current resources:
- https://www.youtube.com/playlist?list=PLTCFnfWaEOP2OgHq7qoe2PENmFDZ0sqBa

- https://learn.openapis.org/
- https://dredd.org/en/latest/
- https://schemathesis.readthedocs.io/en/stable/
- https://docs.tracecov.sh/
- https://upptime.js.org/
- https://k6.io/
- https://www.karatelabs.io/


### Reference commands:
#### Apicur: 

docker pull quay.io/apicurio/apicurio-studio:1.0.0.Beta1
docker pull quay.io/apicurio/apicurio-studio-ui:1.0.0.Beta1

docker run -it -p 8080:8080 quay.io/apicurio/apicurio-studio:1.0.0.Beta1
docker run -it -p 8888:8080 quay.io/apicurio/apicurio-studio-ui:1.0.0.Beta1

#### Python:
uvicorn main:app --reload