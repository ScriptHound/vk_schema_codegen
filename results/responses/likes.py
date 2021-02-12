

class AddResponse(BaseResponse):
	likes = None

class DeleteResponse(BaseResponse):
	likes = None

class GetListExtendedResponse(BaseResponse):
	count = None
	items = None

class GetListResponse(BaseResponse):
	count = None
	items = None

class IsLikedResponse(BaseResponse):
	liked = None
	copied = None