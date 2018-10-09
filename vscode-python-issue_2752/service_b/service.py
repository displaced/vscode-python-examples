from nameko.rpc import rpc

class ServiceB(object):
    name="service_b"
    
    @rpc
    def echo(self, message):
        return("Service B says, '{0}'".format(message))