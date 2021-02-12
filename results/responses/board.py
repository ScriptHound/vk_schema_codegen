

class AddTopicResponse(BaseResponse):
	

class CreateCommentResponse(BaseResponse):
	

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