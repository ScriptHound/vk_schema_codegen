


class AddResponse(BaseResponse):
	response = None


class DocUploadResponse(BaseResponse):
	response = None


class GetByIdResponse(BaseResponse):
	response = None


class GetTypesResponse(BaseResponse):
	response = None


class GetUploadServer(BaseResponse):
	response = None


class GetResponse(BaseResponse):
	response = None


class SaveResponse(BaseResponse):
	response = None


class SearchResponse(BaseResponse):
	response = None


AddResponseModel = None


class DocUploadResponse(BaseResponse):
	file = None


GetByIdResponseModel = array


class GetTypesResponse(BaseResponse):
	count = None
	items = None


GetUploadServerModel = None


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