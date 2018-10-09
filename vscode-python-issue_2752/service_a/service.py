from nameko.rpc import rpc


class ServiceA(object):
    name="service_a"
    
    @rpc
    def echo(self, message):
        return("Service A says, '{0}'".format(message))