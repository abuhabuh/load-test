# Overview

Test against single service app.

# Todo

[] monitor uwsgi via emperor mode

# Latest

2024-10-16: Running test:
    AH HA! Moments
        - aiohttp limits concurrent connections to 100 by default

    Test 1
        - Using load_script.py to send concurrent requests to server
        - Using `tcpdump -l -i eth0 | grep -F '[S]'` to capture SYN packets so I
            can see network traffic onto the container
    Behavior 1
        - uwsgi is configured with listen queue of 100
        - When I send 200 concurrent requests, I see 100 SYN packets immediately
        - Then SYN packets come in one at a time after each request is completed
        - Looks like there's some queueing somewhere

    Test 2
        - Change listen queue to 120 and see if I get 120 SYN packets immediately
    Behavior 2
        - Still getting 100 SYN packets immediately; checked setup is correct
            because I changed uwsgi port along with listen queue parameter

    Test 3: did 80 listen queue and still 100 SYN packets immediately

    Investigation
        - Looking at tcpdump on macos loopback interface lo0 (localhost)
          `sudo tcpdump -i lo0 -A | grep "Host:\|GET\|POST"`
        - Saw 100 immediate GET requests, then occassional GET requests
          afterwards. Once I killed the load script, no more GET requests
        - Must be the python script and aiohttp
            Found aiohttp limits concurrent connections to 100 by default

    Test 4: Sent 100 requests concurrently to uwsgi process with listen queue
        of 300. aiohttp timeout set to 300 seconds.
        - load test script exited after ~120 seconds with 29 successful
          requests but 71 "Server disconnected" errors.
        - uwsgi logs show 171 requests...

2024-10-12: Setup to overwhelm server with high number of concurrent requests.
