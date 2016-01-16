class PresentationLayer:
	def_init_(self):
		this.name = "Presentationlayer"
		
	def setLowerLayer(self, lowerLayer):
		self.lowerLayer = lowerLayer
		
	def s3(self, param):
		print ("entramos al servicio s3")
		self.lowerLayer.s2(param)
		print("terminamos servicio s3")
