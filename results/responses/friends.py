


class AddListResponse(BaseResponse):
	response = None


class AddResponse(BaseResponse):
	response = None


class AreFriendsExtendedResponse(BaseResponse):
	response = None


class AreFriendsResponse(BaseResponse):
	response = None


class DeleteResponse(BaseResponse):
	response = None


class GetAppUsersResponse(BaseResponse):
	response = None


class GetByPhonesResponse(BaseResponse):
	response = None


class GetListsResponse(BaseResponse):
	response = None


class GetMutualResponse(BaseResponse):
	response = None


class GetMutualTargetUidsResponse(BaseResponse):
	response = None


class GetOnlineOnlineMobileResponse(BaseResponse):
	response = None


class GetOnlineResponse(BaseResponse):
	response = None


class GetRecentResponse(BaseResponse):
	response = None


class GetRequestsExtendedResponse(BaseResponse):
	response = None


class GetRequestsNeedMutualResponse(BaseResponse):
	response = None


class GetRequestsResponse(BaseResponse):
	response = None


class GetSuggestionsResponse(BaseResponse):
	response = None


class GetFieldsResponse(BaseResponse):
	response = None


class GetResponse(BaseResponse):
	response = None


class SearchResponse(BaseResponse):
	response = None


class AddListResponse(BaseResponse):
	list_id = None


AddResponseModel = None


AreFriendsExtendedResponseModel = array


AreFriendsResponseModel = array


class DeleteResponse(BaseResponse):
	success = None
	friend_deleted = None
	out_request_deleted = None
	in_request_deleted = None
	suggestion_deleted = None


GetAppUsersResponseModel = array


GetByPhonesResponseModel = array


class GetListsResponse(BaseResponse):
	count = None
	items = None


GetMutualResponseModel = array


GetMutualTargetUidsResponseModel = array


class GetOnlineOnlineMobileResponse(BaseResponse):
	online = None
	online_mobile = None


GetOnlineResponseModel = array


GetRecentResponseModel = array


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