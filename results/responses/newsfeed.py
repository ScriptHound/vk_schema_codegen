from typing import Optional, List, Union
from vkbottle_types.objects import GroupsGroupFull, GroupsGroup, MessagesMessage, MessagesPinnedMessage, MessagesHistoryAttachment, MessagesChatFull, MessageChatPreview, MessagesLongpollParams, MessagesLastActivity, MessagesConversation, BaseMessageError, MessagesConversationWithMessage, BaseBoolInt, MessagesChatRestrictions, MessagesChat, UsersUser, UsersUserFull, MessagesLongpollMessages, MessagesConversationMember
from .base_response import BaseResponse



class GetBannedExtendedResponse(BaseResponse):
	response: Optional["GetBannedExtendedResponseModel"] = None


class GetBannedResponse(BaseResponse):
	response: Optional["GetBannedResponseModel"] = None


class GetCommentsResponse(BaseResponse):
	response: Optional["GetCommentsResponseModel"] = None


class GetListsExtendedResponse(BaseResponse):
	response: Optional["GetListsExtendedResponseModel"] = None


class GetListsResponse(BaseResponse):
	response: Optional["GetListsResponseModel"] = None


class GetMentionsResponse(BaseResponse):
	response: Optional["GetMentionsResponseModel"] = None


class GetRecommendedResponse(BaseResponse):
	response: Optional["GetRecommendedResponseModel"] = None


class GetSuggestedSourcesResponse(BaseResponse):
	response: Optional["GetSuggestedSourcesResponseModel"] = None


class GetResponse(BaseResponse):
	response: Optional["GetResponseModel"] = None


class IgnoreItemResponse(BaseResponse):
	response: Optional["IgnoreItemResponseModel"] = None


class SaveListResponse(BaseResponse):
	response: Optional["SaveListResponseModel"] = None


class SearchExtendedResponse(BaseResponse):
	response: Optional["SearchExtendedResponseModel"] = None


class SearchResponse(BaseResponse):
	response: Optional["SearchResponseModel"] = None


class GetBannedExtendedResponseModel(BaseResponse):
	groups: Optional["array"] = None
	profiles: Optional["array"] = None


class GetBannedResponseModel(BaseResponse):
	groups: Optional["array"] = None
	members: Optional["array"] = None


class GetCommentsResponseModel(BaseResponse):
	items: Optional["array"] = None
	profiles: Optional["array"] = None
	groups: Optional["array"] = None
	next_from: Optional["string"] = None


class GetListsExtendedResponseModel(BaseResponse):
	count: Optional["integer"] = None
	items: Optional["array"] = None


class GetListsResponseModel(BaseResponse):
	count: Optional["integer"] = None
	items: Optional["array"] = None


class GetMentionsResponseModel(BaseResponse):
	count: Optional["integer"] = None
	items: Optional["array"] = None


class GetRecommendedResponseModel(BaseResponse):
	items: Optional["array"] = None
	profiles: Optional["array"] = None
	groups: Optional["array"] = None
	next_from: Optional["string"] = None


class GetSuggestedSourcesResponseModel(BaseResponse):
	count: Optional["integer"] = None
	items: Optional["array"] = None


class GetResponseModel(BaseResponse):
	items: Optional["array"] = None
	profiles: Optional["array"] = None
	groups: Optional["array"] = None
	next_from: Optional["string"] = None


class IgnoreItemResponseModel(BaseResponse):
	status: Optional["boolean"] = None


SaveListResponseModel = int


class SearchExtendedResponseModel(BaseResponse):
	items: Optional["array"] = None
	profiles: Optional["array"] = None
	groups: Optional["array"] = None
	suggested_queries: Optional["array"] = None
	next_from: Optional["string"] = None
	count: Optional["integer"] = None
	total_count: Optional["integer"] = None


class SearchResponseModel(BaseResponse):
	items: Optional["array"] = None
	suggested_queries: Optional["array"] = None
	next_from: Optional["string"] = None
	count: Optional["integer"] = None
	total_count: Optional["integer"] = None

GetBannedExtendedResponse.update_forward_refs()
GetBannedResponse.update_forward_refs()
GetCommentsResponse.update_forward_refs()
GetListsExtendedResponse.update_forward_refs()
GetListsResponse.update_forward_refs()
GetMentionsResponse.update_forward_refs()
GetRecommendedResponse.update_forward_refs()
GetSuggestedSourcesResponse.update_forward_refs()
GetResponse.update_forward_refs()
IgnoreItemResponse.update_forward_refs()
SaveListResponse.update_forward_refs()
SearchExtendedResponse.update_forward_refs()
SearchResponse.update_forward_refs()
