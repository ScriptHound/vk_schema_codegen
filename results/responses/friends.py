

class AddListResponse(BaseResponse):
	list_id = None

class AddResponse(BaseResponse):
	

class AreFriendsExtendedResponse(BaseResponse):
	

class AreFriendsResponse(BaseResponse):
	

class DeleteResponse(BaseResponse):
	success = None
	friend_deleted = None
	out_request_deleted = None
	in_request_deleted = None
	suggestion_deleted = None

class GetAppUsersResponse(BaseResponse):
	

class GetByPhonesResponse(BaseResponse):
	

class GetListsResponse(BaseResponse):
	count = None
	items = None

class GetMutualResponse(BaseResponse):
	

class GetMutualTargetUidsResponse(BaseResponse):
	

class GetOnlineOnlineMobileResponse(BaseResponse):
	online = None
	online_mobile = None

class GetOnlineResponse(BaseResponse):
	

class GetRecentResponse(BaseResponse):
	

class GetRequestsExtendedResponse(BaseResponse):
	count = None
	items = None

class GetRequestsNeedMutualResponse(BaseResponse):
	count = None
	items = None

class GetRequestsResponse(BaseResponse):
	count = None
	items = None
	count_unread = None

class GetSuggestionsResponse(BaseResponse):
	count = None
	items = None

class GetFieldsResponse(BaseResponse):
	count = None
	items = None

class GetResponse(BaseResponse):
	count = None
	items = None

class SearchResponse(BaseResponse):
	count = None
	items = None