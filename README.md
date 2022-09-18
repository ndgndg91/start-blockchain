# Start Blockchain Demo

1. run node1, node2, node3
2. call /get_chain to node1, node2, node3
    <pre><h3>curl -i 'http://localhost:8080/get_chain'</h3>
   HTTP/1.1 200 OK
   Server: Werkzeug/2.2.2 Python/3.9.13
   Date: Mon, 12 Sep 2022 12:13:00 GMT
   Content-Type: application/json
   Content-Length: 123
   Connection: close

   {"chain":[{"index":1,"previous_hash":"0","proof":1,"timestamp":"2022-09-12 21:12:37.403359","transaction":[]}],"length":1}

   <h3>curl -i 'http://localhost:8081/get_chain'</h3>
   HTTP/1.1 200 OK
   Server: Werkzeug/2.2.2 Python/3.9.13
   Date: Mon, 12 Sep 2022 12:13:00 GMT
   Content-Type: application/json
   Content-Length: 123
   Connection: close

   {"chain":[{"index":1,"previous_hash":"0","proof":1,"timestamp":"2022-09-12 21:12:39.834801","transaction":[]}],"length":1}
   
   <h3>curl -i 'http://localhost:8082/get_chain'</h3>
   HTTP/1.1 200 OK
   Server: Werkzeug/2.2.2 Python/3.9.13
   Date: Mon, 12 Sep 2022 12:13:00 GMT
   Content-Type: application/json
   Content-Length: 123
   Connection: close

   {"chain":[{"index":1,"previous_hash":"0","proof":1,"timestamp":"2022-09-12 21:12:42.185377","transaction":[]}],"length":1}
   </pre>
3. call /connect_node to node1, node2, node3 using each nodes1.json, nodes2.json, nodes3.json
    <pre><h3>curl -i -X POST 'http://localhost:8080/connect_node'\
    --header 'Content-Type: application/json'\
    -d'{"nodes": ["http://localhost:8081","http://localhost:8082"]}'</h3>
   HTTP/1.1 201 CREATED
   Server: Werkzeug/2.2.2 Python/3.9.13
   Date: Mon, 12 Sep 2022 12:15:27 GMT
   Content-Type: application/json
   Content-Length: 133
   Connection: close

   {"message":"All the nodes are now connected. The giricoins the followings nodes:","total_nodes":["localhost:8082","localhost:8081"]}
   
   <h3>curl -i -X POST 'http://localhost:8081/connect_node'\
    --header 'Content-Type: application/json'\
    -d'{"nodes": ["http://localhost:8080","http://localhost:8082"]}'</h3>
   HTTP/1.1 201 CREATED
   Server: Werkzeug/2.2.2 Python/3.9.13
   Date: Mon, 12 Sep 2022 12:16:01 GMT
   Content-Type: application/json
   Content-Length: 133
   Connection: close

   {"message":"All the nodes are now connected. The giricoins the followings nodes:","total_nodes":["localhost:8082","localhost:8080"]}
   
   <h3>curl -i -X POST 'http://localhost:8082/connect_node'\
    --header 'Content-Type: application/json'\
    -d'{"nodes": ["http://localhost:8080","http://localhost:8081"]}'</h3>
   HTTP/1.1 201 CREATED
   Server: Werkzeug/2.2.2 Python/3.9.13
   Date: Mon, 12 Sep 2022 12:16:01 GMT
   Content-Type: application/json
   Content-Length: 133
   Connection: close

   {"message":"All the nodes are now connected. The giricoins the followings nodes:","total_nodes":["localhost:8080","localhost:8081"]}
   </pre>
