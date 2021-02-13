


class AddTagResponse(BaseResponse):
	response = None


class GetPagesResponse(BaseResponse):
	response = None


class GetTagsResponse(BaseResponse):
	response = None


class GetExtendedResponse(BaseResponse):
	response = None


class GetResponse(BaseResponse):
	response = None


AddTagResponseModel = None


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