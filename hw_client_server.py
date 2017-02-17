import logging
logging.basicConfig(level=logging.DEBUG)
import argparse

import asyncio
import zmq
import zmq.asyncio

def run_as_server():
    ctx = zmq.asyncio.Context()
    loop = zmq.asyncio.ZMQEventLoop()
    asyncio.set_event_loop(loop)

    socket = ctx.socket(zmq.REP)
    socket.bind("tcp://*:5555")

    async def recv_and_process():
        while True:
            print("RX")
            msg = await socket.recv()
            print("TX")
            await socket.send(b"world +" + msg)

    asyncio.async(recv_and_process())
    loop.run_forever()


def run_as_client():
    context = zmq.Context()
    
    #  Socket to talk to server
    print("Connecting to hello world server…")
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://127.0.0.1:5555")
    
    #  Do 10 requests, waiting each time for a response
    for request in range(10):
        print("Sending request %s …" % request)
        socket.send(b"Hello")
        
        print("starting recv")
        #  Get the reply.
        message = socket.recv()
        print("Received reply %s [ %s ]" % (request, message))

        
parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--run_as', dest='run_as_role', help="run as SERVER or CLIENT")
args = parser.parse_args()
if 'CLIENT' == args.run_as_role:
    logging.info("Running as client")
    run_as_client()
    
if 'SERVER' == args.run_as_role:
    logging.info("Running as server")
    run_as_server()
