


class AddTopicResponse(BaseResponse):
	response = None


class CreateCommentResponse(BaseResponse):
	response = None


class GetCommentsExtendedResponse(BaseResponse):
	response = None


class GetCommentsResponse(BaseResponse):
	response = None


class GetTopicsExtendedResponse(BaseResponse):
	response = None


class GetTopicsResponse(BaseResponse):
	response = None


AddTopicResponseModel = None


CreateCommentResponseModel = None


class GetCommentsExtendedResponse(BaseResponse):
	count = None
	items = None
	poll = None
	profiles = None
	groups = None


class GetCommentsResponse(BaseResponse):
	count = None
	items = None
	poll = None


class GetTopicsExtendedResponse(BaseResponse):
	count = None
	items = None
	default_order = None
	can_add_topics = None
	profiles = None


class GetTopicsResponse(BaseResponse):
	count = None
	items = None
	default_order = None
	can_add_topics = None