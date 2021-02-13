


class GetFollowersFieldsResponse(BaseResponse):
	response = None


class GetFollowersResponse(BaseResponse):
	response = None


class GetSubscriptionsExtendedResponse(BaseResponse):
	response = None


class GetSubscriptionsResponse(BaseResponse):
	response = None


class GetResponse(BaseResponse):
	response = None


class SearchResponse(BaseResponse):
	response = None


class GetFollowersFieldsResponse(BaseResponse):
	count = None
	items = None


class GetFollowersResponse(BaseResponse):
	count = None
	items = None


class GetSubscriptionsExtendedResponse(BaseResponse):
	count = None
	items = None


class GetSubscriptionsResponse(BaseResponse):
	users = None
	groups = None


GetResponseModel = array


class SearchResponse(BaseResponse):
	count = None
	items = None