4. call /mine_block to node1 then call /get_chain node1 then call /get_chain node2, node3
    <pre><h2>you can check different chains node1, node2, node3</h2>
   <h3>curl -i 'http://localhost:8080/mine_block'</h3>
   HTTP/1.1 200 OK
   Server: Werkzeug/2.2.2 Python/3.9.13
   Date: Mon, 12 Sep 2022 12:20:43 GMT
   Content-Type: application/json
   Content-Length: 293
   Connection: close

   {"index":2,"message":"Congratulations, you just mined a block!","previous_hash":"258f54a9203f048947c82db023de3f98969e160cff041fbb38f674d5ee4da3e5","proof":533,"timestamp":"2022-09-12 21:20:43.592232","transactions":[{"amount":1,"receiver":"giri","sender":"79ece563c40f488e88a2a95d3939e18b"}]}
   
   <h3>curl -i 'http://localhost:8080/get_chain'</h3>
   HTTP/1.1 200 OK
   Server: Werkzeug/2.2.2 Python/3.9.13
   Date: Mon, 12 Sep 2022 12:21:14 GMT
   Content-Type: application/json
   Content-Length: 364
   Connection: close

   {
      "chain":[
         {"index":1,"previous_hash":"0","proof":1,"timestamp":"2022-09-12 21:20:01.060843","transactions":[]},
         {"index":2,"previous_hash":"258f54a9203f048947c82db023de3f98969e160cff041fbb38f674d5ee4da3e5","proof":533,"timestamp":"2022-09-12 21:20:43.592232","transactions":[{"amount":1,"receiver":"giri","sender":"79ece563c40f488e88a2a95d3939e18b"}]}],
      "length":2
   }

   <h3>curl -i 'http://localhost:8081/get_chain'</h3>
   HTTP/1.1 200 OK
   Server: Werkzeug/2.2.2 Python/3.9.13
   Date: Mon, 12 Sep 2022 12:24:09 GMT
   Content-Type: application/json
   Content-Length: 124
   Connection: close

   {"chain":[{"index":1,"previous_hash":"0","proof":1,"timestamp":"2022-09-12 21:20:04.344363","transactions":[]}],"length":1}

   
   <h3>curl -i 'http://localhost:8082/get_chain'</h3>
   HTTP/1.1 200 OK
   Server: Werkzeug/2.2.2 Python/3.9.13
   Date: Mon, 12 Sep 2022 12:24:24 GMT
   Content-Type: application/json
   Content-Length: 124
   Connection: close

   {"chain":[{"index":1,"previous_hash":"0","proof":1,"timestamp":"2022-09-12 21:20:06.692114","transactions":[]}],"length":1}
   </pre>
5. call /replace_chain to node2, node3
    <pre><h2>you can check all node has same chain</h2>
   <h3>curl -i 'http://localhost:8081/replace_chain'</h3>
   HTTP/1.1 200 OK
   Server: Werkzeug/2.2.2 Python/3.9.13
   Date: Mon, 12 Sep 2022 12:27:04 GMT
   Content-Type: application/json
   Content-Length: 461
   Connection: close

   {
      "chain":[
         {"index":1,"previous_hash":"0","proof":1,"timestamp":"2022-09-12 21:20:01.060843","transactions":[]},
         {"index":2,"previous_hash":"258f54a9203f048947c82db023de3f98969e160cff041fbb38f674d5ee4da3e5","proof":533,"timestamp":"2022-09-12 21:20:43.592232","transactions":[{"amount":1,"receiver":"giri","sender":"79ece563c40f488e88a2a95d3939e18b"}]}],
      "message":"The nodes had different chains so the chain was replaced by the longest chains.",
      "replaced":true
   }
   <h3>curl -i 'http://localhost:8082/replace_chain'</h3>
   HTTP/1.1 200 OK
   Server: Werkzeug/2.2.2 Python/3.9.13
   Date: Mon, 12 Sep 2022 12:27:16 GMT
   Content-Type: application/json
   Content-Length: 461
   Connection: close

   {
      "chain":[
         {"index":1,"previous_hash":"0","proof":1,"timestamp":"2022-09-12 21:20:01.060843","transactions":[]},
         {"index":2,"previous_hash":"258f54a9203f048947c82db023de3f98969e160cff041fbb38f674d5ee4da3e5","proof":533,"timestamp":"2022-09-12 21:20:43.592232","transactions":[{"amount":1,"receiver":"giri","sender":"79ece563c40f488e88a2a95d3939e18b"}]}],
      "message":"The nodes had different chains so the chain was replaced by the longest chains.",
      "replaced":true
   }
   </pre>
6. call /add_transaction to node1 using transaction.json
   <pre><h3>curl -i -X POST 'http://localhost:8080/add_transaction' \
   --header 'Content-Type: application/json' \
   -d '{"sender": "giri","receiver": "kate","amount": 100}'</h3>
   HTTP/1.1 201 CREATED
   Server: Werkzeug/2.2.2 Python/3.9.13
   Date: Mon, 12 Sep 2022 12:30:44 GMT
   Content-Type: application/json
   Content-Length: 56
   Connection: close

   {"message":"This transaction will be added to Block 3"}
   </pre>
7. call /mine_block to node1
   <pre><h3>curl -i 'http://localhost:8080/mine_block'</h3>
   HTTP/1.1 200 OK
   Server: Werkzeug/2.2.2 Python/3.9.13
   Date: Mon, 12 Sep 2022 12:31:33 GMT
   Content-Type: application/json
   Content-Length: 344
   Connection: close

   {"index":3,"message":"Congratulations, you just mined a block!","previous_hash":"e64179281ee43294d3b76ee9e46ac659db023b80d844d46f76e6b308d7b99482","proof":45293,"timestamp":"2022-09-12 21:31:33.409607","transactions":[{"amount":100,"receiver":"kate","sender":"giri"},{"amount":1,"receiver":"giri","sender":"79ece563c40f488e88a2a95d3939e18b"}]}
   </pre>
