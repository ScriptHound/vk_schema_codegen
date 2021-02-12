

class AddResponse(BaseResponse):
	

class DocUploadResponse(BaseResponse):
	file = None

class GetByIdResponse(BaseResponse):
	

class GetTypesResponse(BaseResponse):
	count = None
	items = None

class GetUploadServer(BaseResponse):
	

class GetResponse(BaseResponse):
	count = None
	items = None

class SaveResponse(BaseResponse):
	type = None
	audio_message = None
	doc = None
	graffiti = None

class SearchResponse(BaseResponse):
	count = None
	items = None