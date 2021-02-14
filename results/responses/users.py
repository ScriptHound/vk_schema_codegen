from typing import Optional, List, Union
from vkbottle_types.objects import GroupsGroupFull, GroupsGroup, MessagesMessage, MessagesPinnedMessage, MessagesHistoryAttachment, MessagesChatFull, MessageChatPreview, MessagesLongpollParams, MessagesLastActivity, MessagesConversation, BaseMessageError, MessagesConversationWithMessage, BaseBoolInt, MessagesChatRestrictions, MessagesChat, UsersUser, UsersUserFull, MessagesLongpollMessages, MessagesConversationMember
from .base_response import BaseResponse



class GetFollowersFieldsResponse(BaseResponse):
	response: Optional["GetFollowersFieldsResponseModel"] = None


class GetFollowersResponse(BaseResponse):
	response: Optional["GetFollowersResponseModel"] = None


class GetSubscriptionsExtendedResponse(BaseResponse):
	response: Optional["GetSubscriptionsExtendedResponseModel"] = None


class GetSubscriptionsResponse(BaseResponse):
	response: Optional["GetSubscriptionsResponseModel"] = None


class GetResponse(BaseResponse):
	response: Optional["GetResponseModel"] = None


class SearchResponse(BaseResponse):
	response: Optional["SearchResponseModel"] = None


class GetFollowersFieldsResponseModel(BaseResponse):
	count: Optional["integer"] = None
	items: Optional["array"] = None


class GetFollowersResponseModel(BaseResponse):
	count: Optional["integer"] = None
	items: Optional["array"] = None


class GetSubscriptionsExtendedResponseModel(BaseResponse):
	count: Optional["integer"] = None
	items: Optional["array"] = None


class GetSubscriptionsResponseModel(BaseResponse):
	users: Optional["usersusersarray"] = None
	groups: Optional["groupsgroupsarray"] = None


GetResponseModel = List[UsersUserXtrCounters]


class SearchResponseModel(BaseResponse):
	count: Optional["integer"] = None
	items: Optional["array"] = None

GetFollowersFieldsResponse.update_forward_refs()
GetFollowersResponse.update_forward_refs()
GetSubscriptionsExtendedResponse.update_forward_refs()
GetSubscriptionsResponse.update_forward_refs()
GetResponse.update_forward_refs()
SearchResponse.update_forward_refs()
