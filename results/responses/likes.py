


class AddResponse(BaseResponse):
	response = None


class DeleteResponse(BaseResponse):
	response = None


class GetListExtendedResponse(BaseResponse):
	response = None


class GetListResponse(BaseResponse):
	response = None


class IsLikedResponse(BaseResponse):
	response = None


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