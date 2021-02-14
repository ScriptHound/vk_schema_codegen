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
	list_id: Optional["integer"] = None


AddResponseModel = int


AreFriendsExtendedResponseModel = List[FriendsFriendExtendedStatus]


AreFriendsResponseModel = List[FriendsFriendStatus]


class DeleteResponseModel(BaseResponse):
	success: Optional["integer"] = None
	friend_deleted: Optional["integer"] = None
	out_request_deleted: Optional["integer"] = None
	in_request_deleted: Optional["integer"] = None
	suggestion_deleted: Optional["integer"] = None


GetAppUsersResponseModel = List[int]


GetByPhonesResponseModel = List[FriendsUserXtrPhone]


class GetListsResponseModel(BaseResponse):
	count: Optional["integer"] = None
	items: Optional["array"] = None


GetMutualResponseModel = List[int]


GetMutualTargetUidsResponseModel = List[FriendsMutualFriend]


class GetOnlineOnlineMobileResponseModel(BaseResponse):
	online: Optional["array"] = None
	online_mobile: Optional["array"] = None


GetOnlineResponseModel = List[int]


GetRecentResponseModel = List[int]


class GetRequestsExtendedResponseModel(BaseResponse):
	count: Optional["integer"] = None
	items: Optional["array"] = None


class GetRequestsNeedMutualResponseModel(BaseResponse):
	count: Optional["integer"] = None
	items: Optional["array"] = None


class GetRequestsResponseModel(BaseResponse):
	count: Optional["integer"] = None
	items: Optional["array"] = None
	count_unread: Optional["integer"] = None


class GetSuggestionsResponseModel(BaseResponse):
	count: Optional["integer"] = None
	items: Optional["array"] = None


class GetFieldsResponseModel(BaseResponse):
	count: Optional["integer"] = None
	items: Optional["array"] = None


class GetResponseModel(BaseResponse):
	count: Optional["integer"] = None
	items: Optional["array"] = None


class SearchResponseModel(BaseResponse):
	count: Optional["integer"] = None
	items: Optional["array"] = None

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
