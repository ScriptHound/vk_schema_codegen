

class GetBannedExtendedResponse(BaseResponse):
	groups = None
	profiles = None

class GetBannedResponse(BaseResponse):
	groups = None
	members = None

class GetCommentsResponse(BaseResponse):
	items = None
	profiles = None
	groups = None
	next_from = None

class GetListsExtendedResponse(BaseResponse):
	count = None
	items = None

class GetListsResponse(BaseResponse):
	count = None
	items = None

class GetMentionsResponse(BaseResponse):
	count = None
	items = None

class GetRecommendedResponse(BaseResponse):
	items = None
	profiles = None
	groups = None
	next_from = None

class GetSuggestedSourcesResponse(BaseResponse):
	count = None
	items = None

class GetResponse(BaseResponse):
	items = None
	profiles = None
	groups = None
	next_from = None

class IgnoreItemResponse(BaseResponse):
	status = None

class SaveListResponse(BaseResponse):
	

class SearchExtendedResponse(BaseResponse):
	items = None
	profiles = None
	groups = None
	suggested_queries = None
	next_from = None
	count = None
	total_count = None

class SearchResponse(BaseResponse):
	items = None
	suggested_queries = None
	next_from = None
	count = None
	total_count = None