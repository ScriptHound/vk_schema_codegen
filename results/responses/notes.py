


class AddResponse(BaseResponse):
	response = None


class CreateCommentResponse(BaseResponse):
	response = None


class GetByIdResponse(BaseResponse):
	response = None


class GetCommentsResponse(BaseResponse):
	response = None


class GetResponse(BaseResponse):
	response = None


AddResponseModel = None


CreateCommentResponseModel = None


GetByIdResponseModel = None


class GetCommentsResponse(BaseResponse):
	count = None
	items = None


class GetResponse(BaseResponse):
	count = None
	items = None