from typing import Optional, List, Union
from vkbottle_types.objects import GroupsGroupFull, GroupsGroup, MessagesMessage, MessagesPinnedMessage, MessagesHistoryAttachment, MessagesChatFull, MessageChatPreview, MessagesLongpollParams, MessagesLastActivity, MessagesConversation, BaseMessageError, MessagesConversationWithMessage, BaseBoolInt, MessagesChatRestrictions, MessagesChat, UsersUser, UsersUserFull, MessagesLongpollMessages, MessagesConversationMember
from .base_response import BaseResponse



class AddListResponse(BaseResponse):
	response: Optional["AddListResponseModel"] = None


class AddResponse(BaseResponse):
	response: Optional["AddResponseModel"] = None


class AreFriendsExtendedResponse(BaseResponse):
	response: Optional["AreFriendsExtendedResponseModel"] = None


class AreFriendsResponse(BaseResponse):
	response: Optional["AreFriendsResponseModel"] = None


class DeleteResponse(BaseResponse):
	response: Optional["DeleteResponseModel"] = None


class GetAppUsersResponse(BaseResponse):
	response: Optional["GetAppUsersResponseModel"] = None


class GetByPhonesResponse(BaseResponse):
	response: Optional["GetByPhonesResponseModel"] = None


class GetListsResponse(BaseResponse):
	response: Optional["GetListsResponseModel"] = None


class GetMutualResponse(BaseResponse):
	response: Optional["GetMutualResponseModel"] = None


class GetMutualTargetUidsResponse(BaseResponse):
	response: Optional["GetMutualTargetUidsResponseModel"] = None


class GetOnlineOnlineMobileResponse(BaseResponse):
	response: Optional["GetOnlineOnlineMobileResponseModel"] = None


class GetOnlineResponse(BaseResponse):
	response: Optional["GetOnlineResponseModel"] = None


class GetRecentResponse(BaseResponse):
	response: Optional["GetRecentResponseModel"] = None


class GetRequestsExtendedResponse(BaseResponse):
	response: Optional["GetRequestsExtendedResponseModel"] = None


class GetRequestsNeedMutualResponse(BaseResponse):
	response: Optional["GetRequestsNeedMutualResponseModel"] = None


class GetRequestsResponse(BaseResponse):
	response: Optional["GetRequestsResponseModel"] = None


class GetSuggestionsResponse(BaseResponse):
	response: Optional["GetSuggestionsResponseModel"] = None


class GetFieldsResponse(BaseResponse):
	response: Optional["GetFieldsResponseModel"] = None


class GetResponse(BaseResponse):
	response: Optional["GetResponseModel"] = None


class SearchResponse(BaseResponse):
	response: Optional["SearchResponseModel"] = None


class AddListResponseModel(BaseResponse):
	list_id: Optional[int] = None


AddResponseModelModel = None


AreFriendsExtendedResponseModelModel = array


AreFriendsResponseModelModel = array


class DeleteResponseModel(BaseResponse):
	success: Optional[int] = None
	friend_deleted: Optional[int] = None
	out_request_deleted: Optional[int] = None
	in_request_deleted: Optional[int] = None
	suggestion_deleted: Optional[int] = None


GetAppUsersResponseModelModel = array


GetByPhonesResponseModelModel = array


class GetListsResponseModel(BaseResponse):
	count: Optional[int] = None
	items: Optional["Array"] = None


GetMutualResponseModelModel = array


GetMutualTargetUidsResponseModelModel = array


class GetOnlineOnlineMobileResponseModel(BaseResponse):
	online: Optional["Array"] = None
	online_mobile: Optional["Array"] = None


GetOnlineResponseModelModel = array


GetRecentResponseModelModel = array


class GetRequestsExtendedResponseModel(BaseResponse):
	count: Optional[int] = None
	items: Optional["Array"] = None


class GetRequestsNeedMutualResponseModel(BaseResponse):
	count: Optional[int] = None
	items: Optional["Array"] = None


class GetRequestsResponseModel(BaseResponse):
	count: Optional[int] = None
	items: Optional["Array"] = None
	count_unread: Optional[int] = None


class GetSuggestionsResponseModel(BaseResponse):
	count: Optional[int] = None
	items: Optional["Array"] = None


class GetFieldsResponseModel(BaseResponse):
	count: Optional[int] = None
	items: Optional["Array"] = None


class GetResponseModel(BaseResponse):
	count: Optional[int] = None
	items: Optional["Array"] = None


class SearchResponseModel(BaseResponse):
	count: Optional[int] = None
	items: Optional["Array"] = None

AddListResponse.update_forward_refs()
AddResponse.update_forward_refs()
AreFriendsExtendedResponse.update_forward_refs()
AreFriendsResponse.update_forward_refs()
DeleteResponse.update_forward_refs()
GetAppUsersResponse.update_forward_refs()
GetByPhonesResponse.update_forward_refs()
GetListsResponse.update_forward_refs()
GetMutualResponse.update_forward_refs()
GetMutualTargetUidsResponse.update_forward_refs()
GetOnlineOnlineMobileResponse.update_forward_refs()
GetOnlineResponse.update_forward_refs()
GetRecentResponse.update_forward_refs()
GetRequestsExtendedResponse.update_forward_refs()
GetRequestsNeedMutualResponse.update_forward_refs()
GetRequestsResponse.update_forward_refs()
GetSuggestionsResponse.update_forward_refs()
GetFieldsResponse.update_forward_refs()
GetResponse.update_forward_refs()
SearchResponse.update_forward_refs()
