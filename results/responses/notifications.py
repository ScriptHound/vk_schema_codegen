


class GetResponse(BaseResponse):
	response = None


class MarkAsViewedResponse(BaseResponse):
	response = None


class SendMessageResponse(BaseResponse):
	response = None


class GetResponse(BaseResponse):
	count = None
	items = None
	profiles = None
	groups = None
	last_viewed = None
	photos = None
	videos = None
	apps = None
	next_from = None
	ttl = None


MarkAsViewedResponseModel = None


SendMessageResponseModel = array