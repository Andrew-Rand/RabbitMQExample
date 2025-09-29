## Simple Example
1) Run infra docker-compose up --build
2) Open rabbit admin on http://127.0.0.1:15672/ and see what happens
2) Run python3 basic_examples.producer_example.py (message sent)
3) Run python3 basic_examples.consumer_example.py (message handled)


## Fastapi Example
1) Run infra docker-compose up --build
2) If fastapi failed, run it again after rabbit container up
3) publish message with http 

curl --location --request POST 'http://127.0.0.1:8000/order?name=stick' \
--data ''

4) start bot python3 bot.py
5) use bot to see messages @fasgsgsdgdsgdsgdsg_bot