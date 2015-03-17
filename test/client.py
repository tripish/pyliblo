#!/usr/bin/env python

import liblo, sys

# send all messages to port 1234 on the local machine
try:
    target = liblo.Address(9049)
except liblo.AddressError, err:
    print str(err)
    sys.exit()

# send message "/foo/message1" with int, float and string arguments
# liblo.send(target, "/foo/message1", 123, 456.789, "test")

# send double, int64 and char
# liblo.send(target, "/foo/message2", ('d', 3.1415), ('h', 2**42), ('c', 'x'))

# we can also build a message object first...
msg = liblo.Message("/foo/blah")
# ... append arguments later...
msg.add(123, "foo")
# ... and then send it
# liblo.send(target, msg)

# send a list of bytes as a blob
blob = [4, 8, 15, 16, 23, 42]
# liblo.send(target, "/foo/blob", blob)

# wrap a message in a bundle, to be dispatched after 2 seconds
bundle = liblo.Bundle(liblo.time() + 2.0, liblo.Message("/blubb", 123))
# liblo.send(target, bundle)




# Test message for EQ
msg = liblo.Message('/eq')
msg.add("oops1")
msg.add("poo2")
msg.add(0.123)
msg.add(1)
print "Serialise test eq: ", msg.serialise()
liblo.send(target, msg)