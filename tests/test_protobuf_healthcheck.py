import unittest
 
class TestProtocol(unittest.TestCase):

	def test_import(self):
		import myproto
		import myproto.healthcheck_pb2

	def test_serialize_healthcheck(self):
		import myproto.healthcheck_pb2
		d = myproto.healthcheck_pb2.HealthCheckRequest()
		d.timestamp = 1234
		d2 = myproto.healthcheck_pb2.HealthCheckRequest.FromString(d.SerializeToString())
		self.assertEqual(d2.timestamp,1234)

	def test_serialize_healtcheck_response(self):
		import myproto.healthcheck_pb2
		d = myproto.healthcheck_pb2.HealthCheckResponse()
		d.timestamp_request = 1234
		d2 = myproto.healthcheck_pb2.HealthCheckResponse.FromString(d.SerializeToString())
		self.assertEqual(d2.timestamp_request,1234)




if __name__ == '__main__':
	unittest.main()
