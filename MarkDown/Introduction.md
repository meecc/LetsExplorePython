
# What is REST
------

REST stands for Representational State Transfer. (It is sometimes spelled "ReST".) It relies on a stateless, client-server, cacheable communications protocol -- and in virtually all cases, the HTTP protocol is used.

REST is an architecture style for designing networked applications. The idea is that, rather than using complex mechanisms such as CORBA, RPC or SOAP to connect between machines, simple HTTP is used to make calls between machines.

> REST is a simple way to organize interactions between independent systems.

> In many ways, the World Wide Web itself, based on HTTP, can be viewed as a REST-based architecture.

## RESTful Web Services 
RESTful Web Services are REST architecture based web services. In REST Architecture everything is a resource. RESTful web services are light weight, highly scalable and maintainable and are very commonly used to create APIs for web based applications.


## HTTP Verbs

### GET 
GET is the simplest type of HTTP request method; the one that browsers use each time you click a link or type a URL into the address bar. It instructs the server to transmit the data identified by the URL to the client. Data should never be modified on the server side as a result of a GET request. In this sense, a GET request is read-only, but of course, once the client receives the data, it is free to do any operation with it on its own side - for instance, format it for display.

### POST
POST is used when the processing you wish to happen on the server should be repeated, if the POST request is repeated (that is, they are not idempotent; more on that below). In addition, POST requests should cause processing of the request body as a subordinate of the URL you are posting to.

In plain words:

    >  POST /clients/

should not cause the resource at /clients/, itself, to be modified, but a resource whose URL starts with /clients/. For instance, it could append a new client to the list, with an id generated by the server.

    > /clients/some-unique-id

PUT requests are used easily instead of POST requests, and vice versa. Some systems use only one, some use POST for create operations, and PUT for update operations (since with a PUT request you always supply the complete URL), some even use POST for updates and PUT for creates.

Often, POST requests are used to trigger operations on the server, which do not fit into the Create/Update/Delete paradigm; but this, however, is beyond the scope of REST. In our example, we'll stick with PUT all the way.

### DELETE
DELETE should perform the contrary of PUT; it should be used when you want to delete the resource identified by the URL of the request.
	
> ```curl -v -X DELETE /clients/anne```

This will delete all data associated with the resource, identified by ```/clients/anne```

### PUT 
A PUT request is used when you wish to create or update the resource identified by the URL. For example,
1
	
> ```PUT /clients/robin```


might create a client, called Robin on the server. You will notice that REST is completely backend agnostic; there is nothing in the request that informs the server how the data should be created - just that it should. This allows you to easily swap the backend technology if the need should arise. PUT requests contain the data to use in updating or creating the resource in the body. In cURL, you can add data to the request with the -d switch.

	
> ```curl -v -X PUT -d "some text"```

### 


```python

```