8. call /get_chain to node1
   <pre><h2>you can check node1 has chain with 3 length </h2>
   <h3>curl -i 'http://localhost:8080/get_chain'</h3>
   HTTP/1.1 200 OK
   Server: Werkzeug/2.2.2 Python/3.9.13
   Date: Mon, 12 Sep 2022 12:32:47 GMT
   Content-Type: application/json
   Content-Length: 655
   Connection: close

   {
      "chain":[
         {"index":1,"previous_hash":"0","proof":1,"timestamp":"2022-09-12 21:20:01.060843","transactions":[]},
         {"index":2,"previous_hash":"258f54a9203f048947c82db023de3f98969e160cff041fbb38f674d5ee4da3e5","proof":533,"timestamp":"2022-09-12 21:20:43.592232","transactions":[{"amount":1,"receiver":"giri","sender":"79ece563c40f488e88a2a95d3939e18b"}]},
         {"index":3,"previous_hash":"e64179281ee43294d3b76ee9e46ac659db023b80d844d46f76e6b308d7b99482","proof":45293,"timestamp":"2022-09-12 21:31:33.409607","transactions":[{"amount":100,"receiver":"kate","sender":"giri"},{"amount":1,"receiver":"giri","sender":"79ece563c40f488e88a2a95d3939e18b"}]}],
      "length":3
   }
   </pre>
9. call /get_chain to node2, node3
   <pre><h2>you can check node2 and node3 has different chains from node1 chain</h2>
   <h3>curl -i 'http://localhost:8081/get_chain'</h3>
   HTTP/1.1 200 OK
   Server: Werkzeug/2.2.2 Python/3.9.13
   Date: Mon, 12 Sep 2022 12:34:16 GMT
   Content-Type: application/json
   Content-Length: 364
   Connection: close

   {
      "chain":[
         {"index":1,"previous_hash":"0","proof":1,"timestamp":"2022-09-12 21:20:01.060843","transactions":[]},
         {"index":2,"previous_hash":"258f54a9203f048947c82db023de3f98969e160cff041fbb38f674d5ee4da3e5","proof":533,"timestamp":"2022-09-12 21:20:43.592232","transactions":[{"amount":1,"receiver":"giri","sender":"79ece563c40f488e88a2a95d3939e18b"}]}],
      "length":2
   }

   <h3>curl -i 'http://localhost:8082/get_chain'</h3>
   HTTP/1.1 200 OK
   Server: Werkzeug/2.2.2 Python/3.9.13
   Date: Mon, 12 Sep 2022 12:34:57 GMT
   Content-Type: application/json
   Content-Length: 364
   Connection: close

   {
      "chain":[
         {"index":1,"previous_hash":"0","proof":1,"timestamp":"2022-09-12 21:20:01.060843","transactions":[]},
         {"index":2,"previous_hash":"258f54a9203f048947c82db023de3f98969e160cff041fbb38f674d5ee4da3e5","proof":533,"timestamp":"2022-09-12 21:20:43.592232","transactions":[{"amount":1,"receiver":"giri","sender":"79ece563c40f488e88a2a95d3939e18b"}]}
      ],
      "length":2
   }
   </pre>
10. call /replace_chain to node2, node3
   <pre><h2>you can check all node has same chain</h2>
   <h3>curl -i 'http://localhost:8081/replace_chain'</h3>
   HTTP/1.1 200 OK
   Server: Werkzeug/2.2.2 Python/3.9.13
   Date: Mon, 12 Sep 2022 12:39:05 GMT
   Content-Type: application/json
   Content-Length: 752
   Connection: close

   {
      "chain":[
         {"index":1,"previous_hash":"0","proof":1,"timestamp":"2022-09-12 21:20:01.060843","transactions":[]},
         {"index":2,"previous_hash":"258f54a9203f048947c82db023de3f98969e160cff041fbb38f674d5ee4da3e5","proof":533,"timestamp":"2022-09-12 21:20:43.592232","transactions":[{"amount":1,"receiver":"giri","sender":"79ece563c40f488e88a2a95d3939e18b"}]},
         {"index":3,"previous_hash":"e64179281ee43294d3b76ee9e46ac659db023b80d844d46f76e6b308d7b99482","proof":45293,"timestamp":"2022-09-12 21:31:33.409607","transactions":[{"amount":100,"receiver":"kate","sender":"giri"},{"amount":1,"receiver":"giri","sender":"79ece563c40f488e88a2a95d3939e18b"}]}
      ],
      "message":"The nodes had different chains so the chain was replaced by the longest chains.",
      "replaced":true
   }

   <h3>curl -i 'http://localhost:8082/replace_chain'</h3>
   HTTP/1.1 200 OK
   Server: Werkzeug/2.2.2 Python/3.9.13
   Date: Mon, 12 Sep 2022 12:39:20 GMT
   Content-Type: application/json
   Content-Length: 752
   Connection: close

   {
      "chain":[
         {"index":1,"previous_hash":"0","proof":1,"timestamp":"2022-09-12 21:20:01.060843","transactions":[]},
         {"index":2,"previous_hash":"258f54a9203f048947c82db023de3f98969e160cff041fbb38f674d5ee4da3e5","proof":533,"timestamp":"2022-09-12 21:20:43.592232","transactions":[{"amount":1,"receiver":"giri","sender":"79ece563c40f488e88a2a95d3939e18b"}]},
         {"index":3,"previous_hash":"e64179281ee43294d3b76ee9e46ac659db023b80d844d46f76e6b308d7b99482","proof":45293,"timestamp":"2022-09-12 21:31:33.409607","transactions":[{"amount":100,"receiver":"kate","sender":"giri"},{"amount":1,"receiver":"giri","sender":"79ece563c40f488e88a2a95d3939e18b"}]}
      ],
      "message":"The nodes had different chains so the chain was replaced by the longest chains.",
      "replaced":true
   }
   </pre>
11. iterate 6 to 10


# Smart Contract
- https://remix-project.org/
- https://github.com/MyEtherWallet/etherwallet
- https://trufflesuite.com/ganache/

1. create network giricoin ico in etherwallet
<img width="1209" alt="스크린샷 2022-09-18 오후 3 49 35" src="https://user-images.githubusercontent.com/19872667/190889653-58b9ffb2-6bd6-4b36-b040-0109238bd851.png">
<img width="812" alt="스크린샷 2022-09-18 오후 3 49 28" src="https://user-images.githubusercontent.com/19872667/190889666-78ae2a94-1c99-4ddb-a959-1c087ffc315b.png"><br>
<img width="318" alt="스크린샷 2022-09-18 오후 3 49 46" src="https://user-images.githubusercontent.com/19872667/190889668-2f37086f-b65e-4c2f-914a-b55abf1eae4e.png">
2. use giricoin_ico bytecode in etherwallet index.html
<img width="1715" alt="스크린샷 2022-09-18 오후 3 49 50" src="https://user-images.githubusercontent.com/19872667/190889690-3e444281-6b4b-48c6-9b52-acb069fb4b2a.png">
3. use private key in ganache<br>
<img width="710" alt="스크린샷 2022-09-18 오후 3 49 39" src="https://user-images.githubusercontent.com/19872667/190889703-2b74140a-0fb5-4774-9f85-73654eb817fd.png">
<img width="1693" alt="스크린샷 2022-09-18 오후 3 56 41" src="https://user-images.githubusercontent.com/19872667/190889738-336ccb11-4a71-4e89-9c3c-64c3b75b08b1.png">
4. you can check transaction and block in ganache
<img width="1207" alt="스크린샷 2022-09-18 오후 3 58 27" src="https://user-images.githubusercontent.com/19872667/190889871-d49b5999-c880-47ce-a6d9-98e4b58286ba.png">
<img width="1200" alt="스크린샷 2022-09-18 오후 3 58 32" src="https://user-images.githubusercontent.com/19872667/190889875-d2ea2599-753c-41cb-a13e-381e197ee7b0.png">
<img width="1200" alt="스크린샷 2022-09-18 오후 3 58 37" src="https://user-images.githubusercontent.com/19872667/190889877-052f77ef-3484-4c96-85a0-511f5704f453.png">
<img width="1203" alt="스크린샷 2022-09-18 오후 3 59 34" src="https://user-images.githubusercontent.com/19872667/190889879-f39fa953-92d2-4af4-9ee9-722b6a482c37.png">
<img width="1204" alt="스크린샷 2022-09-18 오후 3 59 50" src="https://user-images.githubusercontent.com/19872667/190889880-c61fa70a-9179-4abd-9c7b-8ab468d03dea.png">
5. interact with contract
<img width="1705" alt="스크린샷 2022-09-18 오후 4 39 37" src="https://user-images.githubusercontent.com/19872667/190891230-2f2ae4a4-7865-4b7f-94a0-512c2020b4c2.png">
<img width="1203" alt="스크린샷 2022-09-18 오후 4 40 03" src="https://user-images.githubusercontent.com/19872667/190891232-72b2d755-f761-416d-9e4a-d1f07620f6d2.png">
<img width="1195" alt="스크린샷 2022-09-18 오후 4 40 09" src="https://user-images.githubusercontent.com/19872667/190891233-95647988-7eec-4ee0-956b-978fb6042d67.png">
