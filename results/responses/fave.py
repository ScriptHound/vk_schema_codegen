

class AddTagResponse(BaseResponse):
	

class GetPagesResponse(BaseResponse):
	count = None
	items = None

class GetTagsResponse(BaseResponse):
	count = None
	items = None

class GetExtendedResponse(BaseResponse):
	count = None
	items = None
	profiles = None
	groups = None

class GetResponse(BaseResponse):
	count = None
	items